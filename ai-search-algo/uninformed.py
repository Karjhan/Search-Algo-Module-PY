from graph import Graph, Node
from collections import deque
import heapq

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

    def RepresentDepthLimit(self, startNode, depthLimit, startDepth = 0):
        visited = set()
        self._dfs_recursive_limit(startNode, visited, depthLimit, startDepth)

    def SearchDepthLimit(self, startNode, searchValue, depthLimit, startDepth):
        visited = set()
        self._dfs_recursive_limit(startNode, visited, depthLimit, startDepth, searchValue)

    def SearchIterativeDeepening(self, startNode, searchValue):
        maxDepth = 0
        while True:
            visited = set()
            result = self._iddfs_recursive(startNode, visited, maxDepth, searchValue)
            if result is not None:
                return result
            maxDepth += 1

    def _dfs_recursive(self, currentNode, visited, searchValue=None):
        if currentNode not in visited:
            if searchValue is None:
                print("Node: {nodeName} - Value: {nodeValue}".format(nodeName=self.Graph.Nodes.index(currentNode), nodeValue=currentNode.Data))
            if searchValue is not None and currentNode.Data == searchValue:
                return (currentNode, visited)
            visited.add(currentNode)
            for neighbour in currentNode.Neighbours:
                self._dfs_recursive(neighbour, visited, searchValue)

    def _dfs_recursive_limit(self, currentNode, visited, depthLimit, currentLimit=0, searchValue=None):
        if currentLimit > depthLimit:
            return None
        if currentNode not in visited:
            if searchValue is None:
                print("Node: {nodeName} - Value: {nodeValue}".format(nodeName=self.Graph.Nodes.index(currentNode), nodeValue=currentNode.Data))
            if searchValue is not None and currentNode.Data == searchValue:
                return (currentNode, visited)
            visited.add(currentNode)
            for neighbour in currentNode.Neighbours:
                self._dfs_recursive(neighbour, visited, depthLimit, currentLimit + 1, searchValue)

    def _iddfs_recursive(self, currentNode, visited, depthLimit, searchValue):
        if depthLimit == 0:
            if currentNode.Data == searchValue:
                return (currentNode, visited)
            else:
                return None
        if currentNode not in visited:
            visited.add(currentNode)
            for neighbour in currentNode.Neighbours:
                result = self._iddfs_recursive(neighbour, visited, depthLimit - 1, searchValue)
                if result is not None:
                    return result
        # Goal node not found within depth limit
        return None

class Uniform_Cost:
    def __init__(self, graph):
        self.Graph = graph

    def Search(self, startNode, searchValue):
        goalNodes = self._find_node_by_data(searchValue)
        if len(goalNodes) == 0:
            return None
        visited = set()
        frontier = [(0, startNode)]
        result = []
        for goalNode in goalNodes:
            found = False
            while frontier:
                cost, currentNode = heapq.heappop(frontier)
                if currentNode == goalNode:
                    found = True
                    path = self._construct_path(startNode, goalNode)
                    totalCost = 0
                    for node in path:
                        totalCost += node.Cost
                    result.append((path, totalCost))
                    break
                visited.add(currentNode)
                for neighbour in currentNode.Neighbours:
                    if neighbour not in visited:
                        newCost = cost + neighbour.Cost
                        heapq.heappush(frontier, (newCost, neighbour))
            if found == False:  # Path not found
                result.append(([], float('inf')))
        result = sorted(result, key=lambda tup: tup[1])
        if len(result[0][0]) > 0:
            return result[0]
        return None

    def _find_node_by_data(self, data):
        result = []
        for node in self.Graph.Nodes:
            if node.Data == data:
                result.append(node)
        return result
    def _construct_path(self, startNode, goalNode):
        path = []
        currentNode = goalNode
        while currentNode != startNode:
            path.insert(0, currentNode)
            currentNode = self._find_lowest_cost_neighbor(currentNode)
        path.insert(0, startNode)
        return path
    def _find_lowest_cost_neighbor(self, node):
        lowestCost = float('inf')
        lowestCostNeighbour = None
        for neighbour in node.Neighbours:
            if neighbour.Cost < lowestCost:
                lowestCost = neighbour.Cost
                lowestCostNeighbour = neighbour
        return lowestCostNeighbour