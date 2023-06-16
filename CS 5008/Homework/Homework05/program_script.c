#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Define the input parameters
    int iterations[] = {10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    int algorithms[] = {0, 1, 2, 3, 4}; // 0: Selection Sort, 1: Insertion Sort, 2: Bubble Sort, 3: Merge Sort

    // Compile tester.c
    system("gcc tester.c -o tester");

    // Iterate over the algorithms
    for (int i = 0; i < sizeof(algorithms) / sizeof(algorithms[0]); i++)
    {
        printf("Algorithm %d:\n", algorithms[i]);

        // Iterate over the iterations
        for (int j = 0; j < sizeof(iterations) / sizeof(iterations[0]); j++)
        {
            printf("Iterations: %d\n", iterations[j]);

            // Call the tester program
            char command[100];
            sprintf(command, "./tester %d %d", algorithms[i], iterations[j]);
            system(command);
        }

        printf("==========================\n");
    }

    // Cleanup - remove the compiled executable
    system("rm tester");

    return 0;
}
