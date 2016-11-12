class Queue():
    def __init__(self):
        self.values = []
    def push(self, value):
        self.values.append(value)
    def pop(self):
        self.values.pop()
    def printer(self):
        for x in range(len(self.values)):
            print(self.values[x])