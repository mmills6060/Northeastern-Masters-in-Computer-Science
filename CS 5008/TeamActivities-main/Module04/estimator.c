#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

#define BUFF_SIZE 100
#define ADD_CYCLES 1
#define MOV_CYCLES 1
#define PUSH_CYCLES 1
#define POP_CYCLES 1
#define LEA_CYCLES 3
#define MUL_CYCLES 3
#define DIV_CYCLES 24
#define SUB_CYCLES 1
#define RET_CYCLES 1
#define SHL_CYCLES 1
#define SAR_CYCLES 1

// All the instructions as strings for easier finding
char instructions[][5] = {"ADD", "MOV", "PUSH", "POP", "LEA", "MUL", "DIV", "SUB", "RET", "SHL", "SAR"};


/**
 * Converts a string to upper case. 
*/
void convertToUpperCase(char *str)
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        str[i] = toupper(str[i]); // to upper is from ctype
    }
}


/**
 * Looks for a substring in a string. 
*/
bool contains(char *str, char *substr)
{
    if (strstr(str, substr) != NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}


/**
 * Prints the info for each instruction.
*/
void print_info(int* counts) {
    printf("Total ADD Instructions: %d and Cost: %d \n", counts[0], counts[0] * ADD_CYCLES);
    printf("Total MOV Instructions: %d and Cost: %d \n", counts[1], counts[1] * MOV_CYCLES);
    printf("Total PUSH Instructions: %d and Cost: %d \n", counts[2], counts[2] * PUSH_CYCLES);
    printf("Total POP Instructions: %d and Cost: %d \n", counts[3], counts[3] * POP_CYCLES);
    printf("Total LEA Instructions: %d and Cost: %d \n", counts[4], counts[4] * LEA_CYCLES);
    printf("Total MUL Instructions: %d and Cost: %d \n", counts[5], counts[5] * MUL_CYCLES);
    printf("Total DIV Instructions: %d and Cost: %d \n", counts[6], counts[6] * DIV_CYCLES);
    printf("Total SUB Instructions: %d and Cost: %d \n", counts[7], counts[7] * SUB_CYCLES);
    printf("Total RET Instructions: %d and Cost: %d \n", counts[8], counts[8] * RET_CYCLES);
    printf("Total SHL Instructions: %d and Cost: %d \n", counts[9], counts[9] * SHL_CYCLES);
    printf("Total SAR Instructions: %d and Cost: %d \n", counts[10], counts[10] * SAR_CYCLES);
}

/**
 * Runs the program by reading in a file with the name file_name,
 * and then looping through every line of the file. For each line,
 * it will check if it contains any of the instructions (which is another loop, that goes
 * through instructions calling contains for each instruction), and if it does,
 * it will increment the count for that instruction (using contains).
 * 
 *  Since contains is case sensitive, we convert the line to upper case using convertToUpperCase.
 * 
 * Finally, we print the info for each instruction using print_info.
*/
void run_program(char* file_name) {
     // student TODO

}


/**
 * Main entry point, requires a file name to run
*/
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <file_name>\n", argv[0]);
        exit(1);
    }
    run_program(argv[1]);

    return 0;
}