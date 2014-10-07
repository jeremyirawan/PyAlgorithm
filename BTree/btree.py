#title           : btree.py
#description     : The following code shows how it is to construct a binary tree using 2 classes namely Node and Tree
#author          : Ramadhi Irawan
#date            : 2014-10-07
#version         : 0.2
#usage           : python btree.py
#notes           : Information about binary tree: http://en.wikipedia.org/wiki/Binary_tree
#python_version  : 2.7.x

__author__ = 'Ramadhi Irawan'


class Node:
    left, right, data = None, None, 0

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BTree:

    def __init__(self):
        self.root = None # Initializes root node

    def createNode(self, data):
        return Node(data)

    def insert(self, root, data):
        if root == None:
            return self.createNode(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root

    def lookup(self, root, target):
        if root == None:
            return 0
        else:
            if target == root.data:
                return 1
            else:
                if target < root.data:
                    return self.lookup(root.left, target)
                else:
                    return self.lookup(root.right, target)

    def findMin(self, root):
        while(root.left != None):
            root = root.left
        return root.data

    def findDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.findDepth(root.left)
            rdepth = self.findDepth(root.right)

            return max(ldepth, rdepth) + 1

    def findSize(self, root):
        if root == None:
            return 0
        else:
            return self.findSize(root.left) + 1 + self.findSize(root.right)

    def printTree(self, root):
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print root.data
            self.printTree(root.right)

    def printTreeReverse(self, root):
        if root == None:
            pass
        else:
            self.printTreeReverse(root.right)
            print root.data
            self.printTreeReverse(root.left)

# Initializes tree
my_tree = BTree()
root = my_tree.createNode(0)

# Ask user to insert 5 nodes
for i in range(0, 5):
    data = int(raw_input("Insert node value (%d): " % i))
    my_tree.insert(root, data)
print

# Print Tree
my_tree.printTree(root)
print
my_tree.printTreeReverse(root)
print

# Ask user what value to search from within the tree
data = int(raw_input("Insert a value to search: "))
if my_tree.lookup(root, data):
    print "Node Found."
else:
    print "Node not found."

print my_tree.findMin(root) # Find minimum value within the tree
print my_tree.findDepth(root) # Find tree depth
print my_tree.findSize(root) # Find maximum value within the tree