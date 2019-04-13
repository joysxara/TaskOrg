import PySimpleGUI as sg
from binaryTree import Node

# GUI for Task Organizer

layout = [
            [sg.Text('Task Organizer')],
            [sg.Text('Task Name: ', size=(15,1)), sg.InputText()],
            [sg.Text('Priority: ', size=(15,1)), sg.InputCombo(['LOW', 'MEDIUM', 'HIGH'], size=(20,3))],
            [sg.Button('Add'), sg.Button('Done')]
        ]

window = sg.Window('Task Organizer App').Layout(layout)
root = Node(None, None)

dict = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}

while True:
    event, values = window.Read()
    if event is not None and event == 'Add':
        print(event, dict[values[1]])
        root.insert(values[0], dict[values[1]])
    if event == 'Done' or event is None:
        print('SIZE:')
        print(root.getSize())
        print('TREE:')
        root.PrintTree()
        break

window.Close()
