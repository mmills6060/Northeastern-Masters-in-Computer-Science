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
    fprintf(file, ",%.10f\n", elapsedSeconds);
}

void destroyFibonacciSeries(Fibonacci fibonacci) {
    free(fibonacci.fibonacciSeries);
}

// ./c_implementation {N} {type} {print type}
// type: 0 for recursive, 1 for iterative, 2 for dynamic
// print type: 0 for no print, 1 for print
int main(int argc, char* argv[])
{
    if (argc < 2) {
        printf("At least two arguments needed!\n");
        return 1;
    }

    const int n = atoi(argv[1]);
    int type = 0;
    int print = 0;

    if (argc > 2) {
        type = atoi(argv[2]);
    }

    if (argc > 3) {
        print = atoi(argv[3]);
    }

    Fibonacci result;

    if (type == 0) {
        result = fibonacciRecursive(n);
    }
    else if (type == 1) {
        result = fibonacciIterative(n);
    }
    else if (type == 2) {
        result = fibonacciDynamic(n);
    }
    else {
        printf("Invalid type argument!\n");
        return 1;
    }

    if (print == 1) {
        printFibonacciSeries(result);
    }

    destroyFibonacciSeries(result);

    return 0;
}
