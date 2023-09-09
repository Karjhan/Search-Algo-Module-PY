from graph import Node, Graph
import heapq

class Greedy_Best_First:
    def __init__(self, graph, heuristic):
        self.Graph = graph
        self.Heuristic = heuristic

    def Search(self, startNode, searchValue):
        goalNode = self._find_node_by_data(searchValue)
        if startNode is None or goalNode is None:
            return (None, [])
        path = []
        frontier = [(self.Heuristic(startNode, goalNode), startNode)]
        visited = set()
        while frontier:
            heuristicValue, currentNode = heapq.heappop(frontier)
            if len(path) > 0:
                while currentNode not in path[-1].Neighbours:
                    path.pop()
            path.append(currentNode)
            if currentNode == goalNode:
                return (currentNode, path)
            visited.add(currentNode)
            for neighbour in currentNode.Neighbours:
                if neighbour not in visited:
                    heapq.heappush(frontier, (self.Heuristic(neighbour, goalNode), neighbour))

    def _find_node_by_data(self, data):
        for node in self.Graph.Nodes:
            if node.Data == data:
                return node
        return None

class Astar:
    def __init__(self, graph, heuristic):
        self.Graph = graph
        self.Heuristic = heuristic

    def Search(self, startNode, searchValue):
        if startNode is None:
            return (None, [])
        frontier = [(self.Heuristic(startNode, searchValue), [startNode])]
        visited = set()
        while frontier:
            costHeurValue, currentPath = heapq.heappop(frontier)
            if currentPath[-1].Data == searchValue:
                return (currentPath[-1], currentPath)
            visited.add(currentPath[-1])
            for neighbour in currentPath[-1].Neighbours:
                if neighbour not in visited:
                    newPath = currentPath + [neighbour]
                    newPathCost = sum(map(lambda x:x.Cost, newPath)) + self.Heuristic(neighbour, searchValue)
                    heapq.heappush(frontier, (newPathCost, newPath))