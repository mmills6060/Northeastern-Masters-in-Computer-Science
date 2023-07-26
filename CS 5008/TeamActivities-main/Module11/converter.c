#include "adj_converter.h"

AdjMatrix * convert_list_to_matrix(AdjList * list) {
    AdjMatrix * matrix = blank_matrix(list->size);
    
    // STUDENT TODO 
  int size = list->size;
  AdjMatrix *matrix = blank_matrix(size);

  for (int i = 0; i < size; i++) {
    AdjListNode *node = list->nodes[i];
    while (node) {
      matrix->data[i][node->vertex] = 1;
      node = node->next;
    }
  }
    return matrix;
}

AdjList * convert_matrix_to_list(AdjMatrix * matrix) {
    AdjList * list = create_graph(matrix->size);
    
    // STUDENT TODO
    
    return list;
}