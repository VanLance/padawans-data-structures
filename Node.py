class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node: {self.value}>'

""" node1 = Node("mon")
node2 = Node("Tue")
node3 = Node("Wed")


node1.right = node2
node2.right = node3
print(node1.value)
print(node1.right.right)

 """