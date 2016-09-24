from linkedlist import LinkedList
pwlist = LinkedList()
while True:
    x = input("[V]iew, [S]tring append, [A]ppend, [I]nsert, or [R]emove? ")
    if x == "V" or x == "v":
        pwlist.printer()
    elif x == "S" or x == "s":
        pwlist.append(input("Enter data: "))
    elif x == "A" or x == "a":
        dataType = input("Append [B]oolean, [S]tring, [I]nteger, or [L]ist? ")
        if dataType == "B" or dataType == "b":
            pwlist.append(bool(input("Enter 'True' or enter 'False': ")))
        elif dataType == "S" or dataType == "s":
            pwlist.append(input("Enter a string: "))
        elif dataType == "I" or dataType == "i":
            pwlist.append(eval(input("Enter an integer: ")))
        elif dataType == "L" or dataType == "l":
            print("Format: 'item1,item2,item3,item4'")
            preList = input("Enter list: ")
            newList = preList.split(",")
            pwlist.append(newList)
    elif x == "I" or x == "i":
        pwlist.insert(eval(input("Enter place number: ")), input("Enter data: "))
    elif x == "R" or x == "r":
        pwlist.remove(eval(input("Enter place number: ")))
#UNABLE TO INSERT HEAD OR END, ONLY IN MIDDLE NODES