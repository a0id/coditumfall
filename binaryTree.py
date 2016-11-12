from queue import Queue
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.addLeft = None
        self.addRight = None
class BinaryTree:
    def __init__(self):
        self.head = None
        self.counter = 0
    def printTree(self, curr):
        if self.left != None:
            self.printTree(self.left)
        print(curr.data)
        if self.right != None:
            self.printTree(self.right)
    def add(self, value):
        q = Queue
        if self.head != None:
            q.push(self.head)
            while True:
                temp = q.pop()
                if temp.left == None:
                    newNode = Node()
                    newNode.data = value
                    temp.left = newNode
                    break
                elif temp.right == None:
                    newNode = Node()
                    newNode.data = value
                    temp.right = newNode
                    break
                else:
                    q.push(temp.left)
                    q.push(temp.right)
        self.counter += 1