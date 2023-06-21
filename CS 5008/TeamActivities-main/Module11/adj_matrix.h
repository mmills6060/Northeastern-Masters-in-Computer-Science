#ifndef ADJ_MATRIX_H
#define ADJ_MATRIX_H

#include <stdio.h>
#include <stdlib.h>


typedef struct {
    int **data;
    int size;
} AdjMatrix;

AdjMatrix *blank_matrix(int size);
void free_matrix(AdjMatrix *matrix);
void print_matrix(AdjMatrix *matrix);

#endif