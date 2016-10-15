from stack import Stack
stack = Stack()
while True:
    choice = input("push, pop, peek, or view? ")
    if choice == "push":
        stack.push()
    elif choice == "pop":
        stack.pop()
    elif choice == "peak":
        print(stack.peek())
    elif choice == "view":
        stack.view()