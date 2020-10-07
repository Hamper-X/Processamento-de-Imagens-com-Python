import PySimpleGUI as sg

import explanation
import algorithms
import configs

import opencv
import control
import parameters

elements_col_size = (50, 0)
zoom_buttons_size = (24, 0)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def telaInicial():
    sg.theme(configs.theme)  # please make your windows colorful

def updateButton(window, event):
    if control.button_selected == True:
        control.button_selected = False
        window[event].update(button_color=parameters.color_button_notselected)
    else:
        control.button_selected = True
        window[event].update(button_color=parameters.color_button_selected)

def initializeButton(label, size, key):
    return sg.Button(label, size=size, key=key, button_color=parameters.color_button_notselected)
    
def telaInicial():
    sg.theme(configs.theme)  # please make your windows colorful
    
    layout = [
        [sg.Text('| Menu |', size=elements_col_size)],
        # Fazer um leitor que permitar pegar apenas imagem

        [sg.FileBrowse('Ler diretorio de imagem', size=elements_col_size, key="_op_diretorio", enable_events=True, button_color=parameters.color_button_notselected)],
        [initializeButton('Marcar região de interesse', size=elements_col_size, key="_op_marcar_regiao")],
        [sg.FolderBrowse('Selecionar características', size=elements_col_size, key="_op_selecionar", enable_events = True, button_color=parameters.color_button_notselected)],
        [initializeButton('Treinar classificador', size=elements_col_size, key="_op_treinar")],
        [initializeButton('Abrir Imagem', size=elements_col_size, key="op_abrirImg")],
        [initializeButton('Calcular e exibir características', size=elements_col_size, key="_op_calcular")],
        [initializeButton('Classificar imagem/regiao', size=elements_col_size, key="_op_classificar")],
        [
            initializeButton('zoom in', size=zoom_buttons_size, key="op_zoomO"), 
            initializeButton('zoom out', size=zoom_buttons_size, key="op_zoomI")
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
            updateButton(window, event) #todo: tirar esse updateButton
            imgPath = values[event]
            opencv.abrir_imagem(imgPath)
        elif event == '_op_marcar_regiao':
            updateButton(window, event) #todo: tirar esse updateButton
            if control.mark_image_rectangle == True:
                control.mark_image_rectangle = False
                window[event].update(button_color=parameters.color_button_notselected)
            else:
                control.mark_image_rectangle = True
                window[event].update(button_color=parameters.color_button_selected)
            
        elif event == '_op_selecionar':
            folder = values[event]   #Pegar diretorio das pastas 
        elif event == '_op_treinar' and folder != "":
            algorithms.train(folder)
        elif event == 'op_zoomI':
            print('+ zoom')
        elif event == 'op_zoomO':
            print('- zoom')     