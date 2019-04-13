#test for binary tree:
"""
class Node:

    def __init__(self,data):

        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)

root = Node(10)

root.PrintTree()
"""
class Node:

    def __init__(self, task, data):

        self.left = None
        self.right = None
        self.data = data # this will hold the number value of the priority
        self.task = task # this will hold the name of the task

    def insert(self, task, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, task)
                else:
                    self.left.insert(data, task)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, task)
                else:
                    self.right.insert(data, task)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
    #prompt user to add in a value
print('Give task and priority (task, priority): ')
#how can I divide the task and priority value using the comma?
#what does my data structure look like? Am I going to have separate memory for task and value?
# OR will it be input = {task, value}?
value = input()
root = Node(int(value))

while value != '-1':
    print('Give task and priority (task, priority): ')
    value = input()
    if value == '-1':
        break
    else:
        root.insert(int(value))

print('terminate')

'''
if value == '0':
    print("terminate")
else:
    root.insert(int(value))
'''

root.PrintTree()
