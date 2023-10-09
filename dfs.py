#
# dfs.py
#
# This file provides a function implementing depth-first search for a
# route-finding problem. Various search utilities from "route.py" are
# used in this function, including the classes RouteProblem, Node, and
# Frontier.
# 
# YOUR COMMENTS INCLUDING CITATIONS AND ACKNOWLEDGMENTS
#
# Gustavo Castañeda - 09/21/2023
#


from route import Node
from route import Frontier


def DFS(problem, repeat_check=False):
    """Perform depth-first search to solve the given route finding
    problem, returning a solution node in the search tree, corresponding
    to the goal location, if a solution is found. Only perform repeated
    state checking if the provided boolean argument is true."""

    # PLACE YOUR CODE HERE
    initial_state_node = Node(problem.start)
    #
    if problem.is_goal(initial_state_node):
        return initial_state_node

    frontier = Frontier(initial_state_node, True)
    reached_set = set(initial_state_node.loc)

    while frontier.is_empty() == False:
        popped_node = frontier.pop()
        if problem.is_goal(popped_node.loc) == True:
            return popped_node

        expand_node = popped_node.expand(problem)
        for i in expand_node:
            if repeat_check:
                current = i.loc
                if current not in reached_set:
                    reached_set.add(current)
                    frontier.add(i)
                else:
                    reached_set.add(i.loc)
    return None
