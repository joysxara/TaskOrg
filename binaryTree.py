# Joy Cho 4/12/2019 10:02PM
# Bitcamp 2019
# Workflow Automation: Prioritize
# Binary Tree Data Structure

#include everything

class Node:

    def __init__(self, task, data):
        self.left = None
        self.right = None
        self.data = data
        self.task = task

    def insert(self, task, data): #compare the new value wiht the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(task, data)
                else:
                    self.left.insert(task, data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(task, data)
                else:
                    self.right.insert(task, data)
            elif data == self.data:
                self.right.insert(task, data)

        else:
            self.data = data
            self.task = task

    # This returns the size of the binary tree -- for debugging purposes
    def getSize(self):
        leftSize = self.left.getSize() if self.left else 0
        rightSize = self.right.getSize() if self.right else 0
        return leftSize + 1 + rightSize

    #Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, self.task)
        if self.right:
            self.right.PrintTree()
