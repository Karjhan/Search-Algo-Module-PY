from graph import Graph, Node

class Hill_Climbing:
    def __init__(self, graph, currentNode, heuristic):
        self.Graph = graph
        self.CurrentNode = currentNode
        self.Heuristic = heuristic
        self.Path = []

    def ChangeGraph(self, newGraph, newCurrentNode):
        self.Graph = newGraph
        self.CurrentNode = newCurrentNode
        self.Path = []

    def Search(self, searchValue, maxIterations = 1000, ascend = False):
        for i in range(maxIterations):
            self.Path.append(self.CurrentNode)
            neighbours = self.CurrentNode.Neighbours
            if len(neighbours) == 0:
                return (None,[])
            currentHeurValue = self.Heuristic(self.CurrentNode, searchValue)
            if ascend:
                bestNeighbour = max(neighbours, key = lambda x: self.Heuristic(x,searchValue))
                bestHeurValue = self.Heuristic(bestNeighbour, searchValue)
                if bestHeurValue > currentHeurValue:
                    self.CurrentNode = bestNeighbour
                else:
                    return (self.CurrentNode, self.Path)
            else:
                bestNeighbour = min(neighbours, key = lambda x: self.Heuristic(x, searchValue))
                bestHeurValue = self.Heuristic(bestNeighbour, searchValue)
                if bestHeurValue < currentHeurValue:
                    self.CurrentNode = bestNeighbour
                else:
                    return (self.CurrentNode, self.Path)
        return (self.CurrentNode, self.Path)

