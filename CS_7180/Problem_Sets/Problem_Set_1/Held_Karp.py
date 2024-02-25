import itertools
import pandas as pd
import csv
import math



def held_karp(distance_matrix):
    n = len(distance_matrix)
    print(f"Length of distance matrix {n}")
    # Maps each subset of the nodes to the cost to reach that subset, as well as what node it entered the subset from
    C = {}

    # Set the base case
    for k in range(1, n):
        print(f"Completed base case {k} of {n}")
        C[(1 << k, k)] = (distance_matrix[0][k], 0)

    # Iterate over subsets of increasing size and compute their minimal cost paths
    for subset_size in range(2, n):
        print(f"Completed subset size {subset_size} of {n}")
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


def calculate_distance(p1, p2):
    # Euclidean distance between two points
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def load_coordinates_and_generate_matrix(file_path):
    coordinates = []
    with open(file_path, 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            # Assuming each row is x,y
            coordinates.append((float(row[0]), float(row[1])))
    
    n = len(coordinates)
    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):  # Distance is symmetric, no need to compute twice
            distance = calculate_distance(coordinates[i], coordinates[j])
            distance_matrix[i][j] = distance_matrix[j][i] = distance
    
    return distance_matrix

# Example usage
file_path = '20cities.csv'  # Update this to your actual file path
print("Loading coordinates and generating matrix")
distance_matrix = load_coordinates_and_generate_matrix(file_path)

# Now you can use the generated distance matrix with your held_karp function
print("Determining path and cost")
path, cost = held_karp(distance_matrix)
print(path, cost)



