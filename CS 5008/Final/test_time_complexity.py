import random
import time
import timeit
import matplotlib.pyplot as plt
import algorithms
def time_complexity_increasing_number_of_files():
    initial_file_sizes = [10, 50, 100, 10, 20, 1, 5, 2, 7, 12]  # Initial input sizes
    storage_sizes = [1000, 5000, 100, 500]  # Example input sizes
    execution_times1 = []  # For allocate_files
    execution_times2 = []  # For allocate_files_with_priority
    execution_times3 = []  # For allocate_files_with_priority
    execution_times4 = []  # For allocate_files_with_priority
    execution_times5 = []  # For allocate_files_with_priority
    file_sizes = initial_file_sizes.copy()

    while len(file_sizes) <= 300:
        
        for files in file_sizes:
            for storage in storage_sizes:
                start_time = time.time()
                result = algorithms.allocate_files(file_sizes, storage_sizes)
                end_time = time.time()
                execution_time = end_time
                execution_times1.append((len(file_sizes), storage, execution_time))

        file_sizes.append(random.randint(1, 5))  # Add a random integer between 1 and 10 to file_sizes

    file_sizes = initial_file_sizes.copy()  # Reset file_sizes for the second function
    while len(file_sizes) <= 300:
        for files in file_sizes:
            for storage in storage_sizes:  # Assuming storage_sizes is defined earlier
                start_time = time.time()
                duplication_factor = 2  # Generate random priorities
                # Perform calculations using duplication_factor, files, and storage
                # You might want to call your function here
                result = algorithms.allocate_files_with_duplication(file_sizes, storage_sizes, duplication_factor)
                end_time = time.time()
                execution_time = end_time
                execution_times2.append((len(file_sizes), storage, execution_time))

        file_sizes.append(random.randint(1, 10))  # Add a random integer between 1 and 10 to file_sizes
    file_sizes = initial_file_sizes.copy()  # Reset file_sizes for the second function
    while len(file_sizes) <= 300:
        for files in file_sizes:
            for storage in storage_sizes:
                start_time = time.time()
                sharing_factor = 1
                result = algorithms.allocate_files_with_file_sharing(file_sizes, storage_sizes, sharing_factor)
                end_time = time.time()
                execution_time = end_time 
                execution_times3.append((len(file_sizes), storage, execution_time))

        file_sizes.append(random.randint(1, 10))  # Add a random integer between 1 and 10 to file_sizes

    file_sizes = initial_file_sizes.copy()  # Reset file_sizes for the second function
    while len(file_sizes) <= 300:
        for files in file_sizes:
            for storage in storage_sizes:
                start_time = time.time()
                priority = [1,2,3,2,1,2,3,2,1,2]  # Generate random priorities
                result = algorithms.allocate_files_with_priority(file_sizes, storage_sizes, priority)
                end_time = time.time()
                execution_time = end_time 
                execution_times4.append((len(file_sizes), storage, execution_time))

        file_sizes.append(random.randint(1, 10))  # Add a random integer between 1 and 10 to file_sizes
    file_sizes = initial_file_sizes.copy()  # Reset file_sizes for the second function
    while len(file_sizes) <= 300:
        for files in file_sizes:
            for storage in storage_sizes:
                start_time = time.time()
                priority = [1,2,3,2,1,2,3,2,1,2]  # Generate random priorities
                duplication_factor = 2  # Generate random priorities
                sharing_factor = 2  # Generate random priorities
                result = algorithms.allocate_files_with_priority_duplication_file_sharing(file_sizes, storage_sizes, priority, duplication_factor, sharing_factor)
                end_time = time.time()
                execution_time = end_time 
                execution_times5.append((len(file_sizes), storage, execution_time))

        file_sizes.append(random.randint(1, 10))  # Add a random integer between 1 and 10 to file_sizes

    file_sizes = initial_file_sizes.copy()  # Reset file_sizes for the second function


    # Separate execution times for plotting
    num_files1 = [item[0] for item in execution_times1]
    storage_sizes1 = [item[1] for item in execution_times1]
    times1 = [item[2] for item in execution_times1]

    num_files2 = [item[0] for item in execution_times2]
    storage_sizes2 = [item[1] for item in execution_times2]
    times2 = [item[2] for item in execution_times2]

    num_files3 = [item[0] for item in execution_times3]
    storage_sizes3 = [item[1] for item in execution_times3]
    times3 = [item[2] for item in execution_times3]


    num_files4 = [item[0] for item in execution_times4]
    storage_sizes4 = [item[1] for item in execution_times4]
    times4 = [item[2] for item in execution_times4]


    num_files5 = [item[0] for item in execution_times5]
    storage_sizes5 = [item[1] for item in execution_times5]
    times5 = [item[2] for item in execution_times5]

    print("starting print times")
    print(times1)
    print(times2)
    print(times3)
    print(times4)
    print(times5)
    # Create scatter plots for both functions
    plt.scatter(num_files1, times1, label="allocate_files")
    plt.scatter(num_files2, times2, label="allocate_files_with_duplication")
    plt.scatter(num_files3, times3, label="allocate_files_with_file_sharing")
    plt.scatter(num_files4, times4, label="allocate_files_with_priority")
    plt.scatter(num_files5, times5, label="allocate_files_with_everything")
    plt.xlabel("Number of Files")
    plt.ylabel("Execution Time")
    plt.title("Execution Time vs. Number of Files")
    plt.legend()
    plt.show()
def multiple_knapsack(values, weights, capacities):
    num_knapsacks = len(capacities)
    num_items = len(values)

    dp = [[0] * (num_knapsacks + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(1, num_knapsacks + 1):
            if weights[i - 1] <= capacities[j - 1]:
                dp[i][j] = max(dp[i - 1][j],
                               dp[i - 1][j - 1] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[num_items][num_knapsacks]

def plot_time_complexity():
    num_items_range = range(1, 101)  # Vary the number of items from 1 to 10
    execution_times = []

    for num_items in num_items_range:
        values = [10] * num_items
        weights = [5] * num_items
        capacities = [15, 20, 30]

        start_time = time.time()
        multiple_knapsack(values, weights, capacities)
        end_time = time.time()

        execution_time = end_time
        execution_times.append(execution_time)

    plt.plot(num_items_range, execution_times, marker='o')
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Time Complexity of Multiple Knapsack Algorithm")
    plt.grid()
    plt.show()
def main():
    time_complexity_increasing_number_of_files()
#    plot_time_complexity()
if __name__ == '__main__':
    main()
