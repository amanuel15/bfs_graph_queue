''' Ahmed Mohammed Ate/5119/09
    Amanuel Genene Ate/5124/09
    Henok Edmealem Ate/5166/09
'''
import time

from Queue import Queue
from Graph import *
def BFS(Gra, frAct, scAct):
    start = Gra.getVertex(frAct)
    start.setDistance(0)
    distance = 0
    start.setPrevious(None)
    Que = Queue()
    Que.enQueue(start)
    t1 = time.time()
    while (Que.size != 0):
        currentVert = Que.deQueue()
        for nbr in currentVert.getConnections(): 
            if (nbr.getvisited() == 'unvisted'):
                nbr.setvisited('visited')
                nbr.setDistance(currentVert.getDistance() + 1) 
                if(nbr == scAct):
                    distance = nbr.getDistance()
                    print("time to search",time.time()-t1)
                    print("Distance is: ",distance)
                nbr.setPrevious(currentVert)
                Que.enQueue(nbr)
    if(distance == 0):
        print("time to search",time.time()-t1)
        print("Distance is 0")
    return distance

def Distance(Gra, frAct, seAct):
    
    if(Gra.getVertex(frAct) == None or Gra.getVertex(seAct) == None):
        print("No such an actor!")
        return
    for v in Gra:
        if (v.getVertexNode() == frAct):
            BFS(Gra, v.getVertexNode(), Gra.getVertex(seAct))
    
            
def  readFile():
    enterFile = open("cast.txt","r",encoding="utf-8")
    fileLines = enterFile.readlines()
    grph = Graph()
    t1 = time.time()
    for line in fileLines:
        line.strip()
        film = line.split("/")
        
        for j in range(1, len(film)): 
            if grph.getVertex(film[j]) == None: 
                grph.addVertex(film[j])
                              
        for l in range(1, len(film)):
            for m in range(l+1, len(film)): 
                grph.addEdge(film[l], film[m], film[0])
    print(time.time()-t1,"graph build time")
    return grph

def test():
    grph = readFile()
    Distance(grph, "Beumer, Loek","Bacon, Kevin")

    
test()
