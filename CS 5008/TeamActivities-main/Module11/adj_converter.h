#ifndef ADJ_CONVERTER_H
#define ADJ_CONVERTER_H

#include "adj_list.h"
#include "adj_matrix.h"


AdjMatrix *convert_list_to_matrix(AdjList *list);

AdjList *convert_matrix_to_list(AdjMatrix *matrix);


#endif

