// Note: This is not an exhaustive test suite, but gives you the idea
//       of some tests you might want to create.
//       Adding more tests and slowly making them more and more complicated
//       as you develop your library is recommended.
//
// Compile this assignment with: clang -g -Wall dll_test.c -o dll_test.out
//
// Run with: ./dll_test.out
#include <stdio.h>  // For IO operations
#include <stdlib.h> // for malloc/free
#include "my_dll.h"


// A sample collection of tests for your program
// We will be adding our own to test your program.

// Tests creation and deletion of list
// Ideally does not cause any segfaults, and this
// is considered passing.
// Dll should also be empty.
int unitTest1(int status)
{
    int passed = 0;
    dll_t *test = create_dll();
    if (dll_empty(test))
    {
        passed = 1;
    }
    free_dll(test);

    return passed;
}

// Tests push_front and size functions
int unitTest2(int status)
{
    int passed = 0;
    dll_t *test = create_dll();
    dll_push_front(test, 789);
    if (1 == dll_size(test))
    {
        passed = 1;
    }
    else
    {
        passed = 0;
    }
    free_dll(test);

    return passed;
}

// Tests push_back and size functions
int unitTest3(int status)
{
    int passed = 0;
    dll_t *test = create_dll();
    dll_push_back(test, 142);
    if (1 == dll_size(test))
    {
        passed = 1;
    }
    else
    {
        passed = 0;
    }
    free_dll(test);

    return passed;
}

// Tests push_front and dll_pop_back functions
int unitTest4(int status)
{
    int passed = 0;
    dll_t *test = create_dll();
    dll_push_back(test, 142);
    dll_pop_back(test);
    if (0 == dll_size(test))
    {
        passed = 1;
    }
    else
    {
        passed = 0;
    }
    free_dll(test);

    return passed;
}

// Tests push_back twice, then pops once
// then should compute the correct size.
int unitTest5(int status)
{
    int passed = 0;
    dll_t *test = create_dll();
    dll_push_back(test, 142);
    dll_push_front(test, 142);
    dll_pop_back(test);
    if (1 == dll_size(test))
    {
        passed = 1;
    }
    else
    {
        passed = 0;
    }
    free_dll(test);

    return passed;
}
// Test create_dll 1
int unitTest6(int status)
{
    dll_t *myDLL = create_dll();

    if (myDLL != NULL)
    {
        printf("Test create_dll 1 passed. DLL created successfully.\n");

        // Additional assertions or tests can be performed here

        // Clean up the DLL after testing
        free_dll(myDLL);
    }
    else
    {
        printf("Test create_dll 1 failed. Unable to create DLL.\n");
    }
}

// Test create_dll 2
int unitTest7(int status)
{
    dll_t *myDLL = create_dll();

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_empty 1
int unitTest8(int status)
{
    dll_t *myDLL = create_dll();

    int isEmpty = dll_empty(myDLL);

    if (isEmpty == 1)
    {
        printf("Test dll_empty 1 passed. DLL is empty.\n");
    }
    else if (isEmpty == 0)
    {
        printf("Test dll_empty 1 failed. DLL is not empty.\n");
    }
    else
    {
        printf("Test dll_empty 1 failed. DLL is NULL.\n");
    }

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_empty 2
int unitTest9(int status)
{
    dll_t *myDLL = create_dll();

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test create_node 1
int unitTest10(int status)
{
    node_t *myNode = create_node(5);

    if (myNode != NULL)
    {
        printf("Test create_node 1 passed. Node created successfully.\n");

        // Additional assertions or tests can be performed here

        // Clean up the node after testing
        free(myNode);
    }
    else
    {
        printf("Test create_node 1 failed. Unable to create node.\n");
    }
}

// Test create_node 2
int unitTest11(int status)
{
    node_t *myNode = create_node(5);

    // Perform additional tests or assertions based on your requirements

    // Clean up the node after testing
    free(myNode);
}

// Test dll_push_front 1
int unitTest12(int status)
{
    dll_t *myDLL = create_dll();

    int item = 42;

    int result = dll_push_front(myDLL, item);

    if (result == 1)
    {
        printf("Test dll_push_front 1 passed. Item %d pushed to the front.\n", item);
    }
    else if (result == 0)
    {
        printf("Test dll_push_front 1 failed. Unable to push item %d to the front.\n", item);
    }
    else
    {
        printf("Test dll_push_front 1 failed. DLL is NULL.\n");
    }

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_push_front 2
int unitTest13(int status)
{
    dll_t *myDLL = create_dll();

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_push_back 1
int unitTest14(int status)
{
    dll_t *myDLL = create_dll();

    int item = 42;

    int result = dll_push_back(myDLL, item);

    if (result == 1)
    {
        printf("Test dll_push_back 1 passed. Item %d pushed to the back.\n", item);
    }
    else if (result == 0)
    {
        printf("Test dll_push_back 1 failed. Unable to push item %d to the back.\n", item);
    }
    else
    {
        printf("Test dll_push_back 1 failed. DLL is NULL.\n");
    }

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_push_back 2
int unitTest15(int status)
{
    dll_t *myDLL = create_dll();

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_pop_front 1
int unitTest16(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_pop_front and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_pop_front 2
int unitTest17(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_pop_front and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_pop_back 1
int unitTest18(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_pop_back and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_pop_back 2
int unitTest19(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_pop_back and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_insert 1
int unitTest20(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_insert and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_insert 2
int unitTest21(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_insert and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_get 1
int unitTest22(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_get and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_get 2
int unitTest23(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_get and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_remove 1
int unitTest24(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_remove and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_remove 2
int unitTest25(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_remove and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_size 1
int unitTest26(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_size and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test dll_size 2
int unitTest27(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    // Perform dll_size and check the result

    // Perform additional tests or assertions based on your requirements

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test free_dll 1
int unitTest28(int status)
{
    dll_t *myDLL = create_dll();

    // Perform free_dll and check if the DLL is successfully freed

    free_dll(myDLL); 
   // Perform additional tests or assertions based on your requirements
}

// Test free_dll 2
int unitTest29(int status)
{
    dll_t *myDLL = create_dll();

    // Perform free_dll and check if the DLL is successfully freed

    // Perform additional tests or assertions based on your requirements
    free_dll(myDLL); 
}

// Test print_dll 1
int unitTest30(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    printf("Test print_dll 1: ");
    print_dll(myDLL);

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// Test print_dll 2
int unitTest31(int status)
{
    dll_t *myDLL = create_dll();

    // Populate the DLL with some nodes

    printf("Test print_dll 2: ");
    print_dll(myDLL);

    // Clean up the DLL after testing
    free_dll(myDLL);
}

// An array of function pointers to all of the tests
// that main() can use iterate over them.
// UNCOMMENT Tests as you are ready to use them
// Add your own tests!
int (*unitTests[])(int) = {
    unitTest1,
    unitTest2,
    unitTest3,
    unitTest4,
    unitTest5,
    unitTest6,
    unitTest7,
    unitTest8,
    unitTest9,
    unitTest10,
    unitTest11,
    unitTest12,
    unitTest13,
    unitTest14,
    unitTest14,
    unitTest15,
    unitTest16,
    unitTest17,
    unitTest18,
    unitTest19,
    unitTest20,
    unitTest21,
    unitTest22,
    unitTest23,
    unitTest24,
    unitTest25,
    unitTest26,
    unitTest27,
    unitTest28,
    unitTest29,
    unitTest30,
    unitTest31,
    NULL};

// ====================================================
// ================== Program Entry ===================
// ====================================================
int main()
{
    unsigned int testsPassed = 0;
    // List of Unit Tests to test your data structure
    int counter = 0;
    while (unitTests[counter] != NULL)
    {
        printf("========unitTest %d========\n", counter);
        if (1 == unitTests[counter](1))
        {
            printf("passed test\n");
            testsPassed++;
        }
        else
        {
            printf("failed test, missing functionality, or incorrect test\n");
        }
        counter++;
    }

    printf("%d of %d tests passed\n", testsPassed, counter);

    return 0;
}