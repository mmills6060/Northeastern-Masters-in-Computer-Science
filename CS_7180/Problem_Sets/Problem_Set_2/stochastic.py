import random
def tsp_cost(matrix, tour):
    # Calculate the total cost of the tour
    return sum(matrix[tour[i-1]][tour[i]] for i in range(len(tour)))
def random_restart_tsp(matrix, max_restarts):
    best_tour = None
    best_cost = float('inf')
    for _ in range(max_restarts):
        # Generate a random tour
        tour = list(range(len(matrix)))
        random.shuffle(tour)
        # Hill climbing
        for _ in range(len(matrix)**2):
            i, j = random.sample(range(len(matrix)), 2)
            # Swap two cities and see if it improves the tour
            tour[i], tour[j] = tour[j], tour[i]
            cost = tsp_cost(matrix, tour)
            if cost < best_cost:
                best_tour = tour[:]
                best_cost = cost
    return best_tour, best_cost

def knapsack_value(weights, profits, capacity, selection):
    # Calculate the total weight and profit of the selection
    total_weight = sum(weights[i] for i in range(len(weights)) if selection[i])
    total_profit = sum(profits[i] for i in range(len(profits)) if selection[i])
    # If the total weight exceeds the capacity, return 0
    return total_profit if total_weight <= capacity else 0
def random_restart_knapsack(weights, profits, capacity, max_restarts):
    best_selection = None
    best_value = 0
    for _ in range(max_restarts):
        # Generate a random selection
        selection = [random.choice([0, 1]) for _ in range(len(weights))]
        # Hill climbing
        for _ in range(len(weights)**2):
            i = random.randint(0, len(weights) - 1)
            # Flip the selection of an item and see if it improves the value
            selection[i] = 1 - selection[i]
            value = knapsack_value(weights, profits, capacity, selection)
            if value > best_value:
                best_selection = selection[:]
                best_value = value
    return best_selection, best_value




capacity = 165
weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
max_restarts = 10


best_selection, best_value = random_restart_knapsack(weights, profits, capacity, max_restarts)
print(f"Best Selection: {best_selection}")
print(f"Best Value: {best_value}")











