/// to compile: clang -Wall tester.c -o tester.out

#include <stdio.h>  // Include file for standard input/output
#include <stdlib.h> // so we can use atoi()
#include <time.h>   // so we can use time_t and clock_gettime()

#include "sorts.h"

// these are called function pointers
void (*sorts[])(int *, unsigned int, int) = {
    bubbleSortIntegers,
    quickSortIntegers
};

int* get_random_array(int size) {
    // Allocate memory
    int *random = (int *)malloc(sizeof(int) * size);

    // Populate our test data set
    for (int i = 0; i < size; i++)
    {
        // Generate random values from 0 to 99
        random[i] = rand() % size;
    }
    return random;
}


double sort_and_time(int* array, int size, int type, int print) {
    // Setup timers
    struct timespec begin, end;
    // Get the time before we start
    clock_gettime(CLOCK_MONOTONIC_RAW, &begin);
    // Perform the sort
    sorts[type](array, size, print);
    // Get the time after we are done
    clock_gettime(CLOCK_MONOTONIC_RAW, &end);

    return (end.tv_nsec - begin.tv_nsec) / 1000000000.0 +
                        (end.tv_sec - begin.tv_sec);
}


int main(int argc, char const *argv[])
{
    if (!(argc > 2 && argc < 5))
    {
        printf("Two arguments expected, [sort_type] and random size. Add 1 at the end to print out arrays\n");
        printf("[sort_type] 0 == bubble, 1 == quick\n");
        printf("Random size determines the total size of the the random array of numbers to be sorted\n");
        printf("\n");
        printf("Example: ./tester.out 0 1000");
        return 1;
    }

    //get teh type of sort
    const int type = atoi(argv[1]);
    if(type > 3) {
        printf("invalid type");
        return 1;
    }



    // Convert the argument of the program into an integer
    const int size = atoi(argv[2]);

    int print = 0;
    if (argc == 4) {
        print = 1;
    }

    // Generate a random seed
    time_t t;
    srand((unsigned)time(&t));

    int* random = get_random_array(size);

    
    if(print) {
        printf("Before the sort: ");
        printIntArray(random, size);
    }

    double time_taken = sort_and_time(random, size, type, print);

    // Confirm the sort worked
    if (print)
    {
        printf("After the sort : ");
        printIntArray(random, size);
    }

    printf("Total time = %f seconds\n", time_taken);

    
    // Free our random array
    free(random);
    return 0;
}
