# HW README

Name: Michael Mills

Github Account name:mmills6060 

Link to Assignment on Github: (copy and paste the link to your assignment repo here)

How many hours did it take you to complete this assignment (estimate)? 
5 hours
Did you collaborate with any other students/TAs/Professors? If so, tell us who and in what capacity.  
- one per row, add more if needed
I don't not collaborate with anyone on this project

Did you use any external resources (you do not have to cite in class material)? (Cite them below)  
- one row per resource
I did not use any external resources

(Optional) What was your favorite part of the assignment? 

(Optional) How would you improve the assignment? 

## Understanding Time Complexity

1. Using a markdown table and markdown/latex math, show the BigO for Arrays, Singly Linked Lists, Doubly Linked Lists (so total of 3). For the columns, you will look at the Worst Case Time Complexity for Access, Search/Find, Insertion, and Deletion. 
| Data Structure       | Access | Search/Find | Insertion | Deletion |
|----------------------|--------|-------------|-----------|----------|
| Array                | O(1)   | O(n)        | O(n)      | O(n)     |
| Singly Linked List   | O(n)   | O(n)        | O(1)      | O(n)     |
| Doubly Linked List   | O(n)   | O(n)        | O(1)      | O(1)     |

2. Usually for singly and doubly linked lists, we reference both the head and tail for speed considerations. What would be the cost if you only had your head referenced, and you wanted to push to the tail of either?  $O(?)$
my assumption would be that we would only have the ability to use the head in order to get to the last node. With that being said, we would need to go all the way to the head, which would be a cost of O(n), before we are able to add something to the tail. insertion is 0(1).
3. Name an example where an array is better than a linked list, and an example where a linked list is better than an array. Make sure to reference the big O as part of your reasoning. 
I suppose whether or not an array or linked list would be a better implementation would primarily depend on whether or not elements would need to be randomly accessed. For example, I suppose that a linked list would be a good implementation if you are looking to develop a queue of tasks that are sent to a server for the server to process. It doesn't really matter what is 5th or 6th on the list, since the only thing that needs to be processed is the item at the beginning of the queue. Alternatively, an array would be a better implementation if there is an application that frequently needs to access pieces of information randomly. An example of this would be accessing information from a databse that contains all of the available items in a store. The request for a specific item is completely random, so an array would make more sense here as it would probably be much faster. 

Note: Make sure look at your finished markdown in the browser hosted on github or via a markdown preview extension. To confirm the notation is showing up properly. Double check the resources section in the instructions if you need help with markdown tables. 