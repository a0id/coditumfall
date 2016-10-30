from stack import Stack
formula = Stack()
equ = input("Enter equation in postfix: ")
equation = equ.split(" ")
for x in equation:
    if x != "+" and x != "-" and x != "*" and x != "/":
        formula.push(x)
        formula.view()
    else:
        right = formula.pop()
        left = formula.pop()
        if x == "+":
            formula.push(int(left)+int(right))
        elif x == "-":
            formula.push(int(left)-int(right))
        elif x == "-":
            formula.push(int(left)-int(right))
        elif x == "/":
            formula.push(int(left)/int(right))
        formula.view()
formula.view()