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
            [sg.Output(size=(80,10))]
        ]

window = sg.Window('Task Organizer App').Layout(layout)
root = Node(None, None)

#dict = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}

while True:
    event, values = window.Read()
    if event is None:
        break   
    elif event == 'Add':
        print(values[0], values[1])
        root.insert(values[0], int(values[1]))
    elif event == 'Done':
        print('SIZE:')
        print(root.getSize())
        print('TREE:')
        root.PrintTree()
    #elif event == 'Clear': #clear the console print screen
        

window.Close()
