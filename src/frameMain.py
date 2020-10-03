import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import explanation
import algorithms
import configs

def telaInicial():
    sg.theme(configs.theme)  # please make your windows colorful

    image_col_layout = [
        [sg.Text('Imagem', pad=((220, 150), (20, 20)))],
        [sg.Image(size=(500, 500), key='_image')]
    ]

    image_col = sg.Column(image_col_layout, element_justification='left')

    elements_col_size = (50, 0)
    zoom_buttons_size = (24, 0)

    elements_col_layout = [
        [sg.Text('| Menu |', size=elements_col_size)],
        # Fazer um leitor que permitar pegar apenas imagem
        [sg.FileBrowse('Ler diretorio de imagem',
                       size=elements_col_size, key="_op_diretorio", enable_events=True)],
        [sg.Button('Selecionar características',
                   size=elements_col_size, key="_op_selecionar")],
        [sg.Button('Treinar classificador',
                   size=elements_col_size, key="_op_treinar")],
        [sg.Button('Abrir Imagem', size=elements_col_size, key="op_abrirImg")],
        [sg.Button('Marcar região de interesse',
                   size=elements_col_size, key="_op_marcar")],
        [sg.Button('Calcular e exibir características',
                   size=elements_col_size, key="_op_calcular")],
        [sg.Button('Classificar imagem/regiao',
                   size=elements_col_size, key="_op_classificar")],
        [sg.Button('zoom in', size=zoom_buttons_size, key="op_zoomO"), sg.Button(
            'zoom out', size=zoom_buttons_size, key="op_zoomI")],
        [sg.Output(size=(55, 12))],
        [sg.Exit()]
    ]

    elements_col = sg.Column(
        elements_col_layout, element_justification='right')

    layout = [
        [image_col, elements_col]
    ]

    window = sg.Window(configs.projectName, layout)

    while True:
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_op_treinar':
            algorithms.train()
        elif event == '_op_calcular':
            algorithms.calculate()
        elif event == '_op_classificar':
            algorithms.classificate()
        elif event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == '_op_diretorio':
            imgPath = values['_op_diretorio']
            img = mpimg.imread(imgPath)
            plt.imshow(img)
            plt.show()
            