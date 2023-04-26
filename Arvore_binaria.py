class Node(object):
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

node1 = Node(99)
node2 = Node(87)
node3 = Node(89)
node4 = Node(77)
node5 = Node(79)
node6 = Node(81)
node7 = Node(84)
node8 = Node(53)
node9 = Node(58)
node10 = Node(64)
node11 = Node(61)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7
node4.leftChild = node8
node4.rightChild = node9
node5.leftChild = node10
node5.rightChild = node11
node6.leftChild = None
node6.rightChild = None
node7.leftChild = None
node7.rightChild = None
node8.leftChild = None
node8.rightChild = None
node9.leftChild = None
node9.rightChild = None
node10.leftChild = None
node10.rightChild = None
node11.leftChild = None
node11.rightChild = None

print("Nó 1:")
print(node1.data)
print("Filho da esquerda do NODE1:")
print(node1.leftChild.data)
print("Filho da direita do NODE1:")
print(node1.rightChild.data)

print("Nó 2:")
print(node2.data)
print("Filho da esquerda do NODE2:")
print(node2.leftChild.data)
print("Filho da direita do NODE2:")
print(node2.rightChild.data)

print("Nó 3:")
print(node3.data)
print("Filho da esquerda do NODE3:")
print(node3.leftChild.data)
print("Filho da direita do NODE3:")
print(node3.rightChild.data)

print("Nó 4:")
print(node4.data)
print("Filho da esquerda do NODE4:")
print(node4.leftChild.data)
print("Filho da direita do NODE4:")
print(node4.rightChild.data)

print("Nó 5:")
print(node5.data)
print("Filho da esquerda do NODE5:")
print(node5.leftChild.data)
print("Filho da direita do NODE5:")
print(node5.rightChild.data)

print("Nó 6:")
print(node6.data)
print("Filho da esquerda do NODE6:")
print(node6.leftChild)
print("Filho da direita do NODE6:")
print(node6.rightChild)

print("Nó 7:")
print(node7.data)
print("Filho da esquerda do NODE7:")
print(node7.leftChild)
print("Filho da direita do NODE7:")
print(node7.rightChild)

print("Nó 8:")
print(node8.data)
print("Filho da esquerda do NODE8:")
print(node8.leftChild)
print("Filho da direita do NODE8:")
print(node8.rightChild)

print("Nó 9:")
print(node9.data)
print("Filho da esquerda do NODE9:")
print(node9.leftChild)
print("Filho da direita do NODE9:")
print(node9.rightChild)

print("Nó 10:")
print(node10.data)
print("Filho da esquerda do NODE10:")
print(node10.leftChild)
print("Filho da direita do NODE10:")
print(node10.rightChild)

print("Nó 11:")
print(node11.data)
print("Filho da esquerda do NODE11:")
print(node11.leftChild)
print("Filho da direita do NODE11:")
print(node11.rightChild)