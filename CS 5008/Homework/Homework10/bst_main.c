/**
 * Use this file to add your own tests and run a mini BST program.
 *
 * Things to test for...
 *
 * Fill a Binary Search Tree with values 1-100 and searching for nodes
 * Add 100 nodes and then check that the size is 100
 * Add 100 nodes with the value starting at 0 to 99, then check the sum of the tree to be 4950
 * etc...
 * (don't forget to check what happens in the null cases such as trying to find nodes that don't exist,
 * or any action on an empty tree...)
*/

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include "my_bst.h"

// a helper to get a range  of numbers
int *get_range_array(int start, int end) {
    int *arr = (int*) malloc(sizeof(int) * (end - start));
    int j = 0;
    for (int i = start; i < end; i++, j++) arr[j] = i;
    return arr;
}

// sample helper function to help you create random int arrays
int *get_random_array(int size) {
    int *arr = (int *)malloc(sizeof(int) * size);
    srand(time(NULL)); // seed the random number generator

    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 100;
    }

    return arr;
}

int main() {
    BST* tree = create_bst();

    // Fill a Binary Search Tree with values 1-100
    for (int i = 1; i <= 100; i++) {
        bst_add(tree, i);
    }

    // Searching for nodes
    if (bst_exists(tree, 50)) {
        printf("Node 50 exists in the tree.\n");
    } else {
        printf("Node 50 does not exist in the tree.\n");
    }

    if (bst_exists(tree, 101)) {
        printf("Node 101 exists in the tree.\n");
    } else {
        printf("Node 101 does not exist in the tree.\n");
    }

    // Check the size of the tree
    printf("Size of the tree: %u\n", bst_size(tree));

    // Add 100 nodes and then check that the size is 100
    for (int i = 101; i <= 200; i++) {
        bst_add(tree, i);
    }
    printf("Size of the tree: %u\n", bst_size(tree));

    // Add 100 nodes with the value starting at 0 to 99, then check the sum of the tree
    int* arr = get_range_array(0, 100);
    for (int i = 0; i < 100; i++) {
        bst_add(tree, arr[i]);
    }
    printf("Sum of the tree: %d\n");

    // Print the tree using different traversal orders
    printf("Inorder traversal: ");
    bst_print(tree, "inorder");

    printf("Preorder traversal: ");
    bst_print(tree, "preorder");

    printf("Postorder traversal: ");
    bst_print(tree, "postorder");

    printf("Breadth-first traversal: ");
    bst_print(tree, "breadthfirst");

    // Free the memory allocated for the tree and array
    bst_free(tree);
    free(arr);

    return 0;
}