import PySimpleGUI as sg

import algorithms
import configs

from opencv import opencv
import control
import parameters

elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def telaInicial():
    sg.theme(configs.theme)  # please make your windows colorful
    
def telaInicial():
    sg.theme(configs.theme)  # please make your windows colorful
    
    layout = [
        [sg.Text('| Menu |', size=elements_col_size)],
        # Fazer um leitor que permitar pegar apenas imagem

        [sg.FileBrowse('Buscar imagem', size=elements_col_size, key="_op_diretorio", enable_events=True)],
        [sg.Button('Marcar região de interesse', size=elements_col_size, key="_op_marcar_regiao")],
        [sg.Button('Cortar imagem', size=elements_col_size, key='_cortar_imagem')],
        [sg.Button('Resetar imagem', size=elements_col_size, key='_reset_image')],
        [sg.FolderBrowse('Selecionar características', size=elements_col_size, key="_op_selecionar", enable_events = True)],
        [sg.Button('Treinar classificador', size=elements_col_size, key="_op_treinar")],
        [sg.Button('Calcular e exibir características', size=elements_col_size, key="_op_calcular")],
        [sg.Button('Classificar imagem/regiao', size=elements_col_size, key="_op_classificar")],
        [
            sg.Button('zoom in', size=zoom_buttons_size, key="_op_zoomI"), 
            sg.Button('zoom out', size=zoom_buttons_size, key="_op_zoomO")
        ],

        #[sg.Output(size=(55, 12))],
        [sg.Exit()]
    ]


    window = sg.Window(configs.projectName, layout)

    folder="vazio"
    while (True):
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_op_calcular':
            algorithms.calculate()
        elif event == '_op_classificar':
            opencv.salvar_imagem()
            algorithms.classificate()
        elif event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == '_op_diretorio':
            #imgPath = values['_op_diretorio']
            #img = mpimg.imread(imgPath)
            #plt.imshow(img)
            #plt.show()
            control.image_checked = False 
            imgPath = values[event]
            opencv.abrir_imagem(imgPath)
        elif event == '_op_marcar_regiao':
            if control.mark_image_rectangle == True:
                control.mark_image_rectangle = False
                window[event].update(button_color=parameters.color_button_notselected)
            else:
                control.mark_image_rectangle = True
                window[event].update(button_color=parameters.color_button_selected)
        elif event == '_cortar_imagem':
            opencv.cortar_imagem()
        elif event == '_reset_image':
            opencv.reset_image()
        elif event == '_op_selecionar':
            folder = values[event]   #Pegar diretorio das pastas 
        elif event == '_op_treinar' and folder != "":
            algorithms.train(folder)
        elif event == '_op_zoomI':
            opencv.zoom('+')
        elif event == '_op_zoomO':
            opencv.zoom('-')    