import subprocess
import csv

def generate_fibonacci_data():
    # Compile and run the C implementation
    subprocess.run(["gcc", "C:\\Users\\mmill\\Github Repositories\\Northeastern-Masters-in-Computer-Science\\CS 5008\\Midterm\\c_implementation.c", "-o", "c_implementation"])
    c_output = subprocess.run(["C:\\Users\\mmill\\Github Repositories\\Northeastern-Masters-in-Computer-Science\\CS 5008\\Midterm\\c_implementation"], capture_output=True, text=True).stdout

    # Run the Python implementation
    python_output = subprocess.run(["python", "python_implementation.py"], capture_output=True, text=True).stdout

    # Parse the output and extract the data
    c_data = []
    python_data = []
    for line in c_output.splitlines():
        if line.startswith("Fibonacci"):
            values = line.split(":")[1].strip().split()
            c_data.extend(map(int, values))
    for line in python_output.splitlines():
        if line.startswith("Fibonacci"):
            values = line.split(":")[1].strip().split()
            python_data.extend(map(int, values))

    # Generate the n values
    n_values = list(range(1, len(c_data) + 1))

    # Create a CSV file to store the data
    filename = "fibonacci_data.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["n", "Fibonacci Iterative (C)", "Fibonacci Recursive (Python)", "Fibonacci Dynamic (Python)"])
        writer.writerows(zip(n_values, c_data, python_data, python_data))

    print(f"Data saved to {filename}")

    # Return the data
    return n_values, c_data, python_data

# Call the function to generate the data
n_values, c_data, python_data = generate_fibonacci_data()
