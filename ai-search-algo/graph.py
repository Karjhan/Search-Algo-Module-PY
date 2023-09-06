class Node:
    def __init__(self, data, cost = None):
        self.Data = data
        self.Neighbours = []
        self.Cost = cost

class Graph:
    def __init__(self, biDirectional = False):
        self.Nodes = []
        self.BiDirectional = biDirectional

    def AddNode(self, data, cost = None):
        newNode = Node(data, cost)
        self.Nodes.append(newNode)
        return newNode

    def AddEdge(self, startNode, endNode):
        startNode.Neighbours.append(endNode)
        if self.BiDirectional:
            endNode.Neighbours.append(startNode)