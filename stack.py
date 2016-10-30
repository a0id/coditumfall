from linkedlist import LinkedList
class Stack():
    def __init__(self):
        self.ll = LinkedList()
    def push(self, value):
        self.ll.insert(0, value)
    def pop(self):
        returner = self.ll.peek()
        self.ll.remove(0)
        return returner
    def peek(self):
        self.ll.peek()
    def view(self):
        self.ll.simplePrinter()