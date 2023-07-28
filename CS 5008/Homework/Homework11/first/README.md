# Finding The Shortest Distance

Name:

Github Account name: 

Link to Assignment on Github: (copy and paste the link to your assignment repo here)

How many hours did it take you to complete this assignment (estimate)? 

Did you collaborate with any other students/TAs/Professors? If so, tell us who and in what capacity.  
- one per row, add more if needed


Did you use any external resources (you do not have to cite in class material)? (Cite them below)  
- one row per resource


(Optional) What was your favorite part of the assignment? 

(Optional) How would you improve the assignment? 

## Further Thinking Questions 

1. What is the difference between a directed and undirected graph?

2. What is the Big O of Dijkstra's algorithm.... 
   * Assuming you used an array (or list) to store the vertices.
   * Assuming you used a heap / priority queue to store the vertices.

3. Explain in your own words what that means for larger graphs when trying to find the shortest distance. 

4. For this assignment, you didn't need the most "efficient" set of data structures (for example, a heap wasn't required). However, think on the scale of google/apple maps - they have to deal with millions of vertices and edges. What data structures would you use to store the graph? Why? Somethings to consider - would you be able to store the entire graph at a time? Could you break it up into smaller pieces? How would you do that? Would there be advantages to caching/memoization of paths? You are free to explore your thoughts on this subject/reflect on various ideas. Other than a realization of some scalability of problems, there isn't a wrong answer. 


5. Related to shortest distance, is a problem called the "messenger" or "traveling sales person" problem commonly abbreviated to TSP. This problem is to find the shortest path that visits **every** vertex in a graph. Another way to look at it, is you are an delivery driver, and you have a series of packages to deliver. Can you find an optimal path for your deliveries that minimizes the total distance traveled? Imagine if you had 5 stops. How many different paths are there?  There are 120 possible paths to look at! (assuming fully connected routes). 
   * How many possible paths are there if you have 6 stops?
   * How many possible paths are there if you have 10 stops?
6. What type of growth is this problem? 
7. Take some time to research TSP problems. It falls under a certain classification of problems? What is it? 
8. Provide some examples of fields / problems that use TSP.



---
Note: we are having you explore TSP, so you can see the terms used for problem classification that you will also explore in more depth in 5800. You will not be asked to know about TSP outside of this assignment or even problem classification. Computer Science is often about dealing with problems considered "too hard" or "impossible", and finding ways to make them possible! As such, knowing topics such as N, NP, NP-Complete, etc. is important to understand the limits (to break).
