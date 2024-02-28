from scipy.spatial.distance import pdist, squareform
import csv
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from itertools import combinations
import requests

def stochastic_knapsack(weights, profits, capacity, max_restarts=1000, max_iterations=1000):
    n = len(profits)
    best_weights = [0] * n
    best_profit = 0
    for _ in range(max_restarts):
        current_weights = [0] * n
        current_profit = 0
        current_capacity = capacity
        for _ in range(max_iterations):
            i = random.randint(0, n - 1)  # Choose a random item
            if weights[i] <= current_capacity:  # If the item fits, add it
                current_weights[i] = 1
                current_profit += profits[i]
                current_capacity -= weights[i]
            if current_profit > best_profit:  # If this is the best solution so far, keep it
                best_profit = current_profit
                best_weights = current_weights.copy()
        if current_profit >= best_profit:  # If we didn't find a better solution, restart
            current_weights = [0] * n
            current_profit = 0
            current_capacity = capacity
    return best_profit, best_weights

def knapsack(weights, profits, capacity):
    n = len(profits)
    # Create a matrix to store the maximum profit for each combination of items and capacities
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]
    # Fill the first row
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    # Fill the rest of the matrix
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            # Include the item if its weight is less than or equal to the current capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]
            # Exclude the item
            profit2 = dp[i - 1][c]
            # Store the maximum profit
            dp[i][c] = max(profit1, profit2)
    # The maximum profit is at the bottom-right corner of the matrix
    max_profit = dp[n - 1][capacity]
    # Find the optimal selection of weights
    optimal_weights = [0] * n
    i, c = n - 1, capacity
    while i > 0 and c > 0:
        if dp[i][c] != dp[i - 1][c]:
            optimal_weights[i] = 1
            c -= weights[i]
        i -= 1
    if c != 0:
        optimal_weights[0] = 1
    return max_profit, optimal_weights



knapsack_capacity = 165
weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
max_profit, optimal_weights = stochastic_knapsack(weights, profits, knapsack_capacity)
print(f"Maximum profit: {max_profit}")
print(f"Optimal selection of weights: {optimal_weights}")



def main():


    problem_number = 8
    knapsack_times = []
    iterations = 1
    while iterations < 21:
        print(f"Iteration: {iterations}")
        capacity_url = f"https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p0{problem_number}_c.txt"
        response = requests.get(capacity_url)
        # Ensure we fetched the file successfully
        if response.status_code == 200:
            capacity = int(response.text.strip())
        else:
            print(f"Failed to fetch the file: {response.status_code}")

        weights_url = f"https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p0{problem_number}_w.txt"
        response = requests.get(weights_url)
        # Ensure we fetched the file successfully
        if response.status_code == 200:
            weights = [int(weight) for weight in response.text.split('\n') if weight]
        else:
            print(f"Failed to fetch the file: {response.status_code}")

        profits_url = f"https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p0{problem_number}_p.txt"
        response = requests.get(profits_url)
        # Ensure we fetched the file successfully
        if response.status_code == 200:
            profits = [int(profit) for profit in response.text.split('\n') if profit]
        else:
            print(f"Failed to fetch the file: {response.status_code}")

        optimal_url = f"https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/p0{problem_number}_s.txt"
        response = requests.get(optimal_url)
        # Ensure we fetched the file successfully
        if response.status_code == 200:
            optimals = [int(optimal) for optimal in response.text.split('\n') if optimal]
        else:
            print(f"Failed to fetch the file: {response.status_code}")


        start_time_knapsack = time.time()
        max_profit, optimal_weights = knapsack(weights, profits, capacity)
        end_time_knapsack = time.time()
        knapsack_execution_time = (end_time_knapsack - start_time_knapsack) * 1000
        knapsack_times.append(knapsack_execution_time)
        with open('stochastic_knapsack_p08.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([problem_number, max_profit, knapsack_execution_time])


        iterations += 1



'''
    # Plotting execution times
    fig, ax = plt.subplots()
    indices = np.arange(1, len(knapsack_times) + 1)
    ax.plot(indices, knapsack_times, label='Stochastic', marker='o')
    ax.set_xlabel('Run Number')
    ax.set_ylabel('Execution Time (s)')
    ax.set_title('Execution Times for Held-Karp vs. Clark-Wright')
    ax.legend()
    plt.show()
'''

if __name__ == "__main__":
    main()


