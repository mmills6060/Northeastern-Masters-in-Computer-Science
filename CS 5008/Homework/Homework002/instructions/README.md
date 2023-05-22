# Homework 02 Instructions

Often in the software engineering industry, you will be asked to pickup a new language on the fly. This is because a language is a tool, and you are often needing to select the best tool for the job. In this course, we use C as it helps us better understand the underlying system that we are working with. Learning a new language can be challenging, but the best way to is to find relationships to what you know while also taking time to practice the syntax differences. This homework is designed to help you learn a new language, and get you comfortable with the process of learning a new language. You will be asked to learn the basics of C, and then implement a few functions in C. You will also be asked to write a few tests in C. 


## Provided Files
👉🏽 **Task** 👈🏽: look through provided files to see what is going on while also updating the comments at the top of the file. Make sure to ask questions if you are unsure what is going on!

For this assignment (and all others) you will be provided some files to work with. It is always best to look through the provided files to see what is going on while also updating the comments at the top of the file. 

The files provided for this assignment are:
* [cpractice.h](../cpractice.h) - This files contains all the functions you need to implement along with the structs you need to use. You will notice the function signatures are provided, along with the struct definitions. You will need to implement the functions in [cpractice.h](../cpractice.h) following the comments provided. The various print functions are intentionally implemented for you, so you can use them.
* [main.c](../main.c) - This file contains a sample run of the program testing the various features. You can run this file to see the output of the program, but it is recommended you wait until the end to run it. 
* [tests.c](../tests.c) - This file will be where you will store your tests. **FOR EVERY FUNCTION** you implement except for free'ing memory, you will immediately want to implement a few tests to ensure it is working properly. These tests should try to break the function / look at edge cases, in addition to just making sure works. In true test driven development, you should actually write the tests first, before writing a function. Take a look at this code, how are we running the functions (notice we are adding them to the array).
   > A key concept here - write tests after *every* function. Don't wait until the end. You will thank yourself if you incrementally write tests as you go.


## Write your Code and Tests
👉🏽 **Task** 👈🏽: Write your functions!

Now following the comments in [cpractice.h](../cpractice.h), implement the functions. You will also need to write tests for each function in [tests.c](../tests.c). 

:star: **Important** :star:  
You should incrementally write your code, testing as you go along! 


### Compiling Your Code
As a guideline, here are steps to compile your code via the command line. Even if you are using an IDE, you may find it is easier to compile via the command line.

1. Open your terminal and navigate to the directory with your .h and .c files. 
   * Reminder, you can use `cd` to change directories, and `ls` to list the files in the current directory.
2. To compile run:
   * `clang -Wall tests.c -o test.out` - and then to run your tests, run `./test.out`.
   * `clang -Wall main.c -o main.out` - and then to run your program, run `./main.out`. 


> **IMPORTANT**  
> You should always compile with the `-Wall` flag. This will show you all warnings, which are often errors in your code. You should always fix all warnings before submitting your code as we compile with the -Wall flag on the grading server.

#### :star: Compile Frequently :star:  
It is very easy to have a small error in your code (missing a semicolon), and then have a ton of errors when you compile. It is best to compile frequently, so you can catch these errors early. Often professional developers will compile after every 'chunk' (often 3-4 lines) of code they write. This is a good habit to get into. While the code may not be fully working, it helps you catch errors early. This is also why you should test every function *as you write them*. 


## Questions
In your README.md, there are a number of questions to answer (moving forward you should just assume this is the case).


## 📝 Grading Rubric

1. Learning (AG)
   * Code compiles with no warnings or errors
   * Swap works
   * Basic create fibonacci array works
   * Basic reverse array works
2. Approaching  (AG)
   * Works for edge cases for fibonacci array, and reverse array
   * double array works
   * Copy array works in simple cases (0 <= start < end < size)
   * Create point works
   * Create Polygon, rectangle, and triangle works
3. Meets  (AG)
   * Copy array works in wrap cases (0 <= end < start < size)
   * Calculate area works for different shapes
4. Exceeds  (MG)
   * At least 3 commits
   * All values stored on the heap are properly freed
   * Complete test coverage in tests.c. Including multiple tests for every function except for the ones we provided (the ones that included print), and edge cases checked. You do not have to test free_polygon (but you should look it up in the debugger).
   * Code documented properly (including explaining tests)
   * README.md questions answered correctly



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade **IF** you submit by the **DUE DATE**. Submitting late may mean it isn't possible for the MG to be graded before the **AVAILABLE BY DATE**, removing any windows for your to resubmit in time. While it will be graded, it is always best to *submit by the due date*, so you have full opportunity to improve your grade.


## 📚 Resources
* [Learning C](https://www.linkedin.com/learning/learning-c-5/)  is a tutorial on C in LinkedIn Learning (free with your Northeastern Login)
* [Essential C](https://www.linkedin.com/learning/c-essential-training/) is another tutorial on C in LinkedIn Learning (free with your Northeastern Login)
* [Learn C Interactive Tutorial](http://www.learn-c.org/)
* [clang compiler](https://clang.llvm.org/)
* [gcc compiler](https://www.gnu.org/software/gcc/)
