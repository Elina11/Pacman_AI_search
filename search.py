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
Elina Suslova
CSC665 SFSU Spring 2018
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


def graphSearch(problem, fringe):
    """
    graphSearch algorithm implementation which takes certain datastucture as a parameter
    and performs search through the graph based on datastructure specifics.
    This function checks for start node of a graph and by going through nodes finds path solution to the
    goal node. All visited nodes are put into set and when new node is examined program checks if this node
    was visited previously, which helps to avoid cycles in graph. This function is underlying for graph
    search algorithms implemented in this class.
    :param problem: graph to examine
    :param fringe: datastructure used to examine graph and get to the goal
    :return: path from start node to the goal node
    """

    def goalnode(node):
        return problem.isGoalState(node)

    startstate  = problem.getStartState()


    fringe.push((startstate,[]))


    try:
        startstate.__hash__()
        visited = set()
    except:
        visited = list()


    while not fringe.isEmpty():
        (node,path) = fringe.pop()

        if goalnode(node):
            return path
        #visited.add(node)

        if node not in visited:
            visited.add(node)
            successor = problem.getSuccessors(node)
            for state, action, cost in successor:
                if state not in visited:
                    fringe.push((state, path + [action]))

    return []



     #util.raiseNotDefined()


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    :param problem: graph to examine
    :return: call to graphSearch function with problem and datastructure parameters
    """

    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())

    return graphSearch(problem, util.Stack())



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.
    :param problem: graph to examine
    :return: call to graphSearch function with problem and datastructure parameters

    """
    "*** YOUR CODE HERE ***"
    return graphSearch(problem,util.Queue())

def uniformCostSearch(problem):
    """Search the node of least total cost first.
    :param problem: graph to examine
    :return: :return: path from start node to the goal node

    """
    "*** YOUR CODE HERE ***"



    def goalnode(node):
        return problem.isGoalState(node)

    startstate  = problem.getStartState()

    queue = util.PriorityQueue()
    queue.push((startstate,[]),0)


    try:
        startstate.__hash__()
        visited = set()
    except:
        visited = list()


    while not queue.isEmpty():
        (node,path) = queue.pop()

        if goalnode(node):
            return path
        #visited.add(node)

        if node not in visited:
            visited.add(node)
            successor = problem.getSuccessors(node)
            for state, action, cost in successor:
                if state not in visited:
                    cost = problem.getCostOfActions(path+[action])
                    queue.push((state, path + [action]),cost)

    return []





def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.
    :param problem: graph to examine
    :param heuristic: heuristics of the path
    :return: :return: path from start node to the goal node

    """
    "*** YOUR CODE HERE ***"

    def goalnode(node):
        return problem.isGoalState(node)

    startstate = problem.getStartState()

    queue = util.PriorityQueue()
    queue.push((startstate, []), 0)

    try:
        startstate.__hash__()
        visited = set()
    except:
        visited = list()

    while not queue.isEmpty():
        (node, path) = queue.pop()

        if goalnode(node):
            return path
        # visited.add(node)

        if node not in visited:
            visited.add(node)
            successor = problem.getSuccessors(node)
            for state, action, cost in successor:
                if state not in visited:
                    cost = problem.getCostOfActions(path+[action])
                    queue.push((state, path + [action]), cost+heuristic(state,problem))

    return []








# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

