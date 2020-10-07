import PySimpleGUI as sg

import file_controller

def infoTrab():
    layoutInformacao = [
        [sg.Text(file_controller.TextInfoTrab())],
        [sg.Button("Entendido !", key='_voltar')]
    ]
    
    window = sg.Window('Informações sobre o trabalho', layoutInformacao)
    event, values = window.read()
    if event == '_voltar':
        window.close()


def helpTrab():
    layoutHelp = [
        [sg.Text(file_controller.TextHelpTrab())],
        [sg.Button("Entendido !", key='_voltar')]
    ]

    window = sg.Window('Informações sobre o trabalho', layoutHelp)
    event, values = window.read()
    if event == '_voltar':
        window.close()