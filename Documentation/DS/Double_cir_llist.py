class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def checkNode(head, lastHead):
    currentNode = head
    lastNode = lastHead
    
    while currentNode:
        print(currentNode.data, "->", end=" ")
        currentNode = currentNode.next
    print("None", '\n')

    # Find the previous node
    print("Previous of:", lastNode.data, "->", end=" ")
    lastNode = lastNode.prev
    return lastNode.data

# Assign node value
n1 = Node(4)
n2 = Node(12)
n3 = Node(24)
n4 = Node(55)

# Assign pointer for node 1
n1.next = n2
n1.prev = n4

# Assign pointer for node 2
n2.next = n3
n2.prev = n1

# Assign pointer for node 3
n3.next = n4
n3.prev = n2

# Assign pointer for node 4
n4.next = None
n4.prev = n3

# Test
print(checkNode(n1, n1))
