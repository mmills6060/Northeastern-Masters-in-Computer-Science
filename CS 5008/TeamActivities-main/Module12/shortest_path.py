import heapq
import sys

def shortest_path_dijkstra_heap(graph, start, goal) -> float:
    """Runs djikstra's algorithm to find the shortest path from start to goal.
    
    a priority queue is used to keep track of the node with the smallest distance.

    returns the distance to the goal node.

    """
    # initialize the distance to all nodes to infinity
    dist = {node: float('inf') for node in graph.nodes}
    dist[start] = 0
    # initialize the queue with the start node
    queue = []
    heapq.heappush(queue, (0, start))
    # loop until the queue is empty
    while queue:
       d, u = heapq.heappop(queue)
         # loop through the neighbors of u
       for v in graph.neighbors(u):
            # calculate the distance to v
            alt = d + graph.cost(u, v)
            # if the distance is less than the current distance
            if alt < dist[v]:
                # update the distance
                dist[v] = alt
                # add v to the queue
                heapq.heappush(queue, (alt, v))

 
    return dist[goal]

def minDistance(dist, sptSet, vertices) -> int:
    """Returns the node with the smallest distance index.
    """
    # Initialize minimum distance for next node
    min = sys.maxsize
    min_index = vertices[0]
 
    for u in vertices:
        if dist[u] < min and sptSet[u] == False:
            min = dist[u]
            min_index = u
 
    return min_index

def shortest_path_dijkstra(graph, start, goal) -> float:
    """Runs djikstra's algorithm to find the shortest path from start to goal.
    
    uses minDistance helper function, which returns the node with the smallest distance index.
    runs a V^2 time complexity and is not efficient for large graphs.

    returns the distance to the goal node.
    """
    # initialize the distance to all nodes to infinity
    dist = {node: float('inf') for node in graph.nodes}
    dist[start] = 0
    # initialize the shortest path tree
    sptSet = {node: False for node in graph.nodes}
    # loop through all the nodes
    for i in range(len(graph.nodes)):
        # get the node with the smallest distance
        u = minDistance(dist, sptSet, graph.nodes)
        # add the node to the shortest path tree
        sptSet[u] = True
        # loop through the neighbors of u
        for v in graph.neighbors(u):
            # calculate the distance to v
            alt = dist[u] + graph.cost(u, v)
            # if the distance is less than the current distance
            if alt < dist[v]:
                # update the distance
                dist[v] = alt
    return dist[goal]
