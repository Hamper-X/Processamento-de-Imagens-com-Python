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

sg.theme('Dark Blue 3')  # please make your windows colorful
layout = [
    [sg.Text('|============| Menu |===========|',size=(30,0))],
    # Fazer um leitor que permitar pegar apenas imagem
    [sg.FileBrowse('Ler diretorio de imagem',size=(30,0),key="op_diretorio")],
    [sg.Button('Selecionar características',size=(30,0),key="op_selecionar")],
    [sg.Button('Treinar classificador',size=(30,0),key="op_treinar")],
    [sg.Button('Abrir Imagem',size=(30,0),key="op_abrirImg")],
    [sg.Button('Marcar região de interesse',size=(30,0),key="op_marcar")],
    [sg.Button('Calcular e exibir características',size=(30,0),key="op_calcular")],
    [sg.Button('Classificar imagem/regiao',size=(30,0),key="op_classificar")],
    [sg.Button('zoom in',size=(14,0),key="op_zoomO"),sg.Button('zoom out',size=(14,0),key="op_zoomI")],
    [sg.Output(size=(32,10))],
    [sg.Exit()]
]

window = sg.Window('Teste 01', layout)

while True:
    #event é uma ação e values é uma lista de dados
    event, values = window.read()
    
    #Se a janela for fechada ou o botao EXIT for apertado, ele para o programa.
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    imgPath = values['op_diretorio']


window.close()
