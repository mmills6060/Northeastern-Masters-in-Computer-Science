
from typing import Any
import random


def create_small_test_graph() -> 'graph':
    """Creates a small undirected test graph"""
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    edges = [('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'E', 1), ('B', 'F', 1), ('C', 'F', 1), ('C', 'G', 1), ('D', 'G', 1), ('D', 'H', 1), ('E', 'F', 1), ('F', 'G', 1), ('G', 'H', 1)]
    return graph(nodes, edges)


def create_medium_test_graph() -> 'graph':
    """Creates a medium undirected test graph"""
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    edges = [('A', 'B', 1), ('A', 'C', 1), ('A', 'D', 1), ('B', 'E', 1), ('B', 'F', 1), ('C', 'F', 1), ('C', 'G', 1), ('D', 'G', 1), ('D', 'H', 1), ('E', 'F', 1), ('F', 'G', 1), ('G', 'H', 1), ('H', 'I', 1), ('H', 'J', 1)]
    return graph(nodes, edges)


def create_an_N_test_graph(N: int, min=1, max=1) -> 'graph':
    """Creates a test undirected graph of N vertices and a random number of edges between 1 and N^2 
    (so the graph is almost always connected)"""
    nodes = [str(i) for i in range(N)]
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < 0.5:
                edges.append((nodes[i], nodes[j], random.randint(min, max)))
    return graph(nodes, edges)

def create_an_N_test_graph_smaller(N: int, min=1, max=1) -> 'graph':
    """Creates an undirected graph of N vertices and 2*N-1 edges"""
    nodes = [str(i) for i in range(N)]
    edges = []
    for i in range(N - 1):
        if i < N - 2:
            edges.append((nodes[i], nodes[i + 2], random.randint(min, max)))
        edges.append((nodes[i], nodes[i + 1], random.randint(min, max)))
    return graph(nodes, edges)



class graph():
    """A graph for use in shortest path algorithms (see shortest_path.py)
    """
    def __init__(self, nodes, edges) -> None:
        """Initializes the graph

        Args:
            nodes (list): list of nodes
            edges (list): list of edges
        """
        self.nodes = nodes
        self.edges = edges
        self.adj = {node: [] for node in nodes}
        for edge in edges:
            self.adj[edge[0]].append(edge[1])

    def neighbors(self, node) ->list[Any]:
        """Returns the neighbors of a node

        Args:
            node (any): the node

        Returns:
            list: list of neighbors
        """
        return self.adj[node]

    def cost(self, node1, node2) -> Any:
        """Returns the cost of the edge between two nodes

        Args:
            node1 (any): the first node
            node2 (any): the second node

        Returns:
            int: the cost of the edge
        """
        for edge in self.edges:
            if edge[0] == node1 and edge[1] == node2:
                return edge[2]
        return 0

    def __str__(self) -> str:
        """Returns a string representation of the graph

        Returns:
            str: the string representation
        """
        return f'nodes: {self.nodes} edges: {self.edges}'
    

