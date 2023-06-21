# Solution

## Program Arguments
Here is a solution for the program arguments. This is not the only solution, but it is one that works.

```c
#include <stdio.h>

int main(int argc, char** argv)
{
    if(argc < 2) {
        printf("You must pass in at least one argument\n");
        printf("Example: %s argument1 argument2\n", argv[0])
        return 1;
    }
    printf("The number of arguments is %d\n", argc);
    for (int i = 0; i < argc; i++)
    {
        printf("Argument %d is %s\n", i, argv[i]);
    }
}
```

## Reading a File
Here is a solution for reading a file. This is not the only solution, but it is one that works.

```c
#include <stdio.h>
#include <stdlib.h>


#define BUFF_SIZE 1024

int main(int argc, char** argv) {
    if(argc != 2) {
        printf("You must pass in at least one argument\n");
        printf("Example: %s file_name\n", argv[0])
        return 1;
    }
    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        printf("Error opening file\n");
        exit(1);
    }   
    char* line = malloc(BUFF_SIZE * sizeof(char));
    while (fgets(line, BUFF_SIZE, fp) != NULL)
    {
        printf("%s", line);
    }
    free(line);
    fclose(fp);
    return 0;

}

```


## Estimator.c
Here is a solution for the run_program function in estimator.c. This is not the only solution, but it is one that works.

```c
    int * counts = calloc(11, sizeof(int));

    FILE *fp = fopen(file_name, "r");
    if (fp == NULL)
    {
        printf("Error opening file\n");
        exit(1);
    }
    char* line = malloc(BUFF_SIZE * sizeof(char));
    while (fgets(line, BUFF_SIZE, fp) != NULL)
    {
        convertToUpperCase(line);
        for (int i = 0; i < 11; i++)
        {
            if (contains(line, instructions[i]))
            {
                counts[i]++;
            }
        }
    } 

    print_info(counts);

    free(line);
    free(counts);
    fclose(fp);
```