from graph import Graph, Node

class Hill_Climbing:
    def __init__(self, graph, currentNode, heuristic):
        self.Graph = graph
        self.CurrentNode = currentNode
        self.Heuristic = heuristic

    def ChangeGraph(self, newGraph, newCurrentNode):
        self.Graph = newGraph
        self.CurrentNode = newCurrentNode

    def Search(self, searchValue, maxIterations = 1000, ascend = False):
        for i in range(maxIterations):
            neighbours = self.CurrentNode.Neighbours
            if len(neighbours) == 0:
                return None
            currentHeurValue = self.Heuristic(self.CurrentNode, searchValue)
            if ascend:
                bestNeighbour = max(neighbours, key = lambda x: self.Heuristic(x,searchValue))
                bestHeurValue = self.Heuristic(bestNeighbour, searchValue)
                if bestHeurValue > currentHeurValue:
                    self.CurrentNode = bestNeighbour
                else:
                    return self.CurrentNode
            else:
                bestNeighbour = min(neighbours, key = lambda x: self.Heuristic(x, searchValue))
                bestHeurValue = self.Heuristic(bestNeighbour, searchValue)
                if bestHeurValue < currentHeurValue:
                    self.CurrentNode = bestNeighbour
                else:
                    return self.CurrentNode
        return self.CurrentNode

