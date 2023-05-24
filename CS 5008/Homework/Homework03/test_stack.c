/*  ========== H03 - Personal Queue Implementation ============

 *
 *   Student: UPDATE
 *   Semester: UPDATE
 *
 * A simple queue unit-tst implementation
 *
 */

#include "mystack.h"
// Note that we are locating this file
// within the same directory, so we use quotations
// and provide the path to this file which is within
// our current directory.

// A sample test of your program
// You can add as many unit tests as you like
// We will be adding our own to test your program.

// Tests the capacity of a stack
int unitTest(int status)
{
    int passed = 0;

    neu_stack *test_s = create_stack(MAX_DEPTH);
    if (MAX_DEPTH == test_s->capacity)
    {
        passed = 1;
    }

    free_stack(test_s);

    return passed;
}

// Enqueu several items into a stack and test the size
int unitTest1(int status)
{
    int passed = 0;

    neu_stack *test_s = create_stack(MAX_DEPTH);
    stack_enqueue(test_s, 1);
    stack_enqueue(test_s, 2);
    stack_enqueue(test_s, 3);
    stack_enqueue(test_s, 4);
    stack_enqueue(test_s, 5);
    stack_enqueue(test_s, 6);
    stack_enqueue(test_s, 7);
    stack_enqueue(test_s, 8);
    stack_enqueue(test_s, 9);
    stack_enqueue(test_s, 10);

    if (10 == stack_size(test_s))
    {
        passed = 1;
    }

    free_stack(test_s);

    return passed;
}

// Tests enqueuing and fully dequeing a stack
int unitTest2(int status)
{
    int passed = 0;

    neu_stack *test_s = create_stack(MAX_DEPTH);
    int i = 0;
    for (i = 0; i < MAX_DEPTH; i++)
    {
        stack_enqueue(test_s, 1);
    }
    for (i = 0; i < MAX_DEPTH; i++)
    {
        stack_dequeue(test_s);
    }

    if (0 == stack_size(test_s))
    {
        passed = 1;
    }

    free_stack(test_s);

    return passed;
}

// Tests enqueuing and fully dequeing a stack multiple times
int unitTest3(int status)
{
    int passed = 0;

    neu_stack *test_s = create_stack(MAX_DEPTH);
    int i = 0;
    for (i = 0; i < MAX_DEPTH; i++)
    {
        stack_enqueue(test_s, 1);
    }
    for (i = 0; i < MAX_DEPTH; i++)
    {
        stack_dequeue(test_s);
    }
    for (i = 0; i < MAX_DEPTH; i++)
    {
        stack_enqueue(test_s, 1);
    }
    for (i = 0; i < MAX_DEPTH; i++)
    {
        stack_dequeue(test_s);
    }
    if (0 == stack_size(test_s))
    {
        passed = 1;
    }

    free_stack(test_s);

    return passed;
}

// Simple enqueu and deque stack test
// Also confirms that a stack is full
int unitTest4(int status)
{
    int passed = 0;

    neu_stack *test_s = create_stack(1);
    stack_enqueue(test_s, 1);
    if (1 == stack_full(test_s))
    {
        passed = 1;
    }
    else
    {
        free_stack(test_s);
        return 0;
    }

    stack_dequeue(test_s);
    if (0 == stack_full(test_s))
    {
        passed = 1;
    }
    else
    {
        passed = 0;
    }

    free_stack(test_s);

    return passed;
}

// TODO: Add more tests here
// add your own, and uncomment the provided tests as
// things are implemented
// test create stack 1
int unitTest5(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    if (s->capacity != 5)
    {
        passed = 0;
    }
    free_stack(s);
    return passed;
}
// test create stack 2
int unitTest6(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(10);

    if (s->capacity != 10)
    {
        passed = 0;
    }
    free_stack(s);
    return passed;
}
// test stack empty 1
int unitTest7(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    if (stack_empty(s) != 1)
    {
        passed = 0;
    }
   stack_enqueue(s, 10);

   if (stack_empty(s) != 0)
    {
        passed = 0;
    }
    if (stack_top(s) != 10)
    {
        passed = 0;
    }
    free_stack(s);
    return passed;
}

// test stack empty 2
int unitTest8(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    if (stack_empty(s) != 1)
    {
        passed = 0;
    }
   stack_enqueue(s, 10);

   if (stack_empty(s) != 0)
    {
        passed = 0;
    }
    if (stack_top(s) != 10)
    {
        passed = 0;
    }
    free_stack(s);
    return passed;
}
// test stack full 1
int unitTest9(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    if (stack_full(s) != 0)
    {
        passed = 0;
    }
   return passed;
}    
// test stack full 2
int unitTest10(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(10);

    if (stack_full(s) != 0)
    {
        passed = 0;
    }
   return passed;
}
// test stack enqueue 1
int unitTest11(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    if (stack_top(s) != 10)
    {
        passed = 0;
    }
   return passed;
}
// test stack enqueue 2
int unitTest12(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    if (stack_top(s) != 20)
    {
        passed = 0;
    }
   free_stack(s);
   return passed;
}
// test stack dequeue 1
int unitTest13(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    stack_dequeue(s);
    if (stack_top(s) != 10)
    {
        passed = 0;
    }
   return passed;
}
// test stack dequeue 2
int unitTest14(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    stack_enqueue(s, 30);
    stack_dequeue(s);
    stack_dequeue(s);
    if (stack_top(s) != 10)
    {
        passed = 0;
    }
   return passed;
}
// test stack_size 1
int unitTest15(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    if (stack_size(s) != 2)
    {
        passed = 0;
    }
   return passed;
}
// test stack size 2
int unitTest16(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    stack_dequeue(s);
    if (stack_size(s) != 1)
    {
        passed = 0;
    }
   return passed;
}
// test free stack 1
int unitTest17(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    free_stack(s);
    if (stack_size(s) != 0)
    {
        passed = 1;
    }
    return passed;
}
// test free stack 2
int unitTest18(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    free_stack(s);
    if (stack_size(s) != 0)
    {
        passed = 1;
    }
    return passed;
}
// test stack top 1
int unitTest19(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    if (stack_top(s) != 20)
    {
        passed = 0;
    }
   return passed;
}
// test stack top 2
int unitTest20(int status)
{
    int passed = 1;
    neu_stack *s = create_stack(5);

    stack_enqueue(s, 10);
    stack_enqueue(s, 20);
    stack_dequeue(s);
    if (stack_top(s) != 10)
    {
        passed = 0;
    }
   return passed;
}

int (*unitTests[])(int) = {
    unitTest,
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
    unitTest15,
    unitTest16,
    unitTest17,
    unitTest18,
    unitTest19,
    unitTest20,
    NULL};

// ====================================================
// ================== Program Entry ===================
// ====================================================
int main()
{
    unsigned int testsPassed = 0;
    // List of Unit Tests to test your data structure
    int (*unitTests[])(int) = {
        unitTest,
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
        unitTest15,
        unitTest16,
        unitTest17,
        unitTest18,
        unitTest19,
        unitTest20,
        NULL};
    int counter = 1;
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