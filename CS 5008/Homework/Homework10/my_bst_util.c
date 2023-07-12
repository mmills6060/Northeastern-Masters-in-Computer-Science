/** Implementation of BST utility functions
 *
 *  @author YOUR NAME
 * Semester YOUR SEMESTER
 *
*/


#include "my_bst.h"
#include "my_bst_util.h"
/**
 * Returns the sum of all the values in the tree.
*/



int sum_helper(Node* node) {
    if (node == NULL) {
        return 0;
    }
    return node->data + sum_helper(node->left) + sum_helper(node->right);
}

int sum(BST* tree) {
    return sum_helper(tree->root);
}

int min_helper(Node* node) {
    if (node == NULL) {
        return -1; // Or any other appropriate value for an empty tree
    }
    while (node->left != NULL) {
        node = node->left;
    }
    return node->data;
}

int min(BST* tree) {
    return min_helper(tree->root);
}

int max_helper(Node* node) {
    if (node == NULL) {
        return -1; // Or any other appropriate value for an empty tree
    }
    while (node->right != NULL) {
        node = node->right;
    }
    return node->data;
}

int max(BST* tree) {
    return max_helper(tree->root);
}

