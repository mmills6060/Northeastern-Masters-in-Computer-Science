import random
import operator
import itertools
import geppy as gep
from deap import creator, base, tools

# Define the true model
def f(a, b, c, d):
    """ The true model, which only involves three inputs on purpose. """
    return (a and d) or not c

# Generate the training set which contains all the 16 samples
X = []
Y = []
for a, b, c, d in itertools.product([True, False], repeat=4):
    X.append((a, b, c, d))
    Y.append(f(a, b, c, d))

# Creating the primitives set
pset = gep.PrimitiveSet('Main', input_names=['a', 'b', 'c', 'd'])
pset.add_function(operator.and_, 2)
pset.add_function(operator.or_, 2)
pset.add_function(operator.not_, 1)

# Define the individual class
creator.create("FitnessMax", base.Fitness, weights=(1,))
creator.create("Individual", gep.Chromosome, fitness=creator.FitnessMax)

# Register individual and population creation operations
toolbox = gep.Toolbox()
toolbox.register('gene_gen', gep.Gene, pset=pset, head_length=5)
toolbox.register('individual', creator.Individual, gene_gen=toolbox.gene_gen, n_genes=2, linker=operator.or_)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register('compile', gep.compile_, pset=pset)

# Define the regulatory gene
regulatory_gene = (
    ["mut_uniform", "cx_1p"],  # Functions to be performed
    [0.1, 0.1],  # Probabilities of each function
    [0, 1]  # Locations in the chromosome where the functions will be applied
)

def _choose_a_terminal(terminals):
    """
    Choose a terminal from the given list *terminals* randomly.

    :param terminals: iterable, terminal set
    :return: a terminal
    """
    terminal = random.choice(terminals)
    if isinstance(terminal, EphemeralTerminal):  # an Ephemeral
        terminal = copy.deepcopy(terminal)  # generate a new one
        terminal.update_value()
    return terminal


def mutate_uniform(individual, pset, ind_pb='2p'):
    """
    Uniform point mutation. For each symbol (primitive) in *individual*, change it to another randomly chosen symbol
    from *pset* with the probability *indpb*. A symbol may be a function or a terminal.

    :param individual: :class:`~geppy.core.entity.Chromosome`, the chromosome to be mutated.
    :param pset: :class:`~geppy.core.entity.PrimitiveSet`, a primitive set
    :param ind_pb: float or str, default '2p'. Probability of mutating each symbol.
        If *ind_pb* is given as a string ending with 'p',
        then it indicates the expected number of point mutations among all the symbols in *individual*. For example,
        if the total length of each gene of *individual* is `l` and there are `m` genes in total, then by passing
        `ind_pb='1.5p'` we specify approximately `ind_pb=1.5/(l*m)`.
    :return: A tuple of one chromosome

    It is typical to set a mutation rate *indpb* equivalent to two one-point mutations per chromosome. That is,
    ``indpb = 2 / len(chromosome) * len(gene)``.
    """
    if isinstance(ind_pb, str):
        assert ind_pb.endswith('p'), "ind_pb must end with 'p' if given in a string form"
        length = individual[0].head_length + individual[0].tail_length
        ind_pb = float(ind_pb.rstrip('p')) / (len(individual) * length)
    for gene in individual:
        # mutate the gene with the associated pset
        # head: any symbol can be changed into a function or a terminal
        for i in range(gene.head_length):
            if random.random() < ind_pb:
                if random.random() < 0.5:  # to a function
                    gene[i] = _choose_function(pset)
                else:
                    gene[i] = _choose_terminal(pset)
        # tail: only change to another terminal
        for i in range(gene.head_length, gene.head_length + gene.tail_length):
            if random.random() < ind_pb:
                gene[i] = _choose_terminal(pset)
    return individual,

# Define the mutation operator
def mutation_operator(individual, regulatory_gene):
    functions, probabilities, locations = regulatory_gene
    for gene_index, (func, prob, loc) in enumerate(zip(functions, probabilities, locations)):
        # Check if the mutation function should be applied based on probability
        if random.random() < prob:
            # Apply mutation based on the specified function and location
            if func == 'mut_uniform':
                # Retrieve the gene at the specified location
                gene = individual[loc]
                # Apply mutation to the gene
                mutate_uniform(gene, pset=pset)
                # Update the individual with the mutated gene
                individual[loc] = gene

# Define the crossover operator
def crossover_operator(individual1, individual2):
    functions, probabilities, locations = regulatory_gene
    if functions[1] == 'cx_1p':
        # Randomly select a gene for crossover
        which_gene = random.choice(locations)
        
        # Ensure that which_gene corresponds to a valid gene index
        if which_gene >= len(individual1):
            which_gene = random.randint(0, len(individual1) - 1)

        # Apply crossover based on the selected gene
        return gep.crossover_one_point(individual1, individual2)

# Register mutation and crossover operators with unique aliases
toolbox.register('mutate', mutation_operator, regulatory_gene=regulatory_gene)
toolbox.register('crossover', crossover_operator)

# Define the evaluation function
def evaluate(individual):
    func = toolbox.compile(individual)
    n_correct = sum(int(func(*x) == y) for x, y in zip(X, Y))
    return n_correct,

toolbox.register('evaluate', evaluate)

# Evolution function
def gep_simple(toolbox, population, n_generations, n_elites, stats=None, hall_of_fame=None, verbose=True):
    for gen in range(n_generations):
        offspring = []
        for p in population:
            # Apply mutation operator
            mutant = toolbox.clone(p)
            toolbox.mutate(mutant)

            offspring.append(mutant)

            # Select another individual for crossover
            mate = random.choice(population)
            offspring1 = toolbox.crossover(mutant, mate)
            offspring.append(offspring1)

        # Evaluate the individuals with an invalid fitness
        fitnesses = toolbox.map(toolbox.evaluate, offspring)
        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit

        # Select the next generation individuals
        elites = tools.selBest(population, n_elites)
        population[:] = tools.selBest(offspring, len(population) - len(elites)) + elites

        # Update statistics and hall of fame
        if stats is not None:
            stats.update(population)
        if hall_of_fame is not None:
            hall_of_fame.update(population)

        # Print verbose information
        if verbose:
            print(f"Generation {gen + 1} - Best fitness: {hall_of_fame[0].fitness.values[0]}")

    return population, stats

# Statistics to be inspected
stats = tools.Statistics(key=lambda ind: ind.fitness.values[0])
stats.register("avg", lambda x: sum(x) / len(x))
stats.register("min", min)
stats.register("max", max)

# Set up population and evolutionary parameters
n_pop = 50
n_gen = 50
n_elites = 1

pop = toolbox.population(n=n_pop)
hof = tools.HallOfFame(1)

# Run evolution
pop, log = gep_simple(toolbox, pop, n_gen, n_elites, stats=stats, hall_of_fame=hof)

