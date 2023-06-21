#ifndef TREE_H
#define TREE_H
/**
 * Simple tree implementation that adds nodes based on the most
 * recent empty location.
**/


#include <stdlib.h>
#include <string.h>

/** simple tree structure using string data */
typedef struct Node {
    char* data;
    struct Node* left;
    struct Node* right;
} Node;

Node *read_file_into_tree(char *filename); // this is the only function we are exposing to the 'outside world'

#endif