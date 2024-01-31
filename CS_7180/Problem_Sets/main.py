import time
import itertools
import numpy as np
def held_karp(distance_matrix):
    n = len(distance_matrix)
    # Maps each subset of the nodes to the cost to reach that subset, as well as what node it entered the subset from
    C = {}

    # Set the base case
    for k in range(1, n):
        C[(1 << k, k)] = (distance_matrix[0][k], 0)

    # Iterate over subsets of increasing size and compute their minimal cost paths
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distance_matrix[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distance_matrix[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add start city
    path.append(0)

    return list(reversed(path)), opt
def clark_wright(distance_matrix):

    # Number of locations (including depot)
    num_locations = distance_matrix.shape[0]

    # Initialize savings list
    savings = []

    # Calculate savings for each pair of customers
    for i in range(1, num_locations):
        for j in range(i + 1, num_locations):
            saving = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
            savings.append((saving, i, j))

    # Sort the savings in descending order
    savings.sort(reverse=True)

    # Initialize routes (each customer initially has a separate route)
    routes = [[i] for i in range(1, num_locations)]

    # Function to find route containing a specific customer
    def find_route(routes, customer):
        for route in routes:
            if customer in route:
                return route
        return None

    # Merge routes based on savings
    for saving, cust1, cust2 in savings:
        route1 = find_route(routes, cust1)
        route2 = find_route(routes, cust2)

        # Only merge if cust1 and cust2 are in different routes and the merge doesn't form a loop
        if route1 != route2 and (route1[0] == cust1 or route1[-1] == cust1) and (route2[0] == cust2 or route2[-1] == cust2):
            # Ensure cust1 is at the end of its route and cust2 at the start of its route
            if route1[0] == cust1:
                route1.reverse()
            if route2[-1] == cust2:
                route2.reverse()
            
            # Merge the two routes
            new_route = route1 + route2
            routes.remove(route1)
            routes.remove(route2)
            routes.append(new_route)

    # Final routes (adding depot at start and end)
    final_routes = [[0] + route + [0] for route in routes]
    return final_routes


def main():

    iteration = 0 
    distance_matrix = np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
                               )

    start_time = time.time()
    while iteration < 20:
        iteration = iteration + 1
        path, cost = held_karp(distance_matrix)
    end_time = time.time()

    print("Held-Karp Execution time", end_time - start_time, "seconds")

    iteration = 0 
    start_time = time.time()
    while iteration < 20:
        iteration = iteration + 1
        clark_path = clark_wright(distance_matrix)
    end_time = time.time()

    print("Clark Execution time", end_time - start_time, "seconds")





if __name__ == "__main__":
    main()


