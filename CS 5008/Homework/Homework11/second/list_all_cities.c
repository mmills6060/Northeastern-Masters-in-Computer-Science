#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "search_file.h"
#include "list_all_cities.h"

char* list_all_cities(const char* filename, const char* targetString) {
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error opening the file.\n");
        return NULL;
    }

    char line[256]; // Assuming no line in the file exceeds 255 characters
    char* list = NULL;
    int listSize = 0;

    // for each line that exists in the file, print the line in the terminal separated by a new line

    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
        // Check if the last character of the line is a newline character
        int lineLength = strlen(line);
        if (lineLength > 0 && line[lineLength - 1] != '\n') {
            // Incomplete line, read the rest of the line and concatenate
            char restOfLine[256];
            while (fgets(restOfLine, sizeof(restOfLine), file)) {
                int restLength = strlen(restOfLine);
                if (restLength > 0 && restOfLine[restLength - 1] == '\n') {
                    restOfLine[restLength - 1] = '\0'; // Remove the trailing newline
                    strcat(line, restOfLine);
                    break;
                } else {
                    strcat(line, restOfLine);
                }
            }
        }

        // append the value on the current line to list
        const char* startTag = "<city name=\"";
        char* cityStart = strstr(line, startTag);
        if (cityStart != NULL) {
            cityStart += strlen(startTag); // Move the pointer to the beginning of the city name
            char* cityEnd = strchr(cityStart, '\"'); // Find the closing quote of the city name
            if (cityEnd != NULL) {
                int cityLength = cityEnd - cityStart;
                // Allocate memory for the new city name (+1 for null terminator)
                char* cityName = malloc((cityLength + 1) * sizeof(char));
                strncpy(cityName, cityStart, cityLength);
                cityName[cityLength] = '\0'; // Add the null terminator

                // If the list is empty, allocate memory for it and initialize it with an empty string
                if (list == NULL) {
                    list = malloc(1); // One byte for the null terminator
                    *list = '\0'; // Initialize the list as an empty string
                }

                // Resize the list to accommodate the new city name (+1 for separating newline)
                list = realloc(list, (listSize + cityLength + 1 + 1) * sizeof(char));

                // Append the city name and a newline to the list
                strcat(list, cityName);
                strcat(list, "\n");

                // Update the list size
                listSize += cityLength + 1;
                
                free(cityName);
            }
        }
    }

    fclose(file);
    return list;
}
