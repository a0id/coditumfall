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
                print(self.end.data)
                break
            else:
                print(node.data)
                node = node.link