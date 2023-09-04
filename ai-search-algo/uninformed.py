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

