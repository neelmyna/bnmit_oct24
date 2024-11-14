import sys

class Node:
    def __init__(self):
        self.left  = None
        self.data  = 0
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        print('An empty BST is created')

    def add_node(self, node_data):
        new_node = Node() # created a new node
        new_node.data = node_data

        if self.root is None:
            self.root = new_node
            return
        
        temp1 = self.root
        temp2 = None

        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node

    def get_height(self, root):
        if root == None:
            return 0 # When tree is empty
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(left_height, right_height) + 1
    
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end='  ')
        self.inorder(root.right)

def create_tree(bst):
    number_of_nodes = int(input('Enter number of nodes: '))
    node_values = []
    print(f'Enter {number_of_nodes} values of the nodes')
    for i in range(number_of_nodes):
        node_values.append(int(input()))
        bst.add_node(node_values[-1])

def run_app(bst):
    create_tree(b
                ++---+  +-+-st)
    print('The BST is')
    bst.inorder(bst.root)
    print('\nHeight of the BST is', bst.get_height(bst.root))

bst = BST()
run_app(bst)