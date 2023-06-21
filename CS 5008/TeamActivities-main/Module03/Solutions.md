

## Printing a List

Notice that NULL is the stopping point, and using while loops is a good way to iterate over a list.



```c
   Pair *current = list->head;
    while (current != NULL)
    {
        printf("(%d %d)", current->num_wins, current->year);
        current = current->next;
        if(current != NULL)
        {
            printf("-> ");
        }
    }
    printf("\n");
```


## Finding an Item

Finding an item is similar to printing, but you have to check the value of the node to see if it matches the value you are looking for. If it does, you return the node. If it doesn't, you keep iterating until you find it, or you reach the end of the list. If you reach the end of the list, you return NULL.


```c
Pair *find(NueList *list, int year)
{
    Pair *current = list->head;
    while (current != NULL)
    {
        if (current->year == year)
        {
            return current;
        }
        current = current->next;
    }
    return NULL;
}
```

## Freeing Memory
When you are dealing with data structures, you often have to loop through the items and free them individually. Like the following. 

```c
void free_list(NeuList *list)
{
    Pair *current = list->head;
    while (current != NULL)
    {
        Pair *next = current->next;
        free(current);
        current = next;
    }
    free(list);
}
```