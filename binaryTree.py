# Joy Cho 4/12/2019 10:02PM
# Bitcamp 2019
# Workflow Automation: Prioritize
# Binary Tree Data Structure

class Node:

    def __init__(self, task, data, dueDate):
        self.left = None
        self.right = None
        self.data = data
        self.task = task
        self.dueDate = dueDate

    def insert(self, task, data, dueDate): #compare the new value wiht the parent node
        newSum = data + dueDate
        oldSum = self.data + self.dueDate

        if self.data:
            if oldSum > newSum:
                if self.left is None:
                    self.left = Node(task, data, dueDate)
                else:
                    self.left.insert(task, data, dueDate)
            elif oldSum < newSum:
                if self.right is None:
                    self.right = Node(task, data, dueDate)
                else:
                    self.right.insert(task, data, dueDate)
            elif oldSum == newSum:
                self.right.insert(task, data, dueDate)

        else:
            self.data = data
            self.task = task
            self.dueDate = dueDate
        
        return self

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
