/**
 * Contains information for a Binary Search Tree (BST) data structure.
 * @author YOUR NAME
 * Semester YOUR SEMESTER
*/
#ifndef MYBST_H 
#define MYBST_H

#include <stdbool.h>
#include <stdlib.h>

// use these for print_type in bst_print
#define INORDER "inorder"
#define PREORDER "preorder"
#define POSTORDER "postorder"
#define BREADTHFIRST "breadthfirst"

// Create a node data struct to store data within
// our BST. In our case, we will stores 'integers'
typedef struct Node
{
    int data;                    // data each node holds
    struct Node *left;  // pointer to left child (if any)
    struct Node *right; // pointer to right child (if any)
} Node;

// Our Binary Search Tree data structure
// Our BST holds a pointer to the root node in our BST.
// This helps protect the root node from accidentally loosing children
typedef struct tree
{
    unsigned int size;  // Size keeps track of how many items are in the BST.
                        // Size should be incremented when we add.
    Node *root; //root node in our BST.
} BST;


// the following should be implemented in my_bst.c 
// they deal with the structure of the tree
bool bst_is_empty(BST *tree);
unsigned int bst_size(BST *tree);
bool bst_exists(BST *tree, int value);
int bst_add(BST *tree, int value);
void bst_free(BST *tree);
BST * create_bst(); 

// implemented in my_bst_printer.c - deals with the 'view' of the tree
void bst_print(BST *tree, char* print_type); 




#endif
