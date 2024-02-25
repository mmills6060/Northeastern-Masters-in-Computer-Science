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
max_profit, optimal_weights = knapsack(weights, profits, knapsack_capacity)
print(f"Maximum profit: {max_profit}")
print(f"Optimal selection of weights: {optimal_weights}")
