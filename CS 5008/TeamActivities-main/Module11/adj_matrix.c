#include "adj_matrix.h"

AdjMatrix *blank_matrix(int size)
{
    AdjMatrix *matrix = (AdjMatrix *)malloc(sizeof(AdjMatrix));
    int **data = (int **)malloc(sizeof(int *) * size);

    for (int i = 0; i < size; i++)
    {
        data[i] = (int *)malloc(sizeof(int) * size);
        for (int j = 0; j < size; j++)
        {
            data[i][j] = 0;
        }
    }
    matrix->data = data;
    matrix->size = size;
    return matrix;
}

void free_matrix(AdjMatrix *matrix)
{
    for (int i = 0; i < matrix->size; i++)
        free(matrix->data[i]);
    free(matrix->data);
    free(matrix);
}

void print_matrix(AdjMatrix *matrix)
{
    printf("Adjacency Matrix:\n");
    for (int i = 0; i < matrix->size; i++)
    {
        for (int j = 0; j < matrix->size; j++)
        {
            printf("%d ", matrix->data[i][j]);
        }
        printf("\n");
    }
}