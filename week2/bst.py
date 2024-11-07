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

    def add_node(self, dummy_arg):
        new_node = Node() # created a new node
        new_node.data = int(input('Enter data of new node: '))

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

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end='  ')
        self.inorder(root.right)

    def preorder(self, root):
        if root == None:
            return
        print(root.data, end='  ')
        self.preorder(root.left)        
        self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end='  ')

class Menu:
    def __init__(self):
        self.bst = BST()

    def exit_program(self, dummy_arg):
        sys.exit('End of program')

    def invalid_choice(self, dummy_arg):
        print('invalid choice entered')

    def get_menu(self):
        menu = {
            1 : self.bst.add_node,
            2 : self.bst.inorder,
            3 : self.bst.preorder,
            4 : self.bst.postorder,
            5 : self.exit_program
        }
        return menu
    
    def run_app(self):
        while True:
            print('\n1:AddNode 2:InOrder 3:PreOrder 4:PostOrder 5:Exit. Your choice: ')
            choice = int(input())
            # self.get_menu().get(choice, self.invalid_choice)(self.bst.root)
            if choice in [2, 3, 4] and self.bst.root is None:
                print('Tree is empty')
                continue # go to the next iteration
            menu = self.get_menu()
            menu.get(choice, self.invalid_choice)(self.bst.root)

menu = Menu()
menu.run_app()