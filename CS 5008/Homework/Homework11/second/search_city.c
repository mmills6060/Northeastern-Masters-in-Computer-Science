#include <stdio.h>
#include <string.h>
#include "search_file.h"

int searchStringInFile(const char* filename, const char* targetString) {
    FILE* file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 0;
    }

    char line[256]; // Assuming no line in the file exceeds 255 characters
    int found = 0;

    while (fgets(line, sizeof(line), file)) {
        if (strstr(line, targetString) != NULL) {
            found = 1;
            break;
        }
    }

    fclose(file);
    return found;
}