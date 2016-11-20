from binaryTree import BinaryTree as charlie
louis = charlie()
louis.add(0)
louis.add(1)
louis.add(2)
louis.add(3)
louis.add(4)
louis.add(5)
louis.add(6)
louis.add(7)
louis.add(8)
if louis.head.data != 0:
    print("Rip")
if louis.head.left.data != 1:
    print("rip")
if louis.head.right.data != 2:
    print("ripper")
if louis.head.left.left.data != 3:
    print("overwatch")
louis.printTree()