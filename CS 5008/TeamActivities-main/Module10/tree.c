#include "tree.h"
#include <stdio.h>

/** create a node with a string. Will copy the
 * string into the node so the original can be freed.
 */
Node *createNode(char *data)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->left = NULL;
    newNode->right = NULL;
    newNode->data = (char *)malloc(strlen(data) + 1);
    strcpy(newNode->data, data);
    return newNode;
}

/** add a node to the tree
 * Finds the first open left most spot, so can create a skewed tree if not careful
 */
void addNode(Node *root, char *data)
{

    // adding a check could change which direction we add based on the data info..
    // this will help if we wanted a proper binary search tree


    if (root->left == NULL)
    {
        root->left = createNode(data);
    }
    else if (root->right == NULL)
    {
        root->right = createNode(data);
    }
    else
    {
        addNode(root->left, data);
    }
}



/** add a node to tree in a breadth-first manner
 * for breadth-first addition, it a queue is needed to keep track of locations
 */
void addNodeBreadthFirst(Node *root, char *data)
{
    struct Node *queue[1000];
    int front = 0, rear = 0;

    // Enqueue the root node (if it exists) to start the traversal
    if (root != NULL)
        queue[rear++] = root;

    // Traverse the tree in a breadth-first manner
    while (front < rear)
    {
        // Dequeue the next node and check if it has any empty children
        struct Node *node = queue[front++];
        if (node->left == NULL)
        {
            node->left = createNode(data);
            return;
        }
        if (node->right == NULL)
        {
            node->right = createNode(data);
            return;
        }

        // Enqueue its non-empty children (if any) to continue the traversal
        if (node->left != NULL)
            queue[rear++] = node->left;
        if (node->right != NULL)
            queue[rear++] = node->right;
    }
}

/** read a file, and store elements into the tree as they are read*/
Node *read_file_into_tree(char *filename)
{
    Node *root = NULL;
    FILE *fp = fopen(filename, "r");
    char line[256];
    while (fgets(line, sizeof(line), fp))
    {
        int len = strlen(line);
        if (line[len - 1] == '\n')
        {
            line[len - 1] = '\0'; // Replace the newline with null character
        }

        // if root is null, create a root node
        if (root == NULL)
        {
            root = createNode(line);
        }
        else
        {
            addNodeBreadthFirst(root, line);
        }
    }
    fclose(fp);
    return root;
}