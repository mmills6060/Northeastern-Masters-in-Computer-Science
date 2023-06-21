# Dynamic Programming

In this activity we will explore dynamic programming. It is a fancy term, often taught in overly mathematical ways to say:

> If we already calculated an answer, save it, so we don't have to calculate it again!

Really, that is the heart of it. The idea we are willing to spend more on memory, to save time on speed. While there are some complexities, 
the idea of [memoization] is at the heart of it. If a function is a [pure function], it is relatively easy store the result? 
Why because with pure functions, you have the following properties (source wikipedia):

1. the function return values are identical for identical arguments 
2. the function has no side effects 

In this lab, you will explore adding [memorization] to Pascal's Triangle and exploring the differences
in speed. This will help you practice for the midterm project. 


## Dynamic Programming Warm Up Discussion

As a team, find three to four algorithms that use dynamic programming. You do not need to implement them, or even fully understand them, but you should work together to understand how dynamic programming is being used to help with the algorithm. 

Now that you are thinking about what is dynamic programming, it is time to work together on a sample problem.


## Pascal's Triangle

Here is a cool video for [Pascal's Triangle] (that hopefully you watched before this team activity): [Pascal's Triangle - Numberphile]

The idea behind Pascal's triangle is that starting 1 for spot 0,0 (first row, single element), each following row is sum of two numbers directly above it. All outer edges are always 1. 

![Triangle Animated]

Mathematically, this is represented as 


$$\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$$

or a way to look at it code wise:
```c
unsigned long long pascalr(int n, int k) {
   if (n == k || k == 0)
      return 1;
   else
      return pascalr(n - 1, k) + pascalr(n - 1, k - 1);
}
```

You then have to loop through $n$ and $k$ calling your generator. 
```c
for (int i = 0; i < n; i++) {
   for (int j = 0; j <= i; j++) {              
      unsigned long long tmp = pascalr(i, j);
      printf("%llu ", tmp);
   }
   printf("\n");
}
```

However, while this algorithm is mathematically sound and easier to write, it is extremely inefficient.

There are solutions that are cheaper, and your next step is to add memoization to reduce the cost of this algorithm. 

## Updating Pascal.c
You will see [pascal.c](pascal.c) already has the above recursive version and an iterative version that
is more expensive on memory, but is faster. There is an even faster iterative version, but it struggles with
larger numbers due a multiplication and division calculation [ref](https://en.wikipedia.org/wiki/Binomial_coefficient#In_programming_languages). 

### Discussion and Code 
Take this time to compile the given code, and play with the two given solutions. For example if your compile
command is 

```text
clang -Wall pascal.c -o pascal.out
```

You could run the following to produce the following output:

```text
./pascal.out 10 0 2
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
```

or

```text
./pascal.out 10 1 2
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
```

Both will run relatively quickly, but if you increase your number to ~35, you will see a noticeable increase in time to finish for the recursive version as compared to the iterative solution. 

👉🏽 **Task**: Discuss the following together:
* What is the Big O for each version, and 
* What are observations about the code? 
  * For example, why use uint64 -what does that even mean!? 
  * Why use typedef? 
* You can also look up solutions online (there are a plenty of them) and discuss what you find.   



### Dynamic Programming
👉🏽 **Task**: Use [pascal.c] to write a dynamic programming variation of how to solve Pascal's Triangle for the Nth row.

Take a moment to discuss and describe dynamic programming in your own words to your team.  What are some things you are going to need to write a dynamic version of pascal's triangle. 

1. Make sure you declare a multidimensional array. 
2. Then for each value of  `[n][k]` store that answer in the table, if it isn't already in the table.   
   Hint: since Pascal's triangle always has positive values 1 or higher, you can do the following for a check
   ```c
    if (table[n][k] > 0)  return table[n][k];
   ```

## Analysis

Writing "scripts" such as [pascal.py](pascal.py) is a very common practice. In this case, it is setup to help generate comparable data between the different types of implementations. Take a moment to explore the script, and generate some data. 

Here is an example output using the script, timeout set to 60 seconds.

| n | Iterative | Recursive | Dynamic Programming |
|--|:--:|:--:|:--:|
| 1    | 0.00304 | 0.00244 | 0.00237 |
| 2    | 0.00236 | 0.00272 | 0.00245 |
| 3    | 0.00284 | 0.00293 | 0.00232 |
| 4    | 0.00236 | 0.00276 | 0.00250 |
| 5    | 0.00234 | 0.00249 | 0.00248 |
| 6    | 0.00283 | 0.00238 | 0.00266 |
| 7    | 0.00241 | 0.00232 | 0.00264 |
| 8    | 0.00242 | 0.00240 | 0.00273 |
| 9    | 0.00269 | 0.00272 | 0.00299 |
| 10   | 0.00249 | 0.00276 | 0.00268 |
| 11   | 0.00277 | 0.00229 | 0.00256 |
| 12   | 0.00245 | 0.00237 | 0.00233 |
| 13   | 0.00276 | 0.00237 | 0.00231 |
| 14   | 0.00260 | 0.00239 | 0.00237 |
| 15   | 0.00226 | 0.00242 | 0.00233 |
| 16   | 0.00229 | 0.00249 | 0.00232 |
| 17   | 0.00231 | 0.00239 | 0.00254 |
| 18   | 0.00234 | 0.00436 | 0.00274 |
| 19   | 0.00276 | 0.00467 | 0.00338 |
| 20   | 0.00258 | 0.00895 | 0.00268 |
| 21   | 0.00251 | 0.01675 | 0.00331 |
| 22   | 0.00277 | 0.03272 | 0.00301 |
| 23   | 0.00320 | 0.06526 | 0.00303 |
| 24   | 0.00266 | 0.11526 | 0.00330 |
| 25   | 0.00257 | 0.16509 | 0.00283 |
| 26   | 0.00274 | 0.31644 | 0.00357 |
| 27   | 0.00291 | 0.56648 | 0.00307 |
| 28   | 0.00327 | 1.11818 | 0.00310 |
| 29   | 0.00315 | 2.22168 | 0.00330 |
| 30   | 0.00273 | 4.47703 | 0.00326 |
| 31   | 0.00289 | 8.73789 | 0.00339 |
| 32   | 0.00318 | 17.51031 | 0.00326 |
| 33   | 0.00301 | 35.20920 | 0.00334 |
| 34   | 0.00306 |    -    | 0.00333 |
| 35   | 0.00275 |    -    | 0.00304 |
| 36   | 0.00296 |    -    | 0.00303 |
| 37   | 0.00321 |    -    | 0.00362 |
| 38   | 0.00301 |    -    | 0.00258 |
| 39   | 0.00243 |    -    | 0.00320 |
| 40   | 0.00297 |    -    | 0.00608 |


### Modify Script?
Simply due to the speed differences, it is hard to see the speed growth of the dynamic programming version and iterative version due to the extreme cost of the recursive version. You may want to modify the python, so only the dynamic programming and iterative version runs to generate a much larger dataset. 

Either way, the goal is to experiment and see the differences in speed. 


👉🏽 **Task**: Use either the provided CSV data, or data you generate to build a line graph comparing the various speeds (note you  may need to build separate line graphs for a better comparison). Discuss with your partner. 


## Thinking Deeper
These are not the most efficient implementations! If you have time, study different ways you can improve the implementation
of pascals triangle. 


## Leet Code Practice
Take time practicing some of the past modules leet code. While you may not have time for everyone to do this, have a couple people practice "live coding". Live coding is a skill in interviews were you are asked to describe code **while** you are writing it. It can be a challenging skill, and it takes practice. I recommend that you setup a rotation of people to practice this skill within your team, ideally a couple every week. The other teams members can offer support, and then do a code review after a solution is generated. 

## 📚 Resources
* [Geek for Geeks Pascal Triangle](https://www.geeksforgeeks.org/pascal-triangle/)
* [Dynamic Programming Examples (python)](https://www.makeuseof.com/dynamic-programming-tutorial/)
* [Memoization A "complete" tutorial](https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/)
* [Leet Code - Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) -note: sort for easy ones first...


[memoization]: https://en.wikipedia.org/wiki/Memoization
[pure function]: https://en.wikipedia.org/wiki/Pure_function
[Pascal's Triangle - Numberphile]: https://www.youtube.com/watch?v=0iMtlus-afo
[Pascal's Triangle]: https://en.wikipedia.org/wiki/Pascal%27s_triangle
[Triangle Animated]: https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif