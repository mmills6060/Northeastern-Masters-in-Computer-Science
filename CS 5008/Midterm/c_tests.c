#include <stdio.h>
#include "c_implementation.c"

void test_fibonacci_iterative() {
    int n = 10;
    int series[10] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    printf("Testing Fibonacci Iterative...\n");

    for (int i = 0; i < n; i++) {
        Fibonacci result = fibonacciIterative(i + 1);
        if (result.fibonacciSeries[i] != series[i]) {
            printf("Test failed for index %d\n", i + 1);
        } else {
            printf("Test passed for index %d\n", i + 1);
        }
        destroyFibonacciSeries(result);
    }

    printf("Fibonacci Iterative test completed.\n");
}

void test_fibonacci_recursive() {
    int n = 10;
    int series[10] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    printf("Testing Fibonacci Recursive...\n");

    for (int i = 0; i < n; i++) {
        Fibonacci result = fibonacciRecursive(i + 1);
        if (result.fibonacciSeries[i] != series[i]) {
            printf("Test failed for index %d\n", i + 1);
        } else {
            printf("Test passed for index %d\n", i + 1);
        }
        destroyFibonacciSeries(result);
    }

    printf("Fibonacci Recursive test completed.\n");
}

void test_fibonacci_dynamic() {
    int n = 10;
    int series[10] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    printf("Testing Fibonacci Dynamic...\n");

    for (int i = 0; i < n; i++) {
        Fibonacci result = fibonacciDynamic(i + 1);
        if (result.fibonacciSeries[i] != series[i]) {
            printf("Test failed for index %d\n", i + 1);
        } else {
            printf("Test passed for index %d\n", i + 1);
        }
        destroyFibonacciSeries(result);
    }

    printf("Fibonacci Dynamic test completed.\n");
}

int main() {
    test_fibonacci_iterative();
    test_fibonacci_recursive();
    test_fibonacci_dynamic();

    return 0;
}
