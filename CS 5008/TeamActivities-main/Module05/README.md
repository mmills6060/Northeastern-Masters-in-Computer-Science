# Team Activity - Sorting (Part 1)


For this activity you will be writing a simple bubble sort, while discussing about sorts and BigO. A bubble sort is one of three sorts we will write this module, with the other two also being quadratic ($O(n^2)$) sorts: insertion and selection.  While the code during this workshop will be done as a group, you will use the code from your lab directly in your weekly assignment. 

Sorts are often openly available online, so the real key over the next two weeks is understanding which sort to use in which situation.

## Bubble Sort
Bubble Sort is one of the oldest sorts, and if you line people up asking them to sort by their names, they will often default to a bubble sort. 

The idea behind a bubble sort is that you compare two side by side numbers, swapping them if the right is lower than the left. It is also worth noting the bubble sort is an in place sort, meaning you can sort the array modifying it directly. 

### 👉🏽 **Task**  Practice
With your group, take turns writing out 5 values, then write out what the array looks like after 1 complete pass. 

For example:
```text
4 2 1 3 5
2 1 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
```

For five values, you will have five rows even if the sort looks complete to humans, computers still need to check the values. 


You can also [visualize] the sort! (suggestion right click and open the visualization into a new tab).

### Another Example from wikipedia:

![bubble]



## Writing Code and Running It
To get started, download the associated code:

* [sort_helper.h](sort_helper.h)
* [sorts.h](sorts.h)
* [tester.c](tester.c) 

When you compile your code, you will be compiling from tester.c

```console
> clang -Wall tester.c -o tester.out
```

To run your bubble sort, it would be something like the following
```text
> ./tester.out 0 5 print
```
Print is optional, but is great for figuring out each stage, like above in the example. The first number tells the program which sort to run  
     
0 = bubble sort  
1 = a sort built into the c stdlib. 

The second number is the number of random numbers you want generated.

### Testing current code
Right now, the bubble sort doesn't work! (you have to write it). But the sort built into C does work. As such, you can test  `tester.c` with the following

```text
> clang -Wall tester.c -o tester.out
> ./tester.out 1 10000
```
(the print doesn't work with the built in c library as it isn't an option.)

### Writing Swap (10 minutes)
To write the bubble sort, the first you need to do is write a 'swap' function.  The template has been provided in `sort_helper.h`.

```c
void swap(int *a, int *b)
{
    // TODO: Swap two integers in an array.
}
```

The idea is to take two values and swap, so if a comes in with 20, and b comes in with 10, by the end of the function a will be 10, and b will be 20. You can create a temp pointer. 

Go ahead and work on this as a group. 

### Writing Bubble Sort (40 Minutes)
While bubble sort is well documented you should try writing it, talking it through with your partners. A bubble sort will be two nested for loops. One that goes through the entire array, and one that is performing the swaps on each number. The print should be setup in the 'outer-loop' so you can see what the array looks like after each pass. Don't forget to put `if(print)` before your print, or your code may slow down considerably when you are testing large arrays. 



## Deeper Understanding
As you write the bubble sort, make sure to comment on each line what it is doing and why. Bubble sore is well documented, so it is more important that you understand the why than coming up with a creative solution. 

1. Bubble sort is $O(n^2)$. Looking at the algorithm can you explain to your group why that is?
2. Can you come up with an array that will generate the "worst case"? 
3. Can you come up with an array that will generate the "best case"?
   * By default, the best case is the same, but can you optimize it?
   * Given the example above, optimize it so it stops running after the array is sorted? 
     * The optimized version is more common, and gives us the "best case".


## Compare Sorts
Compare the bubble sort against the other sort provided in C using tester. Try it with various sized arrays. You may want to write down the attempts. 


For example:
| N | Bubble |  Quick |
| :-- | :--: | :--: |
| 10 | 0.05 | 0.001 |
| 100 | 0.5 | 0.01 |
| 1000 | 5 |  0.1 |
| 5000 | ... | ... |

We suggest you run it *without* print, as print will slow down the code. So for example, your run code would look like:

```text
> ./tester.out 0 10000
> ./tester.out 1 10000
```

You will notice on larger numbers, the bubble starts to really slow down, while the qsort (quick sort) doesn't.  Have one member store the runs of the output into a spreadsheet, and then graph the results between the two sorts. 

## Homework Prep
With your group, talk about the differences between Insertion, Bubble, and Selection sorts. Try to work them out on paper first!

Work each one out on paper - similar to how you did for the 5 value array above for bubble sort. Make you use the [visualize] tool to better understand!


## Leet Code Practice

Lastly, work on modules 04 leet code practice. Everyone pick a different problem, and take turns explaining your solution *as* you work through the code (as time allows). This is called "live coding" and often required in technical interviews. Moving forward, we would like you to emphasize the explaining of code as you work through it, to better prepare you for technical interviews.


## 📚 Resources
* [Bubble Sort on Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)
* [C Program Bubble Sort](https://www.geeksforgeeks.org/c-program-for-bubble-sort/)
* [Bubble by Geeks for Geeks](https://www.geeksforgeeks.org/bubble-sort/)



[bubble]: https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif
[visualize]: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/