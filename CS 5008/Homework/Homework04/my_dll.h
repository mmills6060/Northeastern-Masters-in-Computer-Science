// =================== Support Code =================
// Doubly Linked List ( DLL ).
//
//
//
// - Implement each of the functions to create a working DLL.
// - Do not change any of the function declarations
//   - (i.e. dll_t* create_dll() should not have additional arguments)
// - You should not have any 'printf' statements in your DLL functions.
//   - (You may consider using these printf statements to debug,
//     but they should be removed from your final version)
//   - (You may write helper functions to help you debug your code such as print_list etc)
// ==================================================
#ifndef MYDLL_H
#define MYDLL_H

#include <stdio.h>
#include <stdlib.h>

// Create a node data structure to store data within
// our DLL. In our case, we will stores 'integers'
typedef struct node
{
    int data;
    struct node *next;
    struct node *previous;
} node_t;

// Create a DLL data structure
// Our DLL holds a pointer to the first node in our DLL called head,
// and a pointer to the last node in our DLL called tail.
typedef struct DLL
{
    int count;    // count keeps track of how many items are in the DLL.
    node_t *head; // head points to the first node in our DLL.
    node_t *tail; // tail points to the last node in our DLL.
} dll_t;

// Creates a DLL
// Returns a pointer to a newly created DLL.
// The DLL should be initialized with data on the heap.
// (Think about what the means in terms of memory allocation)
// The DLLs fields should also be initialized to default values.
// Returns NULL if we could not allocate memory.
dll_t* create_dll() {
    dll_t* myDLL = (dll_t*)malloc(sizeof(dll_t));
    if (myDLL == NULL) {
        return NULL;  // Unable to allocate memory
    }

    myDLL->count = 0;
    myDLL->head = NULL;
    myDLL->tail = NULL;

    return myDLL;
}

// DLL Empty
// Check if the DLL is empty
// Returns -1 if the dll is NULL.
// Returns 1 if true (The DLL is completely empty)
// Returns 0 if false (the DLL has at least one element enqueued)
int dll_empty(dll_t* l) {
    if (l == NULL) {
        return -1;
    }

    if (l->count == 0) {
        return 1;   // DLL is empty
    }

    return 0;       // DLL is not empty
}
// Helper function to create a new node with the given data
node_t* create_node(int data) {
    node_t* newNode = (node_t*)malloc(sizeof(node_t));
    if (newNode == NULL) {
        return NULL;    // Unable to allocate memory
    }

    newNode->data = data;
    newNode->next = NULL;
    newNode->previous = NULL;

    return newNode;
}
// push a new item to the front of the DLL ( before the first node in the list).
// Returns -1 if DLL is NULL.
// Returns 1 on success
// Returns 0 on failure ( i.e. we couldn't allocate memory for the new node)
// (i.e. the memory allocation for a new node failed).
int dll_push_front(dll_t* l, int item) {
    if (l == NULL) {
        return -1;
    }

    node_t* newNode = create_node(item);
    if (newNode == NULL) {
        return 0;   // Unable to allocate memory for the new node
    }

    if (l->count == 0) {
        l->head = newNode;
        l->tail = newNode;
    } else {
        newNode->next = l->head;
        l->head->previous = newNode;
        l->head = newNode;
    }

    l->count++;

    return 1;
}

// push a new item to the end of the DLL (after the last node in the list).
// Returns -1 if DLL is NULL.
// Returns 1 on success
// Returns 0 on failure ( i.e. we couldn't allocate memory for the new node)
// (i.e. the memory allocation for a new node failed).
int dll_push_back(dll_t* l, int item) {
    if (l == NULL) {
        return -1;
    }

    node_t* newNode = create_node(item);
    if (newNode == NULL) {
        return 0;   // Unable to allocate memory for the new node
    }

    if (l->count == 0) {
        l->head = newNode;
        l->tail = newNode;
    } else {
        newNode->previous = l->tail;
        l->tail->next = newNode;
        l->tail = newNode;
    }

    l->count++;

    return 1;
}

// Returns the first item in the DLL and also removes it from the list.
// Returns -1 if the DLL is NULL.
// Returns 0 on failure, i.e. there is noting to pop from the list.
// Assume no negative numbers in the list or the number zero.
int dll_pop_front(dll_t* l) {
    if (l == NULL) {
        return -1;
    }

    if (l->count == 0) {
        return 0;   // DLL is empty, nothing to pop
    }

    node_t* firstNode = l->head;
    int data = firstNode->data;

    if (l->count == 1) {
        l->head = NULL;
        l->tail = NULL;
    } else {
        l->head = firstNode->next;
        l->head->previous = NULL;
    }

    free(firstNode);
    l->count--;

    return data;
}

// Returns the last item in the DLL, and also removes it from the list.
// Returns a -1 if the DLL is NULL.
// Returns 0 on failure, i.e. there is noting to pop from the list.
// Assume no negative numbers in the list or the number zero.
int dll_pop_back(dll_t* l) {
    if (l == NULL) {
        return -1;
    }

    if (l->count == 0) {
        return 0;   // DLL is empty, nothing to pop
    }

    node_t* lastNode = l->tail;
    int data = lastNode->data;

    if (l->count == 1) {
        l->head = NULL;
        l->tail = NULL;
    } else {
        l->tail = lastNode->previous;
        l->tail->next = NULL;
    }

    free(lastNode);
    l->count--;

    return data;
}

// Inserts a new node before the node at the specified position.
// Returns -1 if the list is NULL
// Returns 1 on success
// Retruns 0 on failure:
//  * we couldn't allocate memory for the new node
//  * we tried to insert at a negative location.
//  * we tried to insert past the size of the list
//   (inserting at the size should be equivalent as calling push_back).
int dll_insert(dll_t* l, int pos, int data) {
    if (l == NULL) {
        return -1;  // Invalid list
    }

    if (pos < 0 || pos > l->count) {
        return 0;  // Failure: Invalid position
    }

    node_t* newNode = (node_t*)malloc(sizeof(node_t));
    if (newNode == NULL) {
        return 0;  // Failure: Unable to allocate memory for new node
    }

    newNode->data = data;

    if (pos == 0) {
        newNode->next = l->head;
        newNode->previous = NULL;

        if (l->head != NULL) {
            l->head->previous = newNode;
        } else {
            l->tail = newNode;
        }

        l->head = newNode;
    } else if (pos == l->count) {
        newNode->next = NULL;
        newNode->previous = l->tail;

        l->tail->next = newNode;
        l->tail = newNode;
    } else {
        node_t* currentNode = l->head;
        for (int i = 0; i < pos; i++) {
            currentNode = currentNode->next;
        }

        newNode->next = currentNode;
        newNode->previous = currentNode->previous;

        currentNode->previous->next = newNode;
        currentNode->previous = newNode;
    }

    l->count++;

    return 1;  // Success
}

// Returns the item at position pos starting at 0 ( 0 being the first item )
// Returns -1 if the list is NULL
//  (does not remove the item)
// Returns 0 on failure:
//  * we tried to get at a negative location.
//  * we tried to get past the size of the list
// Assume no negative numbers in the list or the number zero.
int dll_get(dll_t* l, int pos) {
    if (l == NULL) {
        return -1;  // Invalid list
    }

    if (pos < 0 || pos >= l->count) {
        return 0;  // Failure: Invalid position
    }

    node_t* currentNode = l->head;
    for (int i = 0; i < pos; i++) {
        currentNode = currentNode->next;
    }

    return currentNode->data;
}

// Removes the item at position pos starting at 0 ( 0 being the first item )
// Returns -1 if the list is NULL
// Returns 0 on failure:
//  * we tried to remove at a negative location.
//  * we tried to remove get past the size of the list
// Assume no negative numbers in the list or the number zero.
// Otherwise returns the value of the node removed.
int dll_remove(dll_t* l, int pos) {
    if (l == NULL) {
        return -1;  // Invalid list
    }

    if (pos < 0 || pos >= l->count) {
        return 0;  // Failure: Invalid position
    }

    node_t* currentNode = l->head;
    for (int i = 0; i < pos; i++) {
        currentNode = currentNode->next;
    }

    int removedValue = currentNode->data;

    if (currentNode == l->head) {
        l->head = currentNode->next;
    } else {
        currentNode->previous->next = currentNode->next;
    }

    if (currentNode == l->tail) {
        l->tail = currentNode->previous;
    } else {
        currentNode->next->previous = currentNode->previous;
    }

    free(currentNode);
    l->count--;

    return removedValue;
}
// DLL Size
// Returns -1 if the DLL is NULL.
// Queries the current size of a DLL
int dll_size(dll_t* l) {
    if (l == NULL) {
        return -1;
    }

    return l->count;
}

// Free DLL
// Removes a DLL and all of its elements from memory.
// This should be called before the program terminates.
void free_dll(dll_t* l) {
    if (l == NULL) {
        return;
    }

    node_t* currentNode = l->head;
    while (currentNode != NULL) {
        node_t* nextNode = currentNode->next;
        free(currentNode);
        currentNode = nextNode;
    }

    free(l);
}

// Helper function to print the elements of the DLL
void print_dll(dll_t* l) {
    if (l == NULL) {
        printf("DLL is NULL.\n");
        return;
    }

    node_t* currentNode = l->head;
    while (currentNode != NULL) {
        printf("%d ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("\n");
}

#endif