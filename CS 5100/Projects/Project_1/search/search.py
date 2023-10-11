# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    # Initialize an empty stack to store nodes to explore
    stack = util.Stack()

    # Initialize a set to keep track of visited states
    visited = set()

    # Push the start state onto the stack as a tuple (state, actions)
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        # Pop the top state and its corresponding actions from the stack
        state, actions = stack.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions  # Return the list of actions to reach the goal

        # Mark the current state as visited
        visited.add(state)

        # Get successor states and actions
        successors = problem.getSuccessors(state)

        for next_state, action, _ in successors:
            if next_state not in visited:
                # Push unvisited successor states onto the stack
                stack.push((next_state, actions + [action]))

    return []  # Return an empty list if no solution is found

def breadthFirstSearch(problem):
    # create fringe to store nodes
    fringe = util.Queue()
    # track visited nodes
    visited = []
    # push initial state to fringe
    fringe.push((problem.getStartState(), [], 1))
    
    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]
        actions = node[1]
        # goal check
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.append(state)
            # visit child nodes
            successors = problem.getSuccessors(state)
            for child in successors:
                # store state, action and cost = 1
                child_state = child[0]
                child_action = child[1]
                if child_state not in visited:
                    # add child nodes
                    child_action = actions + [child_action]
                    fringe.push((child_state, child_action, 1))
def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    # Initialize a priority queue to store nodes to explore
    priority_queue = util.PriorityQueue()

    # Initialize a dictionary to keep track of the cost to reach each state
    cost_to_state = {}

    # Push the start state onto the priority queue with cost 0
    start_state = problem.getStartState()
    priority_queue.push((start_state, []), 0)
    cost_to_state[start_state] = 0  # Initialize cost for the start state

    while not priority_queue.isEmpty():
        # Dequeue the front state and its corresponding actions and cost
        state, actions = priority_queue.pop()
        state_cost = cost_to_state[state]

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions  # Return the list of actions to reach the goal

        # Get successor states, actions, and costs
        successors = problem.getSuccessors(state)

        for next_state, action, step_cost in successors:
            total_cost = state_cost + step_cost

            if next_state not in cost_to_state or total_cost < cost_to_state[next_state]:
                # Update the cost to reach the next state if it's lower
                cost_to_state[next_state] = total_cost

                # Push unvisited successor states onto the priority queue with their costs
                priority_queue.push((next_state, actions + [action]), total_cost)

    return []  # Return an empty list if no solution is found

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "Search the node that has the lowest combined cost and heuristic first."
    from util import PriorityQueue

    # Creates an empty PriorityQueue.
    open_list = PriorityQueue()

    visited_list = []
    path = []
    priority = 0    # Initializes the priority to 0.

    start_position = problem.getStartState()

    # Pushes the start position to the PriorityQueue.
    open_list.push((start_position, path), priority)

    while not open_list.isEmpty():

        current_node = open_list.pop()
        position = current_node[0]
        path = current_node[1]

        # Returns the final path if the current position is goal.
        if problem.isGoalState(position):
            return path

        # Pushes the current position to the visited list if it is not visited.
        if position not in visited_list:
            visited_list.append(position)

            # Gets successors of the current node.
            successors = problem.getSuccessors(position)

            # Pushes the current node's successors to the PriorityQueue if they are not visited.
            for item in successors:
                if item[0] not in visited_list:
                    new_position = item[0]
                    new_path = path + [item[1]]

                    # Updates priority of the successor using f(n) function.

                    """ g(n): Current cost from start state to the current position. """
                    g = problem.getCostOfActions(new_path)

                    """ h(n): Estimate of the lowest cost from the current position to the goal state. """
                    h = heuristic(new_position, problem)

                    """ f(n): Estimate of the lowest cost of the solution path
                              from start state to the goal state passing through the current position """
                    f = g + h

                    new_priority = f
                    open_list.push((new_position, new_path), new_priority)

    util.raiseNotDefined()
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
