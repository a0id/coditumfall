from linkedlist import LinkedList
pwlist = LinkedList()
while True:
    x = input("[V]iew, [A]ppend, [I]nsert, or [R]emove? ")
    if x == "V" or x == "v":
        pwlist.printer()
    elif x == "A" or x == "a":
        pwlist.append(input("Enter data: "))
    elif x == "I" or x == "i":
        pwlist.insert(eval(input("Enter place number: ")), input("Enter data: "))
    elif x == "R" or x == "r":
        pwlist.remove(eval(input("Enter place number: ")))