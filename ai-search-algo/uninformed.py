from graph import Graph, Node
from collections import deque

class Breadth_First:
    def __init__(self, graph=None):
        self.Graph = graph

    def ChangeGraph(self, newGraph):
        self.Graph = newGraph

    def Represent(self, startingNode):
        visited = set()
        queue = deque()
        queue.append(startingNode)
        visited.add(startingNode)
        while(queue):
            currentNode = queue.popleft()
            print("Node: {nodeName} - Value: {nodeValue}".format(nodeName=self.Graph.Nodes.index(currentNode), nodeValue=currentNode.Data))
            for neighbour in currentNode.Neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

    def Search(self, startingNode, value):
        visited = set()
        queue = deque()
        queue.append(startingNode)
        visited.add(startingNode)
        while (queue):
            currentNode = queue.popleft()
            if currentNode.Data == value:
                return (currentNode, visited)
            for neighbour in currentNode.Neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)

class Bidirectional:
    def __init__(self, graph = None, mode1 = "BFS", mode2 = "BFS"):
        self.Graph = graph
        self.FirstSearch = mode1
        self.SecondSearch = mode2

    def ChangeGraph(self, newGraph):
        self.Graph = newGraph

    def ChangeFirstSearch(self, newMode):
        if newMode in ["BFS", "DFS", "UCS"]:
            self.FirstSearch = newMode

    def ChangeSecondSearch(self, newMode):
        if newMode in ["BFS", "DFS", "UCS"]:
            self.SecondSearch = newMode

    def Search(self, startNode, goalNode):
        if self.FirstSearch == "BFS" and self.SecondSearch == "BFS":
            visitedStart = set()
            visitedGoal = set()
            queueStart = deque()
            queueGoal = deque()
            queueStart.append(startNode)
            queueGoal.append(goalNode)
            visitedStart.add(startNode)
            visitedGoal.add(goalNode)
            while queueStart and queueGoal:
                # Search from the start node
                current_start = queueStart.popleft()
                for neighbor_start in current_start.Neighbours:
                    if neighbor_start not in visitedStart:
                        queueStart.append(neighbor_start)
                        visitedStart.add(neighbor_start)
                        if neighbor_start in visitedGoal:
                            return visitedGoal.union(visitedStart);
                # Search from the goal node
                current_goal = queueGoal.popleft()
                for neighbor_goal in current_goal.Neighbours:
                    if neighbor_goal not in visitedGoal:
                        queueGoal.append(neighbor_goal)
                        visitedGoal.add(neighbor_goal)
                        if neighbor_goal in visitedStart:
                            return visitedGoal.union(visitedStart);
            return set()

class Depth_First:
    def __init__(self, graph=None):
        self.Graph = graph

    def ChangeGraph(self, newGraph):
        self.Graph = newGraph

    def Represent(self, startNode):
        visited = set()
        self._dfs_recursive(startNode, visited)

    def Search(self, startNode, searchValue):
        visited = set()
        self._dfs_recursive(startNode, visited, searchValue)

    def _dfs_recursive(self, currentNode, visited, searchValue=None):
        if currentNode not in visited:
            if searchValue is None:
                print("Node: {nodeName} - Value: {nodeValue}".format(nodeName=self.Graph.Nodes.index(currentNode), nodeValue=currentNode.Data))
            if searchValue is not None and currentNode.Data == searchValue:
                return (currentNode, visited)
            visited.add(currentNode)
            for neighbour in currentNode.Neighbours:
                self._dfs_recursive(neighbour, visited)

