from scipy.spatial.distance import pdist, squareform
import csv
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import combinations

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
    stochastic_times = []
    num_cities_to_read = 2
    while num_cities_to_read < 100:
        cities_filepath = 'medium.csv'
        cities = read_cities(cities_filepath, num_cities_to_read)
        matrix = generate_distance_matrix(cities)
        max_restarts = 10 
        # Stochastic Algorithm Execution
        start_time_stochastic = time.time()
        stochastic_path, stochastic_cost = random_restart_tsp(matrix, max_restarts)
        end_time_stochastic = time.time()
        hk_execution_time = format(end_time_stochastic - start_time_stochastic, '.20f')
        print(f"Number of Cities: {num_cities_to_read} Stochastic cost: {stochastic_cost} Stochastic execution time: {hk_execution_time}")
        stochastic_times.append(end_time_stochastic - start_time_stochastic)
        num_cities_to_read += 1

#        with open('tsp_medium_stochastic.csv', 'a', newline='') as file:
#            writer = csv.writer(file)
#            writer.writerow([num_cities_to_read, stochastic_cost, hk_execution_time])

    # Plotting execution times
    fig, ax = plt.subplots()
    indices = np.arange(1, len(stochastic_times) + 1)
    ax.plot(indices, stochastic_times, label='Stochastic', marker='o')
    ax.set_xlabel('Run Number')
    ax.set_ylabel('Execution Time (s)')
    ax.set_title('Execution Times for Held-Karp vs. Clark-Wright')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()
