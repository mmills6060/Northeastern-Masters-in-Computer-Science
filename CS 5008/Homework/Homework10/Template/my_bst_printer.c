/** 
 * Tree print functions. Use Lab-dfs-bfs-practice as a starting point.
 * You are free to use the solution code provided with that lab.
 * 
 * @author YOUR NAME
 * semester: YOUR SEMESTER
*/

#include "my_bst.h"
#include <stdio.h>
#include <string.h>



// functions copied from lab-dfs-bfs-practice

void print_single_node(Node *node)
{
    printf("%d ", node->data);
}

/** inOrder DFS print of the Tree*/
void printTreeInOrder(Node *root)
{
}

/** post order DFS print of the Tree */
void printTreePostOrder(Node *root)
{
}

/** pre order DFS print of the Tree*/
void printTreePreOrder(Node *root)
{
}

/** iterative breadth-first print of the tree*/
void printTreeBreadthFirst(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    Node *queue[1000];
    int front = 0, rear = 0;
    queue[rear] = root;
    rear++;
    while (front < rear)
    {
        Node *current = queue[front];
        front++;
        print_single_node(current);
        if (current->left != NULL)
        {
            queue[rear] = current->left;
            rear++;
        }
        if (current->right != NULL)
        {
            queue[rear] = current->right;
            rear++;
        }
    }
}

/**
 * Prints the tree based on the specified print_type.
 * One node with a *space* between each node. (you do not have to worry about the trailing space)
 * For example, if the tree is A->B, A->C, B->D, B->E, C->F, C->G are preorder output should be
 * A B D E C F G
 *
 * You should use separate functions for each print type.
 * The print types accepted are
 * - "inorder"
 * - "preorder"
 * - "postorder"
 * - "breadthfirst"
 * HINT: look at the main in the lab-dfs-bfs-practice
 * If an invalid print_type is provided, print an error message.
 */
void bst_print(BST *tree, char *print_type)
{

}
