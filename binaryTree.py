# Joy Cho 4/12/2019 10:02PM
# Bitcamp 2019
# Workflow Automation: Prioritize
# Binary Tree Data Structure

#include TestGUI.py //check syntax!! how do I include JZ's GUI?
#include everything

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data): #compare the new value wiht the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    #Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

#TEST: Prompt user give a value betwen 1~10
print('Put in a value between 1~10: ') #ask for the first number
value = input()
root = Node(int(value))

while value != '-1':
    print('Put in a value between 1~10: ')
    value = input()
    if value == '-1':
        break
    else:
        root.insert(int(value))

print('terminate')

root.PrintTree()
        


        
