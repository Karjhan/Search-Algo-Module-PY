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
        frontier = [(self.Heuristic(startNode, goalNode), startNode)]
        visited = set()
        while frontier:
            heuristicValue, currentNode = heapq.heappop(frontier)
            if currentNode == goalNode:
                path = self._construct_path(startNode,goalNode)
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

    def _construct_path(self, startNode, goalNode):
        path = []
        currentNode = goalNode
        while currentNode != startNode:
            path.insert(0, currentNode)
            currentNode = self._find_best_neighbor(currentNode, goalNode)
        path.insert(0, startNode)
        return path

    def _find_best_neighbor(self, node, goalNode):
        return min(node.Neighbours, key=lambda neighbor: self.Heuristic(neighbor, goalNode))

