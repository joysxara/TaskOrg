import PySimpleGUI as sg
import sys
from binaryTree import Node

# GUI for Task Organizer

layout = [
            [sg.Text('Task Organizer')],
            [sg.Text('Task Name: ', size=(15,1)), sg.InputText(do_not_clear=False)],
            #do_not_clear=False clears the input box everytime event is True
            [sg.Text('Priority: ', size=(15,1)), sg.InputText(do_not_clear=False)],
            [sg.Button('Add'), sg.Button('Done'), sg.Button('Clear')],
        ]

mainWindow = sg.Window('Task Organizer App').Layout(layout)
treeWindow_active = False
root = Node(None, None)

treeData = sg.TreeData()

def insertTree(root):
    if root.left:
        insertTree(root.left)
    treeData.Insert("", root.task, root.task, root.data)      
    if root.right:
        insertTree(root.right)

while True:
    event, values = mainWindow.Read()
    if event is None:
        mainWindow.Close()
        break   
    elif event == 'Add':
        root.insert(values[0], int(values[1]))
    elif event == 'Done' and not treeWindow_active:
        treeWindow_active = True
        mainWindow.Hide()
        insertTree(root)
        layout2 = [[sg.Text('Tasks')], [sg.Tree(data = treeData, headings=['PRIORITY'],change_submits=True, auto_size_columns=True, key='_TREE_', show_expanded=True)]]

        treeWindow = sg.Window('Result').Layout(layout2)

        while True:
            event2, values2 = treeWindow.Read()
            
            if event is None:
                treeWindow.Close()
                treeWindow_active = False
                mainWindow.UnHide()
                break
            

