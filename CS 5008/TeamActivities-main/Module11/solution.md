# Solution

The following is a solution to convert between the two. Make sure you understand how it works. 

Think about the memory and space trade off for each solution! 


```c
AdjMatrix * convert_list_to_matrix(AdjList * list) {
    AdjMatrix * matrix = blank_matrix(list->size);
    for (int i = 0; i < matrix->size; i++) {
        for (int j = 0; j < matrix->size; j++) {
            matrix->data[i][j] = 0;
        }
    }
    for (int i = 0; i < list->size; i++) {
        edge_t *edge = list->adj_lists[i];
        while (edge != NULL) {
            matrix->data[i][edge->vertex] = edge->weight;
            edge = edge->next;
        }
    }
    return matrix;
}

AdjList * convert_matrix_to_list(AdjMatrix * matrix) {
    AdjList * list = create_graph(matrix->size);
    
    for (int i = 0; i < matrix->size; i++) {
        for (int j = 0; j < matrix->size; j++) {
            if (matrix->data[i][j] > 0) {
                add_edge(list, i, j, matrix->data[i][j]);
            }
        }
    }
    return list;
}
```