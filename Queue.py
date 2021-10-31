''' Ahmed Mohammed Ate/5119/09
    Amanuel Genene Ate/5124/09
    Henok Edmealem Ate/5166/09
'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.last = None
        self.next = next
    def set_data(self, data):
        self.data = data
    def setLast(self, last):
        self.last = last
    def get_data(self):
        return self.data

class Queue(object):
    def __init__(self, data=None):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        self.lastNode = self.front
        self.front = Node(data, self.front)
        if self.lastNode:
            self.lastNode.setLast(self.front)
        if self.rear is None:
            self.rear = self.front
        self.size += 1
        
    def deQueue(self):
        if self.rear is None:
            raise IndexError
        result = self.rear.get_data()
        self.rear = self.rear.last
        self.size -= 1
        return result

    def size(self):
        return self.size
