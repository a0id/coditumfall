class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        self.counter = 0
    def append(self, data):
        node = Node(data)
        if self.counter == 0:
            self.head = node
            self.end = node
            self.counter+=1
        self.end.link = node #actually add it
        self.end = node
        self.counter+=1
    def insert(self, place, data):
        if self.counter == 0:
            self.append(data)
        newNode = Node(data)
        node = self.head
        for x in range(place-1):
            node = node.link
        newNode.link = node.link
        node.link = newNode
        self.counter+=1
    def printer(self):
        node = self.head
        for x in range(self.counter):
            if node == self.end:
                print("["+str(x)+"]"+self.end.data)
                break
            else:
                print("["+str(x)+"]"+node.data)
                #ATTEMPTING TO SHOW DATA TYPE WHEN PRINTING
                node = node.link
    def remove(self, place):
        if place == 0:
            self.head = self.head.link
            self.counter-=1
        elif place == self.counter-1:
            node = self.head
            for x in range(place):
                node = node.link
            self.head = node
        else:
            node = self.head
            for x in range(place-1):
                node = node.link
            for x in range(place):
                rmv = node.link
            node.link = rmv.link
            self.counter-=1