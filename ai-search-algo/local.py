from graph import Graph, Node
import random
import math

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

class Simulated_Annealing:
    def __init__(self, graph, currentNode, initialTemp, coolingRate):
        self.Graph = graph
        self.CurrentNode = currentNode
        self.BestNode = currentNode
        self.BestCost = currentNode.Cost
        self.Temperature = initialTemp
        self.CoolingRate = coolingRate
        self.Path = []
    def ChangeGraph(self, newGraph, newCurrentNode):
        self.Graph = newGraph
        self.CurrentNode = newCurrentNode
        self.Path = []

    def ChangeTemperature(self, newTemp):
        self.Temperature = newTemp

    def ChangeCoolingRate(self, newCoolingRate):
        self.CoolingRate = newCoolingRate

    def _accept_neighbour(self, neighbour):
        if neighbour.Cost < self.CurrentNode.Cost:
            return True
        probability = math.exp((self.CurrentNode.Cost - neighbour.Cost) / self.temperature)
        return random.random() < probability

    def AnnealSearch(self, maxIterations):
        for i in range(maxIterations):
            self.Path.append(self.CurrentNode)
            neighbours = self.CurrentNode.Neighbours
            if len(neighbours) == 0:
                return (None, [])
            nextNeighbour = random.choice(neighbours)
            if self._accept_neighbour(nextNeighbour):
                self.CurrentNode = nextNeighbour
                if self.CurrentNode.Cost < self.BestCost:
                    self.BestNode = self.CurrentNode
                    self.BestCost = self.CurrentNode.Cost
            self.Temperature *= self.CoolingRate
        return (self.BestNode, self.Path)


