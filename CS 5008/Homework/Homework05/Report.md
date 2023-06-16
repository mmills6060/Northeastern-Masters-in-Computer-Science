# Sort Analysis Data

## Results Table
Make sure to go out to at least 100,000 (more are welcome), and you have 10 different values (more welcome). You are welcome to go farther, but given 100,000 can take about 20 seconds using a selection sort on a fast desktop computer, and 200,000 took 77 seconds, you start having to wait much longer the more 0s you add. However, to build a clearer line, you will want more data points, and you will find merge and quick are able to handle higher numbers easier (but at a cost you will explore below). 

You are free to write a script to run the program and build your table (then copy that table built into the markdown). If you do that, please include the script into the repo.  Note: merge and quick sorts are going to be explored in the team activity for Module 06. You can start on it now, but welcome to wait.
0 == bubble, 1 == selection, 2 == insertion, 3== merge, 4 == quick
### Table [^note]
| N     | Bubble            | Selection        | Insertion        | Merge            | Quick            |
| 10000 | 0.174081 seconds  | 0.089113 seconds | 0.000007 seconds |                  | 0.000776 seconds |
| 20000 | 0.758874 seconds  | 0.347674 seconds | 0.000010 seconds |                  | 0.001684 seconds |
| 30000 | 1.764095 seconds  | 0.763727 seconds | 0.000007 second  |                  | 0.002720 seconds|
| 40000 | 3.276420 seconds  |1.350319 seconds  | 0.000009 seconds |                  | 0.003708 seconds |
| 50000 | 5.056356 seconds  | 2.109140 seconds | 0.000009 seconds |                  | 0.004597 seconds |
| 60000 | 7.406755 seconds  | 3.034919 seconds | 0.000011 seconds |                  | 0.005646 seconds |
| 70000 | 10.124643 seconds | 4.129134 seconds | 0.000009 seconds |                  | 0.006617 seconds |
| 80000 | 13.236667 seconds | 5.396813 seconds | 0.000009 seconds |                  | 0.007764 seconds |
| 90000 | 16.768206 seconds | 6.838159 seconds | 0.000008 seconds | 0.012594 seconds | 0.008990 seconds |
| 100000| 20.748810 seconds | 8.469072 seconds | 0.000008 seconds | 0.013537 seconds | 0.010962 seconds |
## BigO Analysis  / Questions

### 1. Build a line chart
Build a line chart using your favorite program. Your X axis will be N increasing, and your Y access will be the numbers for each type of sort. This will create something similar to the graph in the instructions, though it won't be as smooth. Due to speed differences, you may need to break up the $O(\log n)$ and $O(n^2)$ into different charts.

Include the image in your markdown. As a reminder, you save the image in your repo, and use [image markdown].



### 2. Convinced?
Given the direction of the line chart, are you "convinced" of the complexity of each of the sorts? Why or why not?

I am convinced to a certain extent. I ran the script a few times and it seemed to change by a few seconds each time. I also ran the script on windows and linux, and linux seemed to be faster. I would say that the average is consistent with what they should be in terms of their complexity. 
### 3. Big O
Build another table that presents the best, worst, and average case for Bubble, Selection, Insertion, Merge, and Quick. You are free to use resources for this, but please reference them if you do. 
|                | Best Case       | Worst Case      | Average Case    |
|----------------|-----------------|-----------------|-----------------|
| Bubble Sort    | O(n)            | O(n^2)          | O(n^2)          |
| Selection Sort | O(n^2)          | O(n^2)          | O(n^2)          |
| Insertion Sort | O(n)            | O(n^2)          | O(n^2)          |
| Merge Sort     | O(n log n)      | O(n log n)      | O(n log n)      |

https://iq.opengenus.org/time-complexity-of-selection-sort/
https://iq.opengenus.org/time-and-space-complexity-of-merge-sort-on-linked-list/
https://iq.opengenus.org/insertion-sort/
https://iq.opengenus.org/bubble-sort-in-c/
#### 3.2 Worst Case
Provide example of arrays that generate _worst_ case for Bubble, Selection, Insertion, Merge Sorts
|                | Best Case       | Worst Case      | Average Case    |
|----------------|-----------------|-----------------|-----------------|
| Bubble Sort    | sorted in order | reverse order   | Not Ordered     |
| Selection Sort | sorted in order | reverse order   | Not Ordered     |
| Insertion Sort | sorted in order | reverse order   | Not Ordered     |
| Merge Sort     | N/A            | N/A              | N/A             |


#### 3.3 Best Case
Provide example of arrays that generate _best_ case for Bubble, Selection, Insertion, Merge Sorts 

mentioned above

#### 3.4 Memory Considerations
Order the various sorts based on which take up the most memory when sorting to the least memory. You may have to research this, and include the mathematical notation. 
merge, quick, selection, bubble, insertion
### 4. Growth of Functions
Give the following values, place them correctly into *six* categories. Use the bullets, and feel free to cut and paste the full LatexMath we used to generate them.  

$n^2$  
$n!$  
$n\log_2n$  
$5n^2+5n$  
$10000$  
$3n$    
$100$  
$2^n$  
$100n$  
$2^{(n-1)}$
#### Categories
* $10000$ , $100$
* $3n$, $100n$
* $n^2$, $5n^2+5n$
* $n\log_2n$
*$2^n$, $2^{(n-1)}$
* $n!$

### 5. Growth of Function Language

Pair the following terms with the correct function in the table. 
* Constant, Logarithmic, Linear, Quadratic, Cubic, Exponential, Factorial

| Big $O$     |  Name       |
| ------      | ------      |
| $O(n^3)$    |  cubic      |
| $O(1)$      | constant    |
| $O(n)$      |  linear     |
| $O(\log_2n)$|  logarithmic|
| $O(n^2)$    |  quadratic  |
| $O(n!)$     |  factorial  |
| $O(2^n)$    |  exponential|



### 6. Stable vs Unstable
Look up stability as it refers to sorting. In your own words, describe one sort that is stable and one sort that isn't stable  

https://www.freecodecamp.org/news/stability-in-sorting-algorithms-a-treatment-of-equality-fa3140a5a539/#:~:text=A%20stable%20sorting%20algorithm%20maintains,after%20the%20collection%20is%20sorted.

merge sort - stable (maintains order of elements)
selection sort - unstable (does not maintain order of elements)


### 6.2 When stability is needed?
Explain in your own words a case in which you will want a stable algorithm over an unstable. Include an example. 

An example of when stability is needed could be a databse that stores all of the times of runners during a marathon. This particular list sorts from first to last place. Stability would be needed in this situation because we need to maintain the order of elements. 
### 7. Gold Thief

You are planning a heist to steal a rare coin that weighs 1.0001 ounces. The problem is that the rare coin was mixed with a bunch of counter fit coins. You know the counter fit coins only weight 1.0000 ounce each. There are in total 250 coins.  You have a simple balance scale where the coins can be weighed against each other. Hint: don't think about all the coins at once, but how you can break it up into even(ish) piles. 

My immediate answer would be to divide the coins in half, put half one one side of the scale and the other half on the other. I would then determine what side is heavier. I would take the heavier side and then divide that in half and weigh both halves. I would repeat this process until I have found the rare coin. 
#### 7.1 Algorithm
Describe an algorithm that will help you find the coin. We encourage you to use pseudo-code, but not required.
I believe what I described is called a binary search algorithm. 
#### 7.2 Time Complexity
What is the average time complexity of your algorithm? 
logarithmic time complexity
### 8. Modern Sort
Sorting algorithms are still being studied today. They often include a statistical analysis of data before sorting. This next question will require some research, as it isn't included in class content. When you call `sort()` or `sorted()` in Python 3.6+, what sort is it using? 


Timsort. I remember this from CS5001

#### 8.1 Visualize
Find a graphic / visualiation (can be a youtube video) that demonstrates the sort in action. 
https://www.youtube.com/watch?v=NVIjHj-lrT4
#### 8.2 Big O
Give the worst and best case time-complexity, and examples that would generate them. 
best case - O(n)
worst case - O(n log n)
<hr>

## References
Add your references here. A good reference includes an inline citation, such as [1] , and then down in your references section, you include the full details of the reference. Computer Science research often uses [IEEE] or [ACM Reference format].

[1] Reference info, date, etc.

Stability in Sorting Algorithms: A Treatment of Equality. (n.d.). FreeCodeCamp. Retrieved from https://www.freecodecamp.org/news/stability-in-sorting-algorithms-a-treatment-of-equality-fa3140a5a539/#:~:text=A%20stable%20sorting%20algorithm%20maintains,after%20the%20collection%20is%20sorted.

Time Complexity of Selection Sort. (n.d.). OpenGenus IQ. Retrieved from https://iq.opengenus.org/time-complexity-of-selection-sort/

Time and Space Complexity of Merge Sort on Linked List. (n.d.). OpenGenus IQ. Retrieved from https://iq.opengenus.org/time-and-space-complexity-of-merge-sort-on-linked-list/

Insertion Sort. (n.d.). OpenGenus IQ. Retrieved from https://iq.opengenus.org/insertion-sort/

Bubble Sort in C. (n.d.). OpenGenus IQ. Retrieved from https://iq.opengenus.org/bubble-sort-in-c/


## Footnotes:
[^note]: You will want at least 10 different N values, probably more to see the curve for Merge and Quick. If bubble, selection, and insertion start to take more than a  minute, you can say $> 60s$. 


<!-- links moved to bottom for easier reading in plain text (btw, this a comment that doesn't show in the webpage generated-->
[image markdown]: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images

[ACM Reference Format]: https://www.acm.org/publications/authors/reference-formatting
[IEEE]: https://www.ieee.org/content/dam/ieee-org/ieee/web/org/conferences/style_references_manual.pdf