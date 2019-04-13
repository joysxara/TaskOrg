# Joy Cho 4/12/2019 10:02PM
# Bitcamp 2019
# Workflow Automation: Prioritize
# Binary Tree Data Structure

#include TestGUI.py //check syntax!! how do I include JZ's GUI?
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

        else:
            self.data = data
            self.task = task

    #Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data, self.task)
        if self.right:
            self.right.PrintTree()

#TEST: Prompt user give a value betwen 1~10
print('Give task and priority (task priority):') #ask for the first number
print('If you\'re done, type in (done -1)')
task, value = input().split()
root = Node(task, int(value))

while value != '-1':
    print('Give task and priority (task priority): ')
    task, value = input().split()
    if value == '-1':
        break
    else:
        root.insert(task, int(value))

print('terminate')

root.PrintTree()
        


        
