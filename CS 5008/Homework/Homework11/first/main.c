#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "search_file.h"
#include "list_all_cities.h"

// Function to find the shortest path between two cities
// (You need to implement your shortest path algorithm here)
void findShortestPath(const char* city1, const char* city2) {
    // call the method in find_shortest_path.c 
    // to find the shortest path between city1 and city2
    char* shortestpath = find_shortest_path(city1, city2);
    if (shortestpath != NULL) {
        printf("Shortest path between %s and %s: %s\n", city1, city2, shortestpath);
        free(shortestpath); // Free the memory allocated for shortestpath
    } else {
        printf("No path found between %s and %s.\n", city1, city2);
    }
}

int main() {
    printf("*****Welcome to the shortest path finder!******\n");
    printf("Commands:\n");
    printf("\tlist - list all cities\n");
    printf("\t<city1> <city2> - find the shortest path between two cities\n");
    printf("\thelp - print this help message\n");
    printf("\texit - exit the program\n");
    printf("*******************************************************\n");

    char command[50];
    char city1[20];
    char city2[20];
    
    while (1) {
        printf("Where do you want to go today? what do i do? ");
        fgets(command, sizeof(command), stdin);
        printf("command: %s \n", command);
        if (strcmp(command, "list") == 0) {
            // List all cities from the file
            const char* filename = "cities_large.txt";
            const char* targetString = "<city name=\"";
            char* list = list_all_cities(filename, targetString);
            printf("%s", list);
            free(list);
        } else if (strcmp(command, "help") == 0) {
            // Print the help message again
            printf("Commands:\n");
            printf("\tlist - list all cities\n");
            printf("\t<city1> <city2> - find the shortest path between two cities\n");
            printf("\thelp - print this help message\n");
            printf("\texit - exit the program\n");
        } else if (strcmp(command, "exit") == 0) {
            // Exit the program
            printf("Exiting the program...\n");
            break;
        } else {
            // Assume the user entered two city names
            printf("command: %s \n", command);
            sscanf(command, "%s %s", city1, city2);
            printf("city 1: %s \n", city1);
            printf("city 2: %s \n", city2);
            findShortestPath(city1, city2);
        }
    }

    return 0;
}
