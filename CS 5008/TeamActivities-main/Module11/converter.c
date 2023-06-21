#include "adj_converter.h"

AdjMatrix * convert_list_to_matrix(AdjList * list) {
    AdjMatrix * matrix = blank_matrix(list->size);
    
    // STUDENT TODO 

    return matrix;
}

AdjList * convert_matrix_to_list(AdjMatrix * matrix) {
    AdjList * list = create_graph(matrix->size);
    
    // STUDENT TODO
    
    return list;
}