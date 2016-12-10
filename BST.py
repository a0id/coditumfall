from test.test_iterlen import NoneLengthHint
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
class BST:
    def __init__(self):
        self.head = None
        self.counter = None
    def insertR(self, value, node):
        if value > node.data:
            if node.right == None:
                newNode = Node()
                newNode.data = value
                node.right = newNode
            else:
                self.insertR(value, node.right)
        else:
            if value < node.data:
                if node.left == None:
                    newNode = Node()
                    newNode.data = value
                    node.left = newNode
                else:
                    self.insertR(value, node.left)
    def insert(self, value):
        if self.head == None:
            newNode =  Node()
            newNode.data = value
            self.head = newNode
        else:
            self.insertR(value, self.head)
    def printerR(self, curr):
        if curr.left != None:
            self.printerR(curr.left)
        print(curr.data)
        if curr.right != None:
            self.printerR(curr.right)
    def printer(self):
        if self.head == None:
            print("Nothing in Tree!")
        else:
            self.printerR(self.head)
    def searchR(self, value, node):
        if value == node.data:
            return True
        elif node.right == None and node.left == None:
            return False
        else:
            b1 = self.searchR(value, node.left)
            b2 = self.searchR(value, node.right)
            return b1 or b2
    def search(self, value):
        self.searchR(value, self.head)