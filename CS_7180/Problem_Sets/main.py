from scipy.spatial.distance import pdist, squareform
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import combinations

def held_karp(distance_matrix):
    num_cities = len(distance_matrix)
    memo = {(1 << k, k): (distance_matrix[0, k], 0) for k in range(1, num_cities)}
    for subset_size in range(2, num_cities):
        for subset in combinations(range(1, num_cities), subset_size):
            bits = sum(1 << bit for bit in subset)
            for k in subset:
                prev_bits = bits & ~(1 << k)
                min_distance = float('inf')
                min_index = None
                for m in subset:
                    if m != k:
                        distance = memo[(prev_bits, m)][0] + distance_matrix[m, k]
                        if distance < min_distance:
                            min_distance = distance
                            min_index = m
                memo[(bits, k)] = (min_distance, min_index)
    final_bits = (2 ** num_cities - 1) - 1
    min_distance = float('inf')
    min_index = None
    for k in range(1, num_cities):
        distance = memo[(final_bits, k)][0] + distance_matrix[k, 0]
        if distance < min_distance:
            min_distance = distance
            min_index = k
    path = [0]
    parent = min_index
    bits = final_bits
    for _ in range(num_cities - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        parent = memo[(bits, parent)][1]
        bits = new_bits
    path.append(0)
    
    return path, min_distance




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

def generate_distance_matrix(cities):
    return squareform(pdist(cities, 'euclidean'))

def main():
    hk_times = []
    cw_times = []
    num_cities_to_read = 2
    while num_cities_to_read < 20:
        cities_filepath = 'medium.csv'
        cities = read_cities(cities_filepath, num_cities_to_read)
        distance_matrix = generate_distance_matrix(cities)
 
        # Held-Karp Algorithm Execution
        start_time_hk = time.time()
        hk_path, hk_cost = held_karp(distance_matrix)
        end_time_hk = time.time()
        hk_execution_time = format(end_time_hk - start_time_hk, '.20f')
        print(f"HK cost: {hk_cost}")
        print(f"HK execution time: {hk_execution_time}")
        # Clark-Wright Algorithm Execution
        start_time_cw = time.time()
        cw_routes, cw_cost = clark_wright(distance_matrix)
        end_time_cw = time.time()
        cw_execution_time = format(end_time_cw - start_time_cw, '.20f')
        print(f"cw cost: {cw_cost}")
        print(f"cw execution time: {cw_execution_time}")
        num_cities_to_read = num_cities_to_read + 1
        hk_times.append(end_time_hk - start_time_hk)
        cw_times.append(end_time_cw - start_time_cw)
    # Plotting execution times
    fig, ax = plt.subplots()
    indices = np.arange(1, len(hk_times) + 1)
    ax.plot(indices, hk_times, label='Held-Karp', marker='o')
    ax.plot(indices, cw_times, label='Clark-Wright', marker='x')
    ax.set_xlabel('Run Number')
    ax.set_ylabel('Execution Time (s)')
    ax.set_title('Execution Times for Held-Karp vs. Clark-Wright')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
