# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Michael Mills
* **GitHub Repo**: [link to github repo with this report]
* **Semester**: Summer 2023
* **Languages Used**: c, python

## Overview
In the algorithm implemented in C, we have a struct. We also have methods that satisfy each requirement. The main class essentially prints the Fibonacci series and its length as well as creates instances of each class. 

As for the Python implementation, there are three different algorithms, iterative, recursive, and dynamic. The iterative function calculates the Fibonacci iteratively. This means that the a list of instructions are run over and over until a specific problem is solved. The recursive function solves the problem recursively. Recursion means that a specific problem will be solved by breaking it down into smaller and smalller pieces. The dynamic algorithm calculates the fibonacci dynamically. This means that a specific problem is broken down into smaller subproblems, and solving each of the sub problems until the problem is solved. 

## Empirical Data & Discussion 

I would say that the timings of the algorithms are exactly what I would expect. For the recursive algorithm, as n increases, the number of recursive calls will increase, which will ultimately cause the algorithm to run longer, the more it calls its function. As for the dynamic algorithm, since it uses a concept called memoization to store previously calculated data, it should in theory take not as long as a recursive algorithm. As for the iterative algorithm, it looks to be done correctly. My only concern is that from what I remember in previous classes, iterative fibbonacci has "1" as the value for the first two values of n. In my case, it is true for only one value of n. I will reevaluate this in testing. 
## Language Analysis

For my second language, I wanted to pick a language where I didn't have to worry about memory. I also wanted a language that is just simply easier to write. To me, it also seems like python consistenetly takes less lines of code in order to achieve the same solution. I have programmed in all of the languages above in the past, and I would say that Python is one of those languages that I can say "hey, I wonder if this will work," writing down some random syntax that I haven't looked up anywhere, and it will actually work. C# is in second place, but I would say Python is definitely in first place when it comes to this. I appreciate the flexibility of Python and the ability to remain creative in the way that I solve problems with Python, as opposed to languages such as Java, which will tell me that what im trying to do is illegal and that I am not allowed to do certain things. Python remains flexible in the way that I want to construct my code.  

### Language 1: C

When I was implementing C, I didn't really have a lot of problems. I suppose my first problem was the fact that I didn't implement several options of what is actually printed. With that being said, I had to rewrite that portion of the code. I suppose another thing that I was thinking about was where I should free memory. 
### Language 2: Python

When I was implementing Python, I also didn't have a lot of problems with this either. In fact, I found it much easier to implement even though it is a completely different language than what I have been recently using. The same thing occured with the Python implementation, where I initially didnt create functionality for different things to be printed. 


### Comparison and Discussion Between Experiences

I would say that there is a vast difference between Python and C. In my mind, I would say that Python is good for productivity. What I mean by this is that it is a good language for someone who is looking to accomplish as much as possible in a certain amount of time. The time it takes to process the code in Python may take a little bit longer, but it was able to be done in half the amount of time. As for C, I would say that this is a good language for someone who wants to build an application that is required to be as fast as possible. For example, maybe a high frequency trading algorithm on wall street, where it is imperative that your algorithm is just a few miliseconds faster than the one across the street. 

Another observation that I see is that as computers become more and more powerful, there will be less and less of a need for C. This is because computers will get to a point where they are so fast that the benefit of manually managing memory will be close to nonexistent. It almost already is. I can see how C was tremendously helpful twenty years ago, looking at my Dell XP in my basement. 

## Conclusions / Reflection

In conclusion, I would say that this is probably one of my favorite projects I have done so far. I think learning and understanding what language should be used in what circumstance is an incredibly valuable trait to have. Ultimately, I think this is one of my favorite aspects of computer science. I can imagine these types of conversations happening in very high level management positions, where one decides what type of language to use and why. I am sure that the person who makes this type of decision has knowledge about ALL languages and the pros and cons of ALL languages, and is able to confidently make a reccomendation on which language would be best for which project. 

