"""
INSTRUÇÕES PARA EXECUÇÃO |===================================
    1) Installar python
    2) Instalar PySimpleGui: pip install --force-reinstall PySimpleGUI
        2.1) Caso não tenha instalado a versão mais recente, dar um pip upgrade

""""""
INSTRUÇÕES E DOCUMENTAÇÃO |===================================
    * Values
        -> para pegar o valor do values, basta fazer: values['key']
"""

import PySimpleGUI as sg
import algorithms

sg.theme('Dark Blue 3')  # please make your windows colorful

image_col_layout = [
    [sg.Text('Imagem',pad=((220, 150),(20,20)))],
    [sg.Image(size=(500,500), background_color='white')]
]

image_col = sg.Column(image_col_layout, element_justification='left')

elements_col_size=(50,0)
zoom_buttons_size=(24,0)

elements_col_layout = [
    [sg.Text('| Menu |', size=elements_col_size)],
    # Fazer um leitor que permitar pegar apenas imagem
    [sg.FileBrowse('Ler diretorio de imagem', size=elements_col_size, key="op_diretorio")],
    [sg.Button('Selecionar características', size=elements_col_size, key="op_selecionar")],
    [sg.Button('Treinar classificador', size=elements_col_size, key="op_treinar")],
    [sg.Button('Abrir Imagem', size=elements_col_size, key="op_abrirImg")],
    [sg.Button('Marcar região de interesse', size=elements_col_size, key="op_marcar")],
    [sg.Button('Calcular e exibir características', size=elements_col_size, key="op_calcular")],
    [sg.Button('Classificar imagem/regiao', size=elements_col_size, key="op_classificar")],
    [sg.Button('zoom in', size=zoom_buttons_size, key="op_zoomO"),sg.Button('zoom out', size=zoom_buttons_size, key="op_zoomI")],
    [sg.Exit()]
]

elements_col = sg.Column(elements_col_layout, element_justification='right')

layout = [
    [image_col,elements_col]
]

window = sg.Window('BIRADS', layout)

while True:
    #event é uma ação e values é uma lista de dados
    event, values = window.read()
    
    if event == 'op_treinar':
        algorithms.train()
    elif event == 'op_calcular':
        algorithms.calculate()
    elif event == 'op_classificar':
        algorithms.classificate()
    elif event == sg.WIN_CLOSED or event == 'Exit':
        break

    imgPath = values['op_diretorio']


window.close()
