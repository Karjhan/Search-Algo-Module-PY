class Node:
    def __init__(self, data):
        self.Data = data
        self.Neighbours = []

class Graph:
    def __init__(self):
        self.Nodes = []

    def AddNode(self, data):
        newNode = Node(data)
        self.Nodes.append(newNode)
        return newNode

    def AddEdge(self, startNode, endNode):
        startNode.Neighbours.append(endNode)