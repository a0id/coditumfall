from queue import Queue
q = Queue()
while True:
    what = input("Push Pop Print Peek or Clear\n")
    if what == "push":
        q.push(input("Enter Value: "))
    elif what == "pop":
        q.pop()
    elif what == "print":
        q.printer()
    elif what == "clear":
        q.clear()