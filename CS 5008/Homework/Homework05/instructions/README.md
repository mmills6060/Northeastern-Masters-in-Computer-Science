# Homework 05 - Sort Analysis

> **Notice**
> This assignment builds directly on Team Activity 05 - Bubble Sort and Team Activity 06 - Merge Sort. You will want to make the code for the activity is completed. 

> This is a two week assignment! (essentially both Homework 05 and 06 combined)

For this homework, you will be writing two other Quadratic Sorts, $O(n^2)$: Insertion and Substitution sort. 
More importantly, you will be running an experiment getting timings for the sorts, and thinking
deeper on the sorts and how to compare the different algorithms.  

Since there are a lot of files with this assignment, let's first examine the files you have:

## Included Files

The files that you will implement:
* [sort_helper.h](../sort_helper.h) - should have been implemented in your team activity. Contains the ability to print an int array, and swap two ints. 
* [sorts.h](../sorts.h) - this is where you will implement your sorts. Please copy the bubble sort of your team activity into this one, and make sure give credit where credit is due. 


Support files to help with implementation and experimentation:
* [insertion_test.c](../insertion_test.c) - provides a few static tests to help with development. 
* [selection_test.c](../selection_test.c)  - provides a few static tests to help with development.
* [merge_test.c](../merge_test.c) -- provides a few static tests for merge start (Team Activity 06)
* [tester.c](../tester.c) - this is the main driver of your program. It will randomly generate arrays, and collect the time it takes to sort the array. You can also specify four different sorts to use, so once all your code is working, use this file to generate data for your experiment. If you want, you may considering writing a script that runs this file repeatedly.


Documentation:
* [README.md](../README.md) - A bit more sparse for this one, as the questions are moved to Report.md. Don't forget the link to your repo as TAs will be looking at the github page to grade. 
* [Report.md](../Report.md) - This is where you will build your data table for your experiment, and answer technical questions. 

## Commonality Between These Sorts
Both Selection Sort and Insertion Sort are meant to be [in place algorithms]. This means the function has 'side affects' which isn't always ideal in modern development, but for sorting of arrays it is often common and effective. Your familiarity with python may cause you to recall `sort()` and `sorted()` making a distinction on which one returns a new list and which one modified the original list. The `sort()` function is an in-place destructive (modifies the parameters) function, similar to what you are writing.

Make sure to use the resources below to visualize the sorts! 

👉🏽 **Task**: In addition to writing the two sorts, you should place comments in the lines explaining what each line does. The goal of this assignment is to demonstrate understanding. 


## Selection Sort
👉🏽 **Task**: Implement the selection sort in [sorts.h](../sorts.h).

<img src="https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif" style="float:right;padding-left:20px;" />

A selection sort sorts by finding the lowest value, and swapping it with the first value it has yet to move. As such, 'selecting' the lowest and moving it. Of course, it could find the highest value with a sign change. 

* `int findMinimum(int *array, int start, int stop)`  - is the function to find the index of the lowest value
* `void selectionSortIntegers(int *array, unsigned int size, int print)` - is your function to sort array in-place. Note: like your lab, if print is 1, then the array should be printed out at each completed step (end of the outer-loop), so you can watch the progress of the sorted array. DO NOT change `printIntArray` or it will break the autograder.

For example:
```text
-9 -7 2 -1 4 -3 6 -5 8 0 10
-9 -7 -5 -1 4 -3 6 2 8 0 10
-9 -7 -5 -3 4 -1 6 2 8 0 10
-9 -7 -5 -3 -1 4 6 2 8 0 10
-9 -7 -5 -3 -1 0 6 2 8 4 10
-9 -7 -5 -3 -1 0 2 6 8 4 10
-9 -7 -5 -3 -1 0 2 4 8 6 10
-9 -7 -5 -3 -1 0 2 4 6 8 10
-9 -7 -5 -3 -1 0 2 4 6 8 10
```

* -9 is already the lowest so doesn't move
* -7 is already the lowest after -9, so doesn't move
* -5 is the next lowest, so swaps with 1
* -3 is the next lowest, so swaps with -1
* -1 is the next lowest, so swaps with 4
* (and so on)

<br style="clear:both"/>

## Insertion Sort
👉🏽 **Task**: Implement the insertion sort in [sorts.h](../sorts.h).

An insertion sort, shown below looks inserts value into their correct location, assuming he left hand size (even if it is one item) is sorted.  So given the graphic, you are looking

For example:

```text
-3 0 2 -1 4 -7 6 -5 8 -9 10
-3 -1 0 2 4 -7 6 -5 8 -9 10
-3 -1 0 2 4 -7 6 -5 8 -9 10
-7 -3 -1 0 2 4 6 -5 8 -9 10
-7 -3 -1 0 2 4 6 -5 8 -9 10
-7 -5 -3 -1 0 2 4 6 8 -9 10
-7 -5 -3 -1 0 2 4 6 8 -9 10
-9 -7 -5 -3 -1 0 2 4 6 8 10
```
* -3 starts of as 'sorted'.
* 0 is greater, so remains
* 2 is greater than 0, so remains
* -1 is less than 2 and 0, but greater than minus -3, moves to the second spot, shifting the rest down. 
* 4 is greater than 2, so remains.
* -7 is less than everything, so moves into the first position. 
* (and so on)


Here is another example:

![Insertion Sort Graphic]


## Calculating Times

Using tester.c, generate a table of timings based on total values sorted. You will want build a table similar to the following (the values are made-up)

| N | Bubble | Selection | Insertion | Merge | Quick |
| :-- | :--: | :--: | :--: | :--: | :--: |
| 10 | 0.05 | 0.02 | 0.0001 | 1 | .5 |
| 100 | 0.5 | 0.2 | 0.001 | 10 | .3 |
| 1000 | 5 | 2 | 0.01 | 100 | .1 |

In truth, your times should be pretty low, and they will vary a lot more. Please make sure to use [markdown table formatting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables), so when TAs view it in github, it looks like a table, and not just text. 

Under the table, make sure to answer the questions specific to your analysis insides of  [Report.md](../Report.md).

We encourage you to spend time, and craft clear answers. You will find markdown has ways to create [diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) and [math expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)



### Growth

One question encourages you to create a line chart (you can create one in google, excel, or your favorite program). When we think of complexity, it helps to compare them visually. For example

![growth]

Another way to look at it, we can think about our searches we touched on in 5001, 5002, and now again in this course.

|Algorithm|	Complexity | n = 100 |  n = 100,000 |
| :-- | :--: | -- | -- |
|Linear Search| $O(n)$| 100 | 100,000 |
|Binary Search| $O(\log_2(n))$ | 6.64 | 16.60 |

> Note: the base 2 of log is often left out in comparison. We included it, so if you took $\log(100)$, you would remember it is actually, $\log_2(100) = 6.64$.



## README.md

Your [README.md](../README.md) has its questions moved to [Report.md](../Report.md). 

## 📝 Grading Rubric


Add (AG) and (MG) next to tiers, add major conditions to meet to pass each tier. Notice, only 2 points are autograded, and two are manually graded! This assignment is focused more on the report. 

1. Learning (AG)
   * Code compiles
   * Swap works correctly
   * Selection and Insertion sort work with basic arrays
2. Approaching  (AG)
   * Selection and Insertion sort work with more complex arrays
   * Neither fail when an array is 0 length
3. Meets  (MG)
   * Comments added to the sorts explaining what each part does.
   * Commits checked (at least 3)
   * README.md is completed 
   * Report has tables and charts. 
   * Questions 1,2,3(all parts) answered correctly.
4. Exceeds  (MG)
   * Remaining Report questions answered correctly.


AG - Auto-graded  
MG - Manually graded

### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade **IF** you submit by the **DUE DATE**. Submitting late may mean it isn't possible for the MG to be graded before the **AVAILABLE BY DATE**, removing any windows for your to resubmit in time. While it will be graded, it is always best to *submit by the due date*, so you have full opportunity to improve your grade.

**Notice** This is time limitation is important for this assignment! 

## 📚 Resources
* [Betty Holberton](https://en.wikipedia.org/wiki/Betty_Holberton) - Developed early sorting algorithms in the early days of computing!
* [Sorting Algorithm Breakdown](https://en.wikipedia.org/wiki/Sorting_algorithm) - Take a look at the stable section, and complexity.
* [Insertion Sort](https://en.wikipedia.org/wiki/Insertion_sort)
* [Selection Sort](https://en.wikipedia.org/wiki/Selection_sort)
* [Latex Math](https://en.wikibooks.org/wiki/LaTeX/Mathematics) - For symbols you can use in markdown math (mathjax)
* [Tables Generator](https://www.tablesgenerator.com/markdown_tables) - Not really used, but there if it helps
* [Searching Algorithms](https://www.geeksforgeeks.org/searching-algorithms/) - there are many algorithms for searching, binary and linear are just the most often compared

[in place algorithms]: https://en.wikipedia.org/wiki/In-place_algorithm
[Insertion Sort Graphic]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif
[growth]: growth.png