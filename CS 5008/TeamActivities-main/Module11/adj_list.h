#ifndef ADJ_LIST_H
#define ADJ_LIST_H

#include <stdio.h>
#include <stdlib.h>

typedef struct edge
{
    int vertex;
    int weight;
    struct edge *next;
} edge_t;

typedef struct graph
{
    int size;
    edge_t **adj_lists;
} AdjList;


edge_t *creat_node(int v, int weight);
AdjList *create_graph(int num_vertices);
void free_graph(AdjList *graph);
void add_edge(AdjList *graph, int src, int dest, int weight);
void print_graph(AdjList *graph);
#endif