''' Ahmed Mohammed Ate/5119/09
    Amanuel Genene Ate/5124/09
    Henok Edmealem Ate/5166/09
'''
class Vertex:
    def __init__(self, node):
        self.Node = node
        self.adjacent = {}
        self.distance =0
        self.visited = 'unvisted'

    def addNext(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def getConnections(self):
        return self.adjacent.keys()

    def getVertexNode(self):
        return self.Node

    def getWeight(self, neighbor):
        if(neighbor in self.adjacent):
            return self.adjacent[neighbor]
        else:
            return None

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setvisited(self, visited):
        self.visited = visited

    def getvisited(self):
        return self.visited

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.vertDictionary = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None

    def addEdge(self, frm, to, title=0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)

        self.vertDictionary[frm].addNext(self.vertDictionary[to],title)
        self.vertDictionary[to].addNext(self.vertDictionary[frm],title)

    def getVertices(self):
        return self.vertDictionary.keys()

    def setPrevious(self, current):
        self.previous = current
