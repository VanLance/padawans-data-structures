from Node import Node

class BST:

    def __init__(self):
        self.root = None

    def add(self, value, node=None):
        
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return
        
        if not node:
            node = self.root

        if new_node.value < node.value:
            if not node.left:
                node.left = new_node
                return
            self.add(value, node.left)
            return
        
        if new_node.value > node.value:
            if not node.right:
                node.right = new_node
                return
            self.add(value, node.right)
            return

    def get_min_value(self, node = None):
        if not node:
            node = self.root
        if not node:
            return
        
        if node.left:
            return self.get_min_value(node.left)
        
        return node.value

    def get_max_value(self):
        node = self.root
        if not node:
            return
        while node.right:
            node = node.right
        return node.value
    
    def sorted_log(self, node=None):
        if not self.root:
            return
        if not node:
            node = self.root
        if node.left:
            self.sorted_log(node.left)
        print(node.value)
        if node.right:
            self.sorted_log(node.right)

bst = BST()



bst.add(100)
bst.add(88)
bst.add(95)
bst.add(120)
bst.add(110)
bst.add(180)
bst.add(50)
bst.add(200)

# print(bst.root.right.right)

# print(bst.get_min_value())
# print(bst.get_max_value())

bst.sorted_log()