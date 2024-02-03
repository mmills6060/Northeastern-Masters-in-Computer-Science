import time
import itertools
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
import pandas as pd

def held_karp(distance_matrix):
    n = len(distance_matrix)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (distance_matrix[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distance_matrix[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distance_matrix[k][0], k))
    opt, parent = min(res)
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    path.append(0)

    return list(reversed(path)), opt

def clark_wright(distance_matrix):

    num_locations = distance_matrix.shape[0]
    savings = []
    for i in range(1, num_locations):
        for j in range(i + 1, num_locations):
            saving = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
            savings.append((saving, i, j))
    savings.sort(reverse=True)
    routes = [[i] for i in range(1, num_locations)]

    def find_route(routes, customer):
        for route in routes:
            if customer in route:
                return route
        return None

    for saving, cust1, cust2 in savings:
        route1 = find_route(routes, cust1)
        route2 = find_route(routes, cust2)

        if route1 != route2 and (route1[0] == cust1 or route1[-1] == cust1) and (route2[0] == cust2 or route2[-1] == cust2):
            # Ensure cust1 is at the end of its route and cust2 at the start of its route
            if route1[0] == cust1:
                route1.reverse()
            if route2[-1] == cust2:
                route2.reverse()
            
            new_route = route1 + route2
            routes.remove(route1)
            routes.remove(route2)
            routes.append(new_route)

    final_routes = [[0] + route + [0] for route in routes]
    return final_routes



def read_cities(filepath, numberlines):
    '''
    Load a TSP dataset.
    This function works for loading CSV files generated
    by the data/make_data.py script.
    '''
    with open(filepath, 'r') as file:
        lines = [next(file) for _ in range(numberlines)]
    cities = np.loadtxt(lines, delimiter=',')
    return cities


def score_solution(cities, solution):
    '''
    Calculate the total distance traveled by the given solution.
    This function scores a TSP solution by computing the total
    distance the salesperson would travel. Lower is better!
    The 'solution' array must contain indices into the 'cities'
    array. Also, the 'solution' array must visit each city exactly
    once!
    '''

    if len(solution) != len(cities):
        raise Exception(('Invalid solution: len(solution) is {}, ' + \
                'but it should be {}.').format(len(solution), len(cities)))

    if set(solution) != set(range(len(cities))):
        raise Exception('Invalid solution: The solution does not ' + \
                'visit each city exactly once!')

    dist = 0.0
    for i in range(len(solution)):
        p_prev = cities[solution[i-1]]
        p_here = cities[solution[i]]
        dist += euclidean(p_prev, p_here)
    return dist


def create_figure():
    '''
    Creates a figure which `visualize_solution()` will draw onto.
    '''
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    return fig, axes


def visualize_solution(cities, solution, fig=None, axes=None, block=True):
    '''
    Visualize the solution in a 2D plot.
    The 'cities' and 'solution' arguments are the same
    as to the `score_solution()` function.
    '''
    dist = score_solution(cities, solution) if len(solution) == len(cities) else float('NaN')

    if fig is None or axes is None:
        fig, axes = create_figure()
    ax1, ax2 = axes
    fig.suptitle('Total Distance: {}'.format(dist), fontsize=20)

    ax1.clear()
    ax1.scatter(cities[:,0], cities[:,1])

    if len(solution) == len(cities):
        path = np.hstack((solution, solution[0]))  # <-- the salesperson has to return home!
    else:
        path = solution
    ax2.clear()
    ax2.plot(cities[path,0], cities[path,1])
    ax2.scatter(cities[:,0], cities[:,1])

    if block:
        while plt.fignum_exists(fig.number):
            plt.pause(0.001)
    else:
        plt.pause(0.001)


def tsp_solver_silly(cities, new_best_solution_func = None):
    '''
    This TSP solver is super silly.
    This solver simply randomizes several solutions then
    keeps the one which is best.
    '''
    best_dist = float("inf")
    best_solution = None
    for i in range(1000):
        solution = np.arange(len(cities))
        np.random.shuffle(solution)
        dist = score_solution(cities, solution)
        if dist < best_dist:
            best_dist = dist
            best_solution = solution
            if new_best_solution_func:
                new_best_solution_func(solution)
    return best_solution
def main():

    #plt.ion()   # turn interactive mode on
    iteration = 0 
    distance_matrix = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
                               )

    while iteration < 20:

        start_time = time.time()
        iteration = iteration + 1
        path, cost = held_karp(distance_matrix)
        end_time = time.time()
        print("Held-Karp Execution time", end_time - start_time, "seconds")

    iteration = 0 
    while iteration < 20:

        start_time = time.time()
        iteration = iteration + 1
        clark_path = clark_wright(distance_matrix)
        end_time = time.time()
        print("Clark Execution time", end_time - start_time, "seconds")

    numbercities = 0
    run = 0
    run1 = 0 
    run2 = 0 
    run3 = 0 
    run4 = 0 
    run5 = 0 
    run6 = 0 
    run7 = 0 
    run8 = 0 
    run9 = 0 
    run10 = 0 
    run11 = 0 
    run12 = 0 
    run13 = 0 
    run14 = 0 
    run15 = 0 
    run16 = 0 
    run17 = 0 
    run18 = 0 
    run19 = 0 
    run20 = 0 

    execution_times = []
    heldcarp_execution_times = []
    clarkwright_execution_times = []
    while run != 20:
        run = run + 1
        while numbercities != 100:
    
            start_time = time.time()
            numbercities = numbercities + 10
            cities = read_cities('medium.csv', numbercities)
            show_progress = True
            if not show_progress:
                solution = tsp_solver_silly(cities)
                visualize_solution(cities, solution)
            else:
                fig, axes = create_figure()

                # Closure over cities, fig, and axes:
                def visualize_wrapper(solution, is_final=False):
                    if is_final:
                        print ('FINAL SOLUTION:', score_solution(cities, solution), solution)
                        visualize_solution(cities, solution, fig, axes, block=is_final)
                    else:
                        print ('Best so far:', score_solution(cities, solution), solution)
                        visualize_solution(cities, solution, fig, axes, block=is_final)
                solution = tsp_solver_silly(cities, visualize_wrapper)
                end_time = time.time()
                execution_time = end_time - start_time
                execution_times.append(execution_time)
                print("Execution time", execution_time, "seconds")
                visualize_wrapper(solution, True)
                if run == 1:
                    run1 = execution_time 
                if run == 2:
                    run2 = execution_time 
                if run == 3:
                    run3 = execution_time 
                if run == 4:
                    run4 = execution_time 
                if run == 5:
                    run5 = execution_time 
                if run == 6:
                    run6 = execution_time 
                if run == 7:
                    run7 = execution_time 
                if run == 8:
                    run8 = execution_time 
                if run == 9:
                    run9 = execution_time 
                if run == 10:
                    run10 = execution_time 
                if run == 11:
                    run11 = execution_time 
                if run == 12:
                    run12 = execution_time 
                if run == 13:
                    run13 = execution_time 
                if run == 14:
                    run14 = execution_time 
                if run == 15:
                    run15 = execution_time 
                if run == 16:
                    run16 = execution_time 
                if run == 17:
                    run17 = execution_time 
                if run == 18:
                    run18 = execution_time 
                if run == 19:
                    run19 = execution_time 
                if run == 20:
                    run20 = execution_time 
                average = run1 + run2 + run3 + run4 + run5 + run6 + run7 + run8 + run9 + run10 + run11 + run12 + run13 + run14 + run15 + run16 + run17 + run18 + run19 + run20 

                print("Average: ", average)

    run = 0
    numbercities = 0
    while run != 20:
        run = run + 1
        while numbercities != 100:
    
            start_time = time.time()
            numbercities = numbercities + 10
            cities = read_cities('medium.csv', numbercities)
            show_progress = True
            if not show_progress:
                solution = tsp_solver_silly(cities)
                visualize_solution(cities, solution)
            else:
                fig, axes = create_figure()

                # Closure over cities, fig, and axes:
                def visualize_wrapper(solution, is_final=False):
                    if is_final:
                        print ('FINAL SOLUTION:', score_solution(cities, solution), solution)
                        visualize_solution(cities, solution, fig, axes, block=is_final)
                    else:
                        print ('Best so far:', score_solution(cities, solution), solution)
                        visualize_solution(cities, solution, fig, axes, block=is_final)
                solution = tsp_solver_silly(cities, visualize_wrapper)
                end_time = time.time()
                execution_time = end_time - start_time
                clarkwright_execution_times.append(execution_time)
                print("Execution time", execution_time, "seconds")
                visualize_wrapper(solution, True)
                if run == 1:
                    run1 = execution_time 
                if run == 2:
                    run2 = execution_time 
                if run == 3:
                    run3 = execution_time 
                if run == 4:
                    run4 = execution_time 
                if run == 5:
                    run5 = execution_time 
                if run == 6:
                    run6 = execution_time 
                if run == 7:
                    run7 = execution_time 
                if run == 8:
                    run8 = execution_time 
                if run == 9:
                    run9 = execution_time 
                if run == 10:
                    run10 = execution_time 
                if run == 11:
                    run11 = execution_time 
                if run == 12:
                    run12 = execution_time 
                if run == 13:
                    run13 = execution_time 
                if run == 14:
                    run14 = execution_time 
                if run == 15:
                    run15 = execution_time 
                if run == 16:
                    run16 = execution_time 
                if run == 17:
                    run17 = execution_time 
                if run == 18:
                    run18 = execution_time 
                if run == 19:
                    run19 = execution_time 
                if run == 20:
                    run20 = execution_time 
                average = run1 + run2 + run3 + run4 + run5 + run6 + run7 + run8 + run9 + run10 + run11 + run12 + run13 + run14 + run15 + run16 + run17 + run18 + run19 + run20 

                print("Average: ", average)

    run = 0
    numbercities = 0
    while run != 20:
        run = run + 1
        while numbercities != 100:
    
            start_time = time.time()
            numbercities = numbercities + 10
            cities = read_cities('medium.csv', numbercities)
            show_progress = True
            if not show_progress:
                solution = tsp_solver_silly(cities)
                visualize_solution(cities, solution)
            else:
                fig, axes = create_figure()

                # Closure over cities, fig, and axes:
                def visualize_wrapper(solution, is_final=False):
                    if is_final:
                        print ('FINAL SOLUTION:', score_solution(cities, solution), solution)
                        visualize_solution(cities, solution, fig, axes, block=is_final)
                    else:
                        print ('Best so far:', score_solution(cities, solution), solution)
                        visualize_solution(cities, solution, fig, axes, block=is_final)
                solution = tsp_solver_silly(cities, visualize_wrapper)
                end_time = time.time()
                execution_time = end_time - start_time
                heldcarp_execution_times.append(execution_time)
                print("Execution time", execution_time, "seconds")
                visualize_wrapper(solution, True)
                if run == 1:
                    run1 = execution_time 
                if run == 2:
                    run2 = execution_time 
                if run == 3:
                    run3 = execution_time 
                if run == 4:
                    run4 = execution_time 
                if run == 5:
                    run5 = execution_time 
                if run == 6:
                    run6 = execution_time 
                if run == 7:
                    run7 = execution_time 
                if run == 8:
                    run8 = execution_time 
                if run == 9:
                    run9 = execution_time 
                if run == 10:
                    run10 = execution_time 
                if run == 11:
                    run11 = execution_time 
                if run == 12:
                    run12 = execution_time 
                if run == 13:
                    run13 = execution_time 
                if run == 14:
                    run14 = execution_time 
                if run == 15:
                    run15 = execution_time 
                if run == 16:
                    run16 = execution_time 
                if run == 17:
                    run17 = execution_time 
                if run == 18:
                    run18 = execution_time 
                if run == 19:
                    run19 = execution_time 
                if run == 20:
                    run20 = execution_time 
                average = run1 + run2 + run3 + run4 + run5 + run6 + run7 + run8 + run9 + run10 + run11 + run12 + run13 + run14 + run15 + run16 + run17 + run18 + run19 + run20 

                print("Average: ", average)



    plt.plot(range(1, len(execution_times) + 1), execution_times, marker='o')
    plt.plot(range(1, len(heldcarp_execution_times) + 1), heldcarp_execution_times, marker='o')
    plt.plot(range(1, len(clarkwright_execution_times) + 1), clarkwright_execution_times, marker='o')
    plt.title('Execution Times for Each Run')
    plt.xlabel('No of Cities')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()


