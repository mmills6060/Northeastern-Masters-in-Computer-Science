# Homework 03 - Stacks - Instructions


For this assignment, you will be writing your own stack library. Stacks are used frequently in computer science, so it is important to understand various ways they are implemented and work. Additionally, you will essentially
be writing a library more than an independent program. This means unit testing becomes essential, and your
final deliverable will not have any output to standard out or read from standard in. 


## Stack: LIFO

👉🏽 **Task** 👈🏽: Implement the [mystack.h] file, and corresponding unit test file, [test_stack.c]. 

1. Each function is required.
2. Do not change the function definitions! 
3. Do not change the structs, typedef, or defines
4. You need to use a LinkedList to implement the Stack


Our testing program will be calling the struct directly, along with the functions for unit testing. You  may **add** additional functions if you need (like printing).

Same as test_queue.h, you will need to work with the test_stack.h file, and **need to add** additional unit tests.

You will notice the functions are called enqueue and dequeue even though it is a stack. That is common, as libraries often use common names. .add, and .remove are also common names. While it doesn't matter as much in **C**, this is a hint towards object oriented programming, and making structures interchangeable which Java's SDK is very good at doing since all Collections inherit the same interface. 


As a reminder stack is Last In, First out.  This is commonly called **Push** (enqueue) or **Pop** (dequeue).
![Stack](https://upload.wikimedia.org/wikipedia/commons/b/b4/Lifo_stack.png)  
Image by Maxtremus, CC0, via Wikimedia Commons


### :star: Testing :star:

As you write every function, make sure you test it. The [test_stack.c](../test_stack.c) has a start to sample tests. Including
those tests, you should write two unit tests (at least) for every function you create. Also, notice the array,
and adding function pointers to it. You can uncomment the lines to see how it works, similar to Homework 2. 

```c
int (*unitTests[])(int) = {
    // unitTest1,
    // unitTest2,
    // unitTest3,
    // unitTest4,
    // unitTest5,
    NULL};
```


Here are some ideas for testing:
* Fill a stack, empty the stack, and fill the stack again.
* Create an stack queue and attempt to add something to it.
* Make sure your stack does not overwrite any data
* Try creating a stack directly (by manually linking the pointers), 
and then try to break that sample stack with other functions
* Try to go over 32 entries. 
* And run all these tests with valgrind!

## 📝 Grading Rubric

1. Learning (AG)
   * Stack compiles
   * Stack created properly
   * Stack return empty or full structures
2. Approaching  (AG)
   * Stack can enqueue and dequeue across multiple tests
3. Meets  (AG)
   * Stack properly return size after multiple function calls
   * Stack don't have any memory leaks
4. Exceeds  (MG)
   * Completed [README.md](../README.md)
     * Including answering Further Thinking questions.
     * Had at least a couple paragraphs for a reflection
   * Unit tests added to test_stack - **at least two for every function** (including the provided ones)
   * Code fully documented, including header on each file
   * LinkedList used for Stack


AG - Auto-graded  
MG - Manually graded

### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade **IF** you submit by the **DUE DATE**. Submitting late may mean it isn't possible for the MG to be graded before the **AVAILABLE BY DATE**, removing any windows for your to resubmit in time. While it will be graded, it is always best to *submit by the due date*, so you have full opportunity to improve your grade.


## 📚 Resources
* [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
* [Stack High Level Description](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))
* [Example Single File C Libraries](https://github.com/nothings/single_file_libs)
* [Are header only libraries more efficient?](https://softwareengineering.stackexchange.com/questions/305618/are-header-only-libraries-more-efficient)
* [Header Files from GCC](https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html)
