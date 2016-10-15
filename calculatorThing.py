from stack import Stack
formula = Stack()
equ = "2 2 /"
equation = equ.split(" ")
for x in equation:
    if x != "+"+"-"+"*"+"/":
        equation.push(x)
    else:
        num1 = equation.pop()
        num2 = equation.pop()
        equation.push()