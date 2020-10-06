#coding=utf-8
"""
INSTRUÇÕES PARA EXECUÇÃO |===================================
    1) Installar python
    2) Instalar PySimpleGui: pip install --force-reinstall PySimpleGUI
        2.1) Caso não tenha instalado a versão mais recente, dar um pip upgrade
    3) Instalar opencv-pythob: pip install opencv-python
        3.1) Caso a auto instalação instale a versão menos atualizada, basta usar o pip install --upgrade pip 
    4) Instalar Pillow: pip install Pillow

""""""
INSTRUÇÕES E DOCUMENTAÇÃO |===================================
    * Values
        -> para pegar o valor do values, basta fazer: values['key']
"""

import PySimpleGUI as sg

import frameMain
import explanation
import configs

sg.theme(configs.theme)  # please make your creations colorful

layoutInicial = [
    [sg.Button('Iniciar', key='_start', size=(62, 1))],
    [sg.Button("Sobre o trabalho", size=(30, 1), key='_sobre'),
        sg.Button("Como funciona?", size=(30, 1), key='_tutorial')],
    [sg.Exit()]
]

# MAIN |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def main():
    window = sg.Window('Processamento de Imagens', layoutInicial)

    while True:
        event, values = window.read()
        # Se a janela for fechada ou o botao EXIT for apertado, ele para o programa.
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            window.close()
        if event == '_sobre':
            explanation.infoTrab()
        if event == '_tutorial':
            explanation.helpTrab()
        if event == '_start':
            window.close()
            frameMain.telaInicial()
    
if __name__ == "__main__":
    main()
