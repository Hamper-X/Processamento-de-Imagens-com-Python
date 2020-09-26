import PySimpleGUI as sg

layout = [
            [sg.Text('1. '), sg.In(key=1)],
            [sg.Text('2. '), sg.In(key=2)],
            [sg.Text('3. '), sg.In(key=3)],
            [sg.Text('4. '), sg.In(key=4)],
            [sg.Text('5. '), sg.In(key=5)],
            [sg.Button('Save'), sg.Button('Exit')]
         ]


window = sg.Window('My Title').Layout(layout)
event, values = window.read()