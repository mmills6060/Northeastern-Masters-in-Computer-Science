// Compile this assignment with: clang -g -Wall main.c -o main.out
// Use this file to implement testing for your
// doubly linked list implementation

#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free

#include "my_dll.h"




// ====================================================
// ================== Program Entry ===================
// ====================================================
int main() {
    dll_t* myDLL = create_dll();

    // Testing the DLL functions
    dll_push_back(myDLL, 10);
    dll_push_front(myDLL, 5);
    dll_push_back(myDLL, 15);
    dll_push_front(myDLL, 2);

    printf("DLL size: %d\n", dll_size(myDLL));  // Output: 4
    print_dll(myDLL);                           // Output: 2 5 10 15

    dll_remove(myDLL, 2);
    dll_insert(myDLL, 2, 8);

    printf("DLL size: %d\n", dll_size(myDLL));  // Output: 4
    print_dll(myDLL);                           // Output: 2 5 8 15

    dll_pop_front(myDLL);
    dll_pop_back(myDLL);

    printf("DLL size: %d\n", dll_size(myDLL));  // Output: 2
    print_dll(myDLL);                           // Output: 5 8

    free_dll(myDLL);

    return 0;
}