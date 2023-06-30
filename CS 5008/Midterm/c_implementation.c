#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Fibonacci {
    int* fibonacciSeries;
    int length;
} Fibonacci;

int fibonacciRecursiveHelper(int n); // Forward declaration to get rid of the warning

Fibonacci fibonacciIterative(int n) {
    if (n <= 0) {
        Fibonacci result;
        result.fibonacciSeries = NULL;
        result.length = 0;
        return result;
    }

    int* series = (int*)malloc(n * sizeof(int));
    int prev = 0, curr = 1;
    for (int i = 0; i < n; i++) {
        series[i] = curr;
        int temp = curr;
        curr += prev;
        prev = temp;
    }

    Fibonacci result;
    result.fibonacciSeries = series;
    result.length = n;
    return result;
}

Fibonacci fibonacciRecursive(int n) {
    if (n <= 0) {
        Fibonacci result;
        result.fibonacciSeries = NULL;
        result.length = 0;
        return result;
    }

    int* series = (int*)malloc(n * sizeof(int));
    for (int i = 1; i <= n; i++) {
        series[i - 1] = fibonacciRecursiveHelper(i);
    }

    Fibonacci result;
    result.fibonacciSeries = series;
    result.length = n;
    return result;
}

int fibonacciRecursiveHelper(int n) {
    if (n == 1 || n == 2)
        return 1;

    return fibonacciRecursiveHelper(n - 1) + fibonacciRecursiveHelper(n - 2);
}

Fibonacci fibonacciDynamic(int n) {
    if (n <= 0) {
        Fibonacci result;
        result.fibonacciSeries = NULL;
        result.length = 0;
        return result;
    }

    int* series = (int*)malloc(n * sizeof(int));
    series[0] = 1;
    series[1] = 1;

    for (int i = 2; i < n; i++) {
        series[i] = series[i - 1] + series[i - 2];
    }

    Fibonacci result;
    result.fibonacciSeries = series;
    result.length = n;
    return result;
}

void printFibonacciSeries(Fibonacci fibonacci) {
    printf("Fibonacci series:\n");
    for (int i = 0; i < fibonacci.length; i++) {
        printf("%d ", fibonacci.fibonacciSeries[i]);
    }
    printf("\n");
}

void printElapsedTime(clock_t start, clock_t end, FILE* file) {
    double elapsedSeconds = ((double)(end - start)) / CLOCKS_PER_SEC;
    fprintf(file, "%.10f\n", elapsedSeconds);
}

void destroyFibonacciSeries(Fibonacci fibonacci) {
    free(fibonacci.fibonacciSeries);
}

int main() {
    int choice = 2; // Set the default choice to Fibonacci Recursive

    FILE* file = fopen("C:\\Users\\mmill\\Github Repositories\\Northeastern-Masters-in-Computer-Science\\fibonacci_data.csv", "w");
    if (file == NULL) {
        printf("Failed to open the file.\n");
        return 1;
    }

    fprintf(file, "n,Elapsed Time\n");

    for (int n = 1; n <= 30; n++) {
        Fibonacci result;
        clock_t start, end;

        switch (choice) {
            case 1:
                start = clock();
                result = fibonacciIterative(n);
                end = clock();
                break;
            case 2:
                start = clock();
                result = fibonacciRecursive(n);
                end = clock();
                break;
            case 3:
                start = clock();
                result = fibonacciDynamic(n);
                end = clock();
                break;
            default:
                printf("Invalid choice.\n");
                return 1;
        }
        printElapsedTime(start, end, file);
        destroyFibonacciSeries(result);

        printf("\n");
    }

    fclose(file);
    return 0;
}
