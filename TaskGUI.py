import PySimpleGUI as sg

# GUI for Task Organizer

layout = [
            [sg.Text('Task Organizer')],
            [sg.Text('Task Name: ', size=(15,1)), sg.InputText()],
            [sg.Text('Priority: ', size=(15,1)), sg.InputCombo(['LOW', 'MEDIUM', 'HIGH'], size=(20,3))],
            [sg.Button('Add'), sg.Button('Done')]
        ]

window = sg.Window('Task Organizer App').Layout(layout)

while True:
    event, values = window.Read()
    if event is not None:
        print(values[0], values[1])
    if event == 'Done':
        break

window.Close()
