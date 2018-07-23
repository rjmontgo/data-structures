class Node:

    def __init__(self, left=None, right=None, data=None):
        # initialize instance variables
        self.left = left
        self.right = right
        self.data = data

class BST:

    def __init__(self):
        # initialize pointer to root of tree
        self.root = None



    def add(self, num):
        if self.root is None:
            self.root = Node(data=num)
        else:
            node = self.__searchHelper(num, self.root)

            if node.data == num:
                raise ValueError('Cannot add a value that\'s already there.')
            elif num > node.data:
                node.right = Node(data=num)
            else:
                node.left = Node(data=num)


    def __searchHelper(self, num, node):
        # find the insertion point.
        # Check base case
        if num == node.data:
            return node
        elif num < node.data:
            # if there is no right child return the current node.
            if node.left is None:
                return node
            # else make recursive call on the left child.
            return self.__searchHelper(num, node.left)
        elif num > node.data:
            # If there is no left child return the current node.
            if node.right is None:
                return node
            # else make recursive call on the right child.
            return self.__searchHelper(num, node.right)

    def search(self, num):
        if self.root is None:
            raise ValueError('No Root')
        return self.__searchHelper(num, self.root)


    def remove(self, num):
        raise ValueError('Not yet implemented')
