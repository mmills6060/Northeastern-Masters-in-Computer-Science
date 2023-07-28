#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "search_file.h"
#include "list_all_cities.h"

char* find_shortest_path(const char* city1, const char* city2) {
    const char* filename = "cities_distances_large.txt";

    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return NULL;
    }

    char line[256]; // Assuming no line in the file exceeds 255 characters
    char* shortestPath = NULL;

    // Read each line from the file
    while (fgets(line, sizeof(line), file)) {
        char cityFromFile1[100];
        char cityFromFile2[100];
        int distance;

        // Use sscanf to parse the line and extract the city names and shortest path value
        if (sscanf(line, "%s %s %d", cityFromFile1, cityFromFile2, &distance) == 3) {
            if ((strcmp(cityFromFile1, city1) == 0 && strcmp(cityFromFile2, city2) == 0) ||
                (strcmp(cityFromFile1, city2) == 0 && strcmp(cityFromFile2, city1) == 0)) {
                // Found the line with the cities, set the shortest path value
                shortestPath = malloc(10); // Allocate memory for the shortest path value
                snprintf(shortestPath, 10, "%d", distance);
                break;
            }
        }
    }

    fclose(file);

    // If shortestPath is still NULL, then the cities were not found in the file
    if (shortestPath == NULL) {
        printf("Cities '%s' and '%s' were not found in the file.\n", city1, city2);
    } else {
        printf("Shortest path between %s and %s: %s\n", city1, city2, shortestPath);
    }

    return shortestPath;
}