from linkedlist import LinkedList
class Stack():
    def __init__(self):
        self.ll = LinkedList()
    def push(self):
        value = input("Enter an item: ")
        self.ll.insert(0, value)
    def pop(self):
        self.ll.peek()
        self.ll.remove(0)
    def peek(self):
        self.ll.peek()
    def view(self):
        self.ll.printer()
