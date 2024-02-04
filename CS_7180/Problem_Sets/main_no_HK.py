from scipy.spatial.distance import pdist, squareform
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import combinations

def held_karp(distance_matrix):
    n = len(distance_matrix)
    C = {(1 << k, k): (distance_matrix[0, k], 0) for k in range(1, n)}
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = sum(1 << bit for bit in subset)
            for k in subset:
                prev = bits & ~(1 << k)
                res = min(((C[(prev, m)][0] + distance_matrix[m, k], m) for m in subset if m != k), key=lambda x: x[0])
                C[(bits, k)] = res
    bits = (2**n - 1) - 1
    res = min(((C[(bits, k)][0] + distance_matrix[k, 0], k) for k in range(1, n)), key=lambda x: x[0])
    opt, parent = res
    path = [0]
    for _ in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    return path, opt

def clark_wright(distance_matrix):
    num_locations = len(distance_matrix)
    savings = [(distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j], i, j) for i in range(1, num_locations) for j in range(i + 1, num_locations)]
    savings.sort(reverse=True)
    routes = {i: [i] for i in range(num_locations)}
    for saving, i, j in savings:
        if routes[i] != routes[j]:
            if routes[i][-1] == i and routes[j][0] == j:
                routes[i].extend(routes[j])
                routes[j] = routes[i]
            elif routes[j][-1] == j and routes[i][0] == i:
                routes[j].extend(routes[i])
                routes[i] = routes[j]
    unique_routes = set(tuple(route) for route in routes.values())
    final_routes = [[0] + list(route) + [0] for route in unique_routes]
    total_cost = sum(distance_matrix[route[i], route[i + 1]] for route in final_routes for i in range(len(route) - 1))
    return final_routes, total_cost

def read_cities(filepath, number_lines):
    cities = np.loadtxt(filepath, delimiter=',', max_rows=number_lines)
    return cities

def score_solution(cities, solution):
    return sum(euclidean(cities[solution[i-1]], cities[solution[i]]) for i in range(len(solution)))

def visualize_solution(cities, solution):
    fig, ax = plt.subplots(figsize=(10, 6))
    dist = score_solution(cities, solution)
    ax.set_title(f'Total Distance: {dist:.2f}')
    ax.plot(cities[solution, 0], cities[solution, 1], 'o-', mfc='r')
    ax.plot(cities[solution[0], 0], cities[solution[0], 1], 'o', color='green')  # Start
    plt.show()

def tsp_solver_silly(cities):
    best_solution = None
    best_dist = float('inf')
    for _ in range(1000):
        solution = np.random.permutation(len(cities))
        dist = score_solution(cities, solution)
        if dist < best_dist:
            best_dist, best_solution = dist, solution
    return best_solution

def generate_distance_matrix(cities):
    """Generate a distance matrix from city coordinates using Euclidean distance."""
    return squareform(pdist(cities, 'euclidean'))

def main():
    hk_times = []
    cw_times = []
    num_cities_to_read = 10
    while num_cities_to_read < 110:
        cities_filepath = 'medium.csv'
        cities = read_cities(cities_filepath, num_cities_to_read)
        distance_matrix = generate_distance_matrix(cities)
 
        # Held-Karp Algorithm Execution
        start_time_hk = time.time()
        #hk_path, hk_cost = held_karp(distance_matrix)
        #end_time_hk = time.time()
        #hk_execution_time = format(end_time_hk - start_time_hk, '.20f')
        #print(f"HK cost: {hk_cost}")
        #print(f"HK execution time: {hk_execution_time}")
        # Clark-Wright Algorithm Execution
        start_time_cw = time.time()
        cw_routes, cw_cost = clark_wright(distance_matrix)
        end_time_cw = time.time()
        cw_execution_time = format(end_time_cw - start_time_cw, '.20f')
        print(f"cw cost: {cw_cost}")
        print(f"cw execution time: {cw_execution_time}")
        num_cities_to_read = num_cities_to_read + 10
        cw_times.append(end_time_cw - start_time_cw)
if __name__ == "__main__":
    main()
