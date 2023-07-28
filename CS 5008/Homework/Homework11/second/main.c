#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "search_file.h"
#include "list_all_cities.h"


// Define a structure for the graph vertices
typedef struct {
    char name[100];
} Vertex;

// Define a structure for the graph edges
typedef struct {
    int distance;
    int sourceIndex; // Index of the source vertex in the vertices array
    int destIndex;   // Index of the destination vertex in the vertices array
} Edge;
// Function to read data from the file and create a list of vertices and edges
void readGraphData(const char* filename, Vertex** vertices, int* numVertices, Edge** edges, int* numEdges) {
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening the file.\n");
        return;
    }

    // Count the number of vertices and edges in the file
    *numVertices = 0;
    *numEdges = 0;
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        (*numEdges)++;
        if (strstr(line, "\n"))
            (*numVertices)++;
    }
    (*numVertices)++; // Account for the last vertex that does not have an edge on the same line

    // Allocate memory for the vertices and edges arrays
    *vertices = (Vertex*)malloc((*numVertices) * sizeof(Vertex));
    *edges = (Edge*)malloc((*numEdges) * sizeof(Edge));

    // Reset file pointer to the beginning of the file
    fseek(file, 0, SEEK_SET);

    // Read data from the file and store it in the vertices and edges arrays
    int vertexIndex = 0;
    int edgeIndex = 0;
    while (fgets(line, sizeof(line), file)) {
        char source[100];
        char destination[100];
        int distance;

        sscanf(line, "%s %s %d", source, destination, &distance);

        // Add source vertex to the vertices array
        strcpy((*vertices)[vertexIndex].name, source);
        vertexIndex++;

        // Add edge to the edges array
        (*edges)[edgeIndex].sourceIndex = vertexIndex - 1;
        for (int i = 0; i < vertexIndex - 1; i++) {
            if (strcmp((*vertices)[i].name, source) == 0) {
                (*edges)[edgeIndex].sourceIndex = i;
                break;
            }
        }
        for (int i = 0; i < vertexIndex; i++) {
            if (strcmp((*vertices)[i].name, destination) == 0) {
                (*edges)[edgeIndex].destIndex = i;
                break;
            }
        }
        (*edges)[edgeIndex].distance = distance;
        edgeIndex++;
    }

    fclose(file);
}
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
                const char* filename = "cities_distances_large.txt";
    Vertex* vertices;
    int numVertices;
    Edge* edges;
    int numEdges;

    // Read data from the file and create the list of vertices and edges
    readGraphData(filename, &vertices, &numVertices, &edges, &numEdges);

    // Create and initialize the adjacency matrix
    int** adjacencyMatrix = (int**)malloc(numVertices * sizeof(int*));
    for (int i = 0; i < numVertices; i++) {
        adjacencyMatrix[i] = (int*)calloc(numVertices, sizeof(int));
    }

    // Populate the adjacency matrix based on the edges' distances
    for (int i = 0; i < numEdges; i++) {
        int sourceIndex = edges[i].sourceIndex;
        int destIndex = edges[i].destIndex;
        int distance = edges[i].distance;

        adjacencyMatrix[sourceIndex][destIndex] = distance;
        adjacencyMatrix[destIndex][sourceIndex] = distance; // Since it's an undirected graph
    }

    // Print the adjacency matrix (for demonstration purposes)
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            printf("%d ", adjacencyMatrix[i][j]);
        }
        printf("\n");
    }

    // Free dynamically allocated memory
    for (int i = 0; i < numVertices; i++) {
        free(adjacencyMatrix[i]);
    }
    free(adjacencyMatrix);
    free(vertices);
    free(edges);

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
