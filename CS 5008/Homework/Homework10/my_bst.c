/** Implementation of the BST data structure 
 * 
 * @author YOUR NAME
 * Semester YOUR SEMESTER
*/

#include "my_bst.h"
#include <stdlib.h>

/**
 * Checks to see if the tree is empty
 * by looking at the tree size.
 * returns true if the tree is empty.
 * False otherwise.
*/
bool bst_is_empty(BST *tree) {
    return tree->size == 0;
}

/**
 * Checks to see if the value exists in the tree.
 * returns true if the value exists in the tree.
 * False otherwise.
*/
bool bst_exists_helper(Node* node, int value) {
    if (node == NULL) {
        return false;
    }
    if (value < node->data) {
        return bst_exists_helper(node->left, value);
    } else if (value > node->data) {
        return bst_exists_helper(node->right, value);
    }
    return true;
}

bool bst_exists(BST* tree, int value) {
    if (tree == NULL) {
        return false;
    }
    return bst_exists_helper(tree->root, value);
}

/**
 * Returns the size of the tree.
*/
unsigned int bst_size(BST *tree) {
    return tree->size;
}

/**
 * Adds a value to the tree.
 * returns 1 if the value was added successfully.
 * returns 0 if the value already exists in the tree.
 * returns -1 if the value could not be added due to errors. (malloc failed)
*/
int bst_add(BST *tree, int value) {
    Node *new_node = (Node *) malloc(sizeof(Node));
    if (new_node == NULL) {
        return -1;
    }
    new_node->data = value;
    new_node->left = NULL;
    new_node->right = NULL;
    if (tree->root == NULL) {
        tree->root = new_node;
        tree->size++;
        return 1;
    }
    Node *current = tree->root;
    while (true) {
        if (current->data == value) {
            free(new_node);
            return 0;
        } else if (current->data > value) {
            if (current->left == NULL) {
                current->left = new_node;
                tree->size++;
                return 1;
            }
            current = current->left;
        } else {
            if (current->right == NULL) {
                current->right = new_node;
                tree->size++;
                return 1;
            }
            current = current->right;
        }
    }
}

/**
 * Frees the memory allocated for the tree.
 * hint: Think about which order works for traversal (pre, in, post) and how that
 * can help you free the memory
*/
void bst_free_helper(Node *node) {
    if (node == NULL) {
        return;
    }
    bst_free_helper(node->left);
    bst_free_helper(node->right);
    free(node);
}

void bst_free(BST *tree) {
    bst_free_helper(tree->root);
    free(tree);
}

/**
 * Creates a new BST.
 * returns a pointer to the new BST.
 * The root node will still be NULL until the first bst_add is called
*/
BST* create_bst() {
    BST* tree = (BST*)malloc(sizeof(BST));
    tree->root = NULL;
    return tree;
}
