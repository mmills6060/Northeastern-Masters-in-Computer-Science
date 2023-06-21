
#include <time.h>
#include <stdlib.h>

#include "adj_converter.h"

#define DIRECTED_ONE_DIRECTION 0
#define DIRECTED_UNBALANCED 1
#define UNDIRECTED 2
#define MAX_DISTANCE 10




AdjMatrix * buildRandomMatrix(int size, int type) {
    srand(time(NULL));
    AdjMatrix * matrix = blank_matrix(size);

    for (int i = 0; i < matrix->size; i++) {
        for (int j = 0; j < matrix->size; j++) {
            if(i == j) continue; // skip self reference
            switch (type)
            {
            case DIRECTED_ONE_DIRECTION:
                if(i < j) matrix->data[i][j] = rand() % MAX_DISTANCE;
                else matrix->data[i][j] = 0; // no back edges 
                /* code */
                break;
            case DIRECTED_UNBALANCED:
                matrix->data[i][j] = rand() % MAX_DISTANCE;
                break;
            case UNDIRECTED:
                matrix->data[i][j] = rand() % MAX_DISTANCE;
                matrix->data[j][i] = matrix->data[i][j];
                break;
            default:
                fprintf(stderr, "Invalid type");
                return NULL;
            }

        }
    }
    return matrix;


}


int main(int argc, char** argv) {
 
    AdjMatrix * matrix = buildRandomMatrix(5, UNDIRECTED);

    print_matrix(matrix);

    AdjList * list = convert_matrix_to_list(matrix);
    print_graph(list);
    free_graph(list);

    free_matrix(matrix);
 return 0;
}