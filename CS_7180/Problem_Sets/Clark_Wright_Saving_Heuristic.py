
import numpy as np

# Example distance matrix: depot is 0, others are customers
distance_matrix = np.array([
    [0, 10, 20, 30, 40],
    [10, 0, 15, 25, 35],
    [20, 15, 0, 18, 28],
    [30, 25, 18, 0, 20],
    [40, 35, 28, 20, 0]
])

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
print(final_routes)


