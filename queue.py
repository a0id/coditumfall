class Queue():
    def __init__(self):
        self.values = []
    def push(self, value):
        self.values.append(value)
    def pop(self):
        #temp = self.values[0]
        return self.values.pop(0)
        
    def printer(self):
        for x in range(len(self.values)):
            print(self.values[x])