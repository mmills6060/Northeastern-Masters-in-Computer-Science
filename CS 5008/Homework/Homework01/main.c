/**
 * Student Name:
 * Semester:
 * 
 * 
 * This is a sample program that you can use to test your c setup/config.
 * You will notice there are some logic errors in the code, you will need to fix them
 * for you submission. 
 * 
 * The code will compile without changes! Though if you are properly using the -Wall 
 * flag, you will see warnings.
 * is a long comment format that can span multiple lines
*/
// is  a single line comment

#include <stdio.h>  // This is a preprocessor directive, it tells the compiler to include the stdio.h header file
#include <stdlib.h> // This is a preprocessor directive, it tells the compiler to include the stdlib.h header file
#include <stdbool.h> // This is a preprocessor directive, it tells the compiler to include the stdbool.h header file

// the stdio.h header file contains the printf function, along with other input/output functions
// the stdlib.h header files contains functions for memory management, process control, conversions, random numbers, and others


/**
 * This function gets an int number. No error checking happens.
 * Header comments like these are expected for functions you write. 
*/
int get_number() // This is a function that returns an int
{
    int number; // This is a local variable, it is only available within this function
    printf("Please enter a number: "); // This is a function call, it calls the printf function
    scanf("%d", &number); // This is a function call, it calls the scanf function, which reads from the command line,
                          // and stores the value in the number variable
    return number; 
}

/**
 * Gets the clients name from the command line, returning a string allocated to the heap. 
*/
char* get_name() // This is a function that returns a pointer to a char array
{
    char* name = (char*) malloc(sizeof(char) * 20); // allocating space for a character array
    printf("Please enter your name: "); // This is a function call, it calls the printf function
    scanf("%s", name); // This is a function call, it calls the scanf function, which reads from the command line,
                      // and stores the value in the name variable
    return name; // This is a return statement, it returns the value of the name variable, which is a char array
}

/** 
 * main entry point of the program
*/
int main(int argc, char const *argv[])
{   
    char* name = get_name(); // This is a function call, it calls the get_name function, and stores the return value in the name variable
    int number = get_number(); // This is a function call, it calls the get_number function, and stores the return value in the number variable

    printf("Hello %s\n", name); // This is a function call, it calls the printf function, which prints the name variable to the command line

    if(number >= 21) { // C uses the basic conditions of >=, >, <=, <, ==, != (not equal to). For logical operators it uses && (and), || (or), ! (not)
        printf("You are old enough to drink in the US\n"); // This is a function call, it calls the printf function, it needs double quoted strings
    } else {
        printf("You are not old enough to drink in the US\n"); // This is a function call, it calls the printf function
    }


    free(name); // This frees the memory of the name variable, which was allocated in the get_name function
    
    
    return 0;
}

