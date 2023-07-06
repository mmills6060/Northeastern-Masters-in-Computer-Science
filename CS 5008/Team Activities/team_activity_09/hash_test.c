
#include <stdio.h>
#include <string.h>
#include "hashing.h"

#define ALGO_SIZE 4 /* make sure to change this if you add hash algos to hash[]*/
#define SIZE 1000000 /* change this around to mess with load / array size - we suggest 1 and other sizes */



/** this is a way that we can
 * cycle through the algorithms.
*/
uint32_t (*hash[])(char*) = {
    simple_hash,
    djb2,
    fnv_hash,
    jenkins_one_at_a_time_hash
    
    };


void printArray(int * array, int size) {

    for(int i = 0; i < size; i++) printf("%d ", array[i]);
    printf("\n");
}

void printCollisionsOnly(int *array, int size)
{
    int total = 0;
    int highest  = 0;
    int counter = 0;
    int length = 0;
    for (int i = 0; i < size; i++) {
        if(array[i] > 1) { 
            total += array[i]; // really looking at total chain length > 1
            length++;
            if(array[i] > highest) highest = array[i];
        }
        if(array[i] > 0) {
            counter++;
        }
    }
    printf("Collisions: %d, Highest: %d, Average Length > 1: %.2f, Filled Spots: %d, Load: %.5f\n", total, highest, 
           total / (float)length, counter, counter / (float)SIZE);
}

int main(int argc, char** argv) {

    int *collisions[ALGO_SIZE]; 
    if (argc < 2)
    {
        printf("Requires at least one file as an argument");
        return 1;
    }

    char buffer[256];
    FILE *fp;
    
    for(int filec = 1; filec < argc; filec++ ) {
        
        for (int i = 0; i < ALGO_SIZE; i++)
        {
            collisions[i] = (int*) malloc(sizeof(int)*SIZE);
            memset(collisions[i], 0, SIZE); // quickly sets everything to 0
        }

        fp = fopen(argv[filec], "r");
        if (fp == NULL)
        {
            printf("Error opening file\n");
            return 1;
        }

        printf("%s...\n", argv[filec]);
        while (fgets(buffer, sizeof(buffer), fp))
        {
            for (int i = 0; i < ALGO_SIZE; i++)
            {
                uint32_t loc = (hash[i](buffer)) % SIZE;
                collisions[i][loc]++;
            }
        }

        fclose(fp);
        for (int i = 0; i < ALGO_SIZE; i++)
        {
            printCollisionsOnly(collisions[i], SIZE);
            //printArray(collisions[i], SIZE);
        
            free(collisions[i]); // free dynamically allocated arrays.
        }
        printf("\n"); // add extra space
        }
    return 0;
}