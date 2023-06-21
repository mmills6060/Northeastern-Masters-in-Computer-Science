#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stdlib.h>
#include <stdio.h>

// TODO: Create your node_t type here
typedef struct node
{
    int num_wins;
    int year;
    struct node *next; // notice this pointer!
} Pair;

typedef struct list
{
    Pair *head;
    int size;
} NeuList;

Pair *new_node(int wins, int year, Pair *next)
{

    Pair *newNode = (Pair *)malloc(sizeof(Pair));
    newNode->num_wins = wins;
    newNode->year = year;
    newNode->next = next;
    return newNode;
}

NeuList* create_list() {
    NeuList *list = (NeuList *)malloc(sizeof(NeuList));
    list->head = NULL;
    list->size = 0;
    return list;
}

void push_front(NeuList *list, int wins, int year)
{
    Pair *newNode = new_node(wins, year, list->head);
    list->head = newNode;
    list->size++;
}

void add_back(NeuList *list, int wins, int year) {
    Pair *newNode = new_node(wins, year, NULL);
    if (list->head == NULL) {
        list->head = newNode;
    } else {
        Pair *curr = list->head;
        while (curr->next != NULL) {
            curr = curr->next;
        }
        curr->next = newNode;
    }
    list->size++;
}

void print_list(NeuList *list)
{
    // todo
}

Pair *find(NeuList *list, int year)
{
    // todo
    return NULL;
}


void free_list(NeuList *list)
{
    // todo
}

#endif //LINKED_LIST_H