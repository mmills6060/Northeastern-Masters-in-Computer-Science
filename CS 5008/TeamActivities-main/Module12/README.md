# Team Activity: Exploring Dijkstra's Algorithm


In this team activity, you will explore Dijkstra's algorithm run time efficiency by comparing it against a version that uses a priority queue/heap, and a version that uses a list. You will also explore the effect of the graph density on the run time of Dijkstra's algorithm.

## Provided Files
For this team activity, we have provided three python files. 
* [graph.py](graph.py) - Contains the Graph class, which is used to represent a graph. 
* [shortest_path.py](shortest_path.py) - Contains the Dijkstra's shortest_path functions, which is used to find the shortest path between two nodes in a graph. 
* [tests.py](tests.py) - Contains tests including the ability to time the run time of the shortest_path functions.


👉🏽 **Task** 👈🏽

1. Read through the code in the provided files. Explain the various lines to each other.
   * What is a major difference between the shortest_path functions?
   * Why would this matter? (We will continue to explore this throughout the team activity)
2. In graph.py, we are creating  a small and medium graph. Take a moment and draw on the paper the visualization of the graph that those represent. 


## Visualizing Dijkstra's Algorithm

Take the graph you built for `create_small_test_graph()`, and work through manually with your group how Dijkstra's algorithm would work. As a reminder, here is Dijkstra's algorithm in more plain terms:

```python
def dijkstra(graph, start, end):
    # Initialize the distance to all nodes to infinity
    # Initialize the distance to the start node to 0
    # Initialize the previous node to None for all nodes
    # Initialize the previous node to the start node for the start node
    # Initialize the unvisited set to contain all nodes
    # While the unvisited set is not empty:
        # Find the unvisited node with the smallest distance
        # Remove the node from the unvisited set
        # For each neighbor of the node:
            # Calculate the distance to the neighbor
            # If the distance to the neighbor is less than the current distance:
                # Update the distance to the neighbor
                # Update the previous node to the current node
    # Return the distance to the end node
```
👉🏽 **Task** 👈🏽
Visualize the algorithm on the graph you drew.


You can also use the Visualization tool provided by the University of San Francisco to visualize Dijkstra's algorithm (link in the resources section). 

## Running the Code
Once you have a good understanding of the algorithm and the code, it is time to run tests. You can do this by loading
tests.py into the interactive python environment. 

You can do this via the command line with:

```bash
$ python3 -i tests.py
```

This will load the tests.py file into the interactive python environment, which in turn imports the graph.py and shortest_path.py files. From here, you can run various commands such as

```python
>>> test_small()
nodes: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] edges: [('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'E', 1), ('B', 'F', 1), ('C', 'F', 1), ('C', 'G', 1), ('D', 'G', 1), ('D', 'H', 1), ('E', 'F', 1), ('F', 'G', 1), ('G', 'H', 1)]
2
>>> test_medium()
nodes: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] edges: [('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'E', 1), ('B', 'F', 1), ('C', 'F', 1), ('C', 'G', 1), ('D', 'G', 1), ('D', 'H', 1), ('E', 'F', 1), ('F', 'G', 1), ('G', 'H', 1), ('H', 'I', 1), ('H', 'J', 1)]
3
```

More importantly, you will see two tests that use timings. 

👉🏽 **Task** 👈🏽

Build a table based on the timings for both run_timed_test, both with a mostly connected graph and a sparser graph. The N will vary greatly between the two. For mostly connected, a 500 node graph took about ~2 minutes. For a sparser 10,000 node graph took 18 seconds to run the entire function. This is the difference of $2n-1$ compared to up to $n^2$ edges. 

### Discussion  

* Take a moment to discuss the differences in speeds, what are some major points of difference between the different implementations of Dijkstra's algorithm? 
* Did the differences go away (mostly) in a certain situation? 
  * If so, what triggered that (think in respect to edges)?


## Research

👉🏽 **Task** 👈🏽

Research the time and space complexity of Dijkstra's algorithm. Between the two different implementations presented, what is the time and space complexity of each?

* In regards to time/space complexity, how did the total number of edges affect the run time of the algorithm?

## Leet Code

In your group, work on some leet code problems. Have a couple people practice "live coding" by discussing what you are doing as you write the code. Live coding is a skill in interviews were you are asked to describe code **while** you are writing it. It can be a challenging skill, and it takes practice. For your assignment you will be writing Dijsktra's algorithm in C, and you should feel free to use the python code as a reference. There are also many resources online that can help you with this. Note that for your homework, you will not need the heap version. The graphs, while sparse, will be small enough the speed difference will not be noticeable.



## 📚 Resources
* Dijkstra's Algorithm - [https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) 
* Dijkstra's Algorithm - [https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
* Dijkstra's Algorithm Visualization - [https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html)