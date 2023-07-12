/** 
 * CS 5008 - Homework 09
 * Student: UPDATE NAME
 * Semester: UPDATE SEMESTER
*/
#ifndef HASHMAP
#define HASHMAP

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct node
{
    char *key;
    float value;
    struct node *next;
} h_node;

typedef struct ht {
    int size;
    h_node **contents;

} hashmap;

typedef unsigned long ul;
typedef h_node **hashTable;

/**
 * A hashing algorithm. Students may pick their own
 * but it is recommended they use one of the ones 
 * from the lab. 
*/
ul get_hash(char *str) {

  ul hash = 5381;

  int c;

  while ((c = *str++)) {

    hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
  }

  return hash;
}

/**
 * Creates with the specified size.
*/
hashmap* map_create(int size) {
   hashmap* map = (hashmap*)malloc(sizeof(hashmap));

   map->size = size;

   map->contents = (h_node**)malloc(sizeof(h_node*) * size);
   
   for (int i = 0; i < size; i++) {

       map->contents[i] = NULL;
   }
   
   return map;
}

/**
 * Gets a value from the hashmap. 
 * If a value is not found, return -1.0F
*/
float map_get(hashmap* map, char *key) {
    ul hash = get_hash(key) % map->size;

    h_node* current = map->contents[hash];
    
    while (current != NULL) {

        if (strcmp(current->key, key) == 0) {

            return current->value;
        }
        current = current->next;
    }
    
    return -1.0F;
}

/**
 * Removes an item from the hashmap, returning
 * the value of the item. If an item
 * is not found to remove, return -1.0F
 * 
 * Remember to free the key value before freeing the node.
*/
float map_del(hashmap* map, char *key) 
{
    ul hash = get_hash(key) % map->size;
    h_node* current = map->contents[hash];
    h_node* prev = NULL;
    
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            if (prev != NULL) {
                prev->next = current->next;
            } else {
                map->contents[hash] = current->next;
            }
            
            float value = current->value;
            free(current->key);
            free(current);
            return value;
        }
        prev = current;
        current = current->next;
    }
    
    return -1.0F;
}

/**
 * Stores a value into the hashmap. 
 * 1. if a key is already in the map, overwrites it with the new value
 * 2. if the key is not in the map, adds the key/value (node) pair.
 * 
 * For Keys, you want to use strcpy to copy the key into the node so that
 * the original string passed into the function can be released.
*/
void map_put(hashmap* map, char *key, float value) {
    ul hash = get_hash(key) % map->size;
    h_node* current = map->contents[hash];
    h_node* prev = NULL;
    
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            current->value = value;
            return;
        }
        prev = current;
        current = current->next;
    }
    
    h_node* new_node = (h_node*)malloc(sizeof(h_node));
    new_node->key = (char*)malloc(sizeof(char) * (strlen(key) + 1));
    strcpy(new_node->key, key);
    new_node->value = value;
    new_node->next = NULL;
    
    if (prev != NULL) {
        prev->next = new_node;
    } else {
        map->contents[hash] = new_node;
    }
}

/**
 * Prints the map in the specified format of
 * {key : value, key : value}
 * Notice there is not a comma after the last
 * value. Refer to the lab if needed. It should
 * only produce strings of .2f (two decimals). 
*/


void map_print(hashmap* map) {
    int count = 0;

    printf("{");  // Opening parenthesis

    for (int i = 0; i < map->size; i++) {
        h_node* current = map->contents[i];

        while (current != NULL) {
            if (count > 0) {
                printf(", ");
            }
            printf("%s : %.2f", current->key, current->value);
            count++;
            current = current->next;
        }
    }

    printf("}\n");  // Closing parenthesis
}
/**
 * Frees the map in memory. Make sure
 * to free all the individual nodes. 
*/
void map_free(hashmap* map) {
    for (int i = 0; i < map->size; i++) {
        h_node* current = map->contents[i];
        
        while (current != NULL) {
            h_node* temp = current;
            current = current->next;
            free(temp->key);
            free(temp);
        }
    }
    
    free(map->contents);
    free(map);
}

#endif
