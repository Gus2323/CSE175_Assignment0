#
# bfs.py
#
# This file provides a function implementing breadth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
#
# YOUR COMMENTS INCLUDING CITATIONS AND ACKNOWLEDGMENTS
# My TA Rebecca helped explain the sudo code
# Gustavo Castañeda - 09/21/2023
#


from route import Node
from route import Frontier


def BFS(problem, repeat_check=False):
    """Perform breadth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    initial_state_node = Node(problem.start)

    if initial_state_node == problem.goal:
        return initial_state_node

    frontier = Frontier(initial_state_node, True)
    reached_set = set(initial_state_node.loc)

    while frontier.is_empty() == False:
        popped_node = frontier.pop()
        if problem.is_goal(popped_node.loc) == True:
            return popped_node

        expand_node = popped_node.expand(problem)
        for i in expand_node:
            frontier.add(i)
            if repeat_check == False:
                    reached_set.add(i.loc)
            else:
                reached_set.add(i)

    return None