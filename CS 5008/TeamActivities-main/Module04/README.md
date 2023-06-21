# Team Activity File Reading and Analyzing Assembly

This lab seeks to help you understand File I/O in c, along with seeing the basic assembly that is generated for programs before it goes into a binary form.

For this team activity, you will have multiple small programs to write. The goals for this team activity are as follows:
* Better understand command line program arguments
* Better understand reading files in c
* Better understand the assembly generated for a program, and the cost of various commands

## :star: Working in Teams :star:
When working in teams, remember do not let one person do all the work. Make sure to work together, and ask questions. It is also better if different people program, and you all take turns programming for various team assignments. 



## Program Arguments
Programs, especially command line programs, have arguments that are passed into them, and based on those arguments it changes how the program runs.  For example, 

* `ls -l` on the linux / macOS command line will list the files in the current directory in a long format. 
* `code my_file.c` will open the file my_file.c in Visual Studio Code.
* `gcc -g -Wall my_file.c -o my_file.out` will compile the file my_file.c into an executable called my_file.out

Everything after the program name, is an argument!  

In c programming, you will notice the main function as two optional arguments

```c
int main(int argc, char** argv){
    // code goes here
}
```

* argc - is the argument count. This is the number of arguments passed into the program. It is always at least 1
* argv - is an array of strings. Each string is an argument passed into the program. The first argument is always the program name.


👉🏽 **Your Task**  Write a program that prints out all of the arguments passed into it. Make it so at least one argument is passed into it. 

### Discussion
* What is the first argument passed into the program?
* Why would having program arguments be useful for programs?


## Reading a File
If you followed Mike Shaw's video, you will have a good idea of how to read a file. This follows a similar guideline. 

The standard c library stdlib provides a number of File access functions.  If you wanted to open a file using the first 
program argument, you could do it the following way

```c
FILE *input = fopen(argv[1],"r");
```

```c
char buff[BUFF_SIZE]; 

FILE *input = fopen(argv[1],"r");
char* line = malloc(BUFF_SIZE * sizeof(char));
while (fgets(line, BUFF_SIZE, input) != NULL) {
    // do the thing, line now has the line from input
    
}

free(line); // don't forget to free memory!
fclose(input); // don't forget to close a file!
```

👉🏽 **Your Task**  Read the file with the name passed in via program arguments, and print out its contents to the screen 


## Generating Assembly Files 

Both gcc and clang allow you to generate the assembly file for their code.  Looking at [simple.c], we see a program that
simply adds two numbers, and then ends. However, [simple.s] is the assembly built from this program. This was done using the following option.

> clang -S simple.c

👉🏽 **Your Task** Generate the assembly code for the programs you just wrote by using the -S option.


### Discussion
* What are some of the assembly commands generated? 
* Was there more than you expected? 
* If you run `clang -S shift.c`. Do you notice anything unusual about the generated assembly? (alright if you don't.. will cover it below)

## Finishing Estimator
Estimator is a program that helps estimate the total number of processor cycles for a program to run. This can be helpful when comparing the costs of various operations in your program (though it is very loosely done).

Go ahead and use [estimator.c] for your template. You will notice the skeleton is implemented, but you will need to complete the `run_program` function


👉🏽 **Your Task**  Go ahead and finish the `run_program` function.


### Discussion
* What were some challenges?
* What do the cycles tell you about the difficulty of the process for the computer?
* Why does this/knowing assembly matter?
  * This right here is the hard one. It can be difficult to see the forest through the trees, so discuss some reasons that come to mind and share them with the class at the end. 
* If you have time, use the Godbolt tool (linked below) to try equivalent programs in various languages. 
  * How does python and c differ, even if it the code is "equivalent"?

## Diving Into Optimization

As a quick reminder, there is a the `shift` operators in most languages. The left and right shift operators are `<<` and `>>` respectively. These operators shift the bits of a number left or right. For example, `5 << 1` is `10` and `10 >> 1` is `5`.

Go ahead and compile shift.c, and run the program. For example

```bash
clang shift.c -o shift.out
./shift.out 10
```

Notice all three statements are equivalent! However, if you look at the assembly generated, you will notice that the first two are the same, but the third is different. Why do you think this is? Compilers will try to optimize their code, and since the cycle costs of MUL is more than SHL, it will try to use SHL when possible.

:star: Go ahead and run your estimator on shift.s. Take a look at the total cycle cost. :star:

Important - before this next step, you will want to backup your shift.s file. You can do this by running the following command

```bash
cp shift.s shift.s.bak
```

### Optimization Level 3
A good compiler will go even farther. Try the following compile command.

```bash
clang shift.c -S -O3
```

That is the letter O, not the number 0. This will compile the code with the highest level of optimization. Now look at the assembly generated. Notice how it is different than the previous assembly generated.

:star: Go ahead and run your estimator on shift.s. Take a look at the total cycle cost. :star:

### Discussion
* How did the total cycle costs of the program change? When setting up this team activity, it was a substantial difference! 


## Leet Code Challenge Problem Practice

As per our standard end of the team activity - go to the Module 03 challenge problems, and as a group pick a couple to work on. Discuss your solutions. 


## 📚 Resources

* [strstr() tutorial](https://www.tutorialspoint.com/c_standard_library/c_function_strstr.htm)
* [CString reference](https://cplusplus.com/reference/cstring/)
* [Compiler Explorer](https://godbolt.org/) - really neat tool to explore compiled code
* [Guide to Cycle Costs](https://www.agner.org/optimize/instruction_tables.pdf)


[simple.c]: simple.c
[simple.s]: simple.s
[estimator.c]: estimator.c