from graph import *
from shortest_path import *

import timeit


def test_small():
    ## a quick test
    small_graph = create_small_test_graph()
    print(small_graph)
    print(shortest_path_dijkstra(small_graph, 'A', 'H'))
  
def test_medium():
    ## a quick test
    medium_graph = create_medium_test_graph()
    print(medium_graph)
    print(shortest_path_dijkstra(medium_graph, 'A', 'J'))


def test_large():
    ## a quick test
    large_graph = create_an_N_test_graph(20)
    print(large_graph)
    print(shortest_path_dijkstra(large_graph, '0', '19'))
 


def run_timed_test(N: int, mostly_connected: bool = False):
    """Runs a timed test on a graph of N nodes"""
    if mostly_connected:
        test_graph = create_an_N_test_graph(N)
    else:
        test_graph = create_an_N_test_graph_smaller(N)
    print('Testing graph with', N, 'nodes')
    print('Dijkstra\'s algorithm')
    print(timeit.timeit(lambda: shortest_path_dijkstra(test_graph, '0', str(N - 1)), number=1))
    print('Dijkstra\'s algorithm with heap')
    print(timeit.timeit(lambda: shortest_path_dijkstra_heap(test_graph, '0', str(N - 1)), number=1))
