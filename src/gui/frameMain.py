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
        [sg.Text('                                             | Menu |', size=elements_col_size)],
        # Fazer um leitor que permitar pegar apenas imagem

        [sg.FileBrowse('Buscar imagem', size=elements_col_size, key="_op_diretorio", enable_events=True, button_color=parameters.color_button_notselected)],
        [sg.Button('Marcar região de interesse', size=elements_col_size, key="_op_marcar_regiao", button_color=parameters.color_button_notselected)],
        [sg.Button('Cortar imagem', size=elements_col_size, key='_cortar_imagem', button_color=parameters.color_button_notselected)],
        [sg.Button('Resetar imagem', size=elements_col_size, key='_reset_image', button_color=parameters.color_button_notselected)],
        [sg.Button('Salvar imagem', size=elements_col_size, key='_save_image', button_color=parameters.color_button_notselected)],
        [sg.FolderBrowse('Carregar imagens de treinamento', size=elements_col_size, key="_op_selecionar", enable_events = True, button_color=parameters.color_button_notselected)],
        [sg.Button('Treinar classificador', size=elements_col_size, key="_op_treinar", button_color=parameters.color_button_notselected)],
        [sg.Button('Calcular e exibir características', size=elements_col_size, key="_op_calcular", button_color=parameters.color_button_notselected)],
        [sg.Input('Gray Scale 1-32',key='_op_gray_scale'),sg.Button('Save', size=(8,0), key="_op_save_gray", button_color=parameters.color_button_notselected)],
        [sg.Button('Classificar imagem/regiao', size=elements_col_size, key="_op_classificar", button_color=parameters.color_button_notselected)],
        [sg.Button('Zoom', size=elements_col_size, key="_op_zoomI", button_color=parameters.color_button_notselected) 
            #sg.Button('zoom out', size=zoom_buttons_size, key="_op_zoomO", button_color=parameters.color_button_notselected)
        ],
        #[sg.Output(size=(55, 12))],
        [sg.Output(size=(54,12))],
        [sg.Exit()]
    ]


    window = sg.Window(configs.projectName, layout)

    folder="vazio"
    while (True):
        # event é uma ação e values é uma lista de dados
        event, values = window.read()

        if event == '_op_diretorio':
            #imgPath = values['_op_diretorio']
            #img = mpimg.imread(imgPath)
            #plt.imshow(img)
            #plt.show()
            imgPath = values[event]

            if imgPath != "": 
                control.image_cropped = False
                control.image_checked = False
                opencv.abrir_imagem(imgPath)
            
        elif event == '_op_marcar_regiao':
            control.button_zoomIn = False
            control.button_zoomOut = False

            #window['_op_zoomO'].update(button_color=parameters.color_button_notselected)
            window['_op_zoomI'].update(button_color=parameters.color_button_notselected)
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
        elif event == '_save_image':
            opencv.salvar_imagem()
        elif event == '_op_selecionar':
            folder = values[event]   #Pegar diretorio das pastas                 
            algorithms.get_images_train(folder)
            algorithms.get_100_path(folder,True)
        elif event == '_op_treinar' and folder != "":
            algorithms.train()
        elif event == '_op_calcular':
            opencv.salvar_imagem()
            algorithms.calculate()
        elif event == '_op_classificar':
            opencv.salvar_imagem()
            algorithms.classificate()

        elif event == '_op_save_gray':
            grayScale = values['_op_gray_scale']
            grayScale_verificad = algorithms.valid_gray_scale(grayScale)

        elif event == '_op_zoomI':
            window['_op_marcar_regiao'].update(button_color=parameters.color_button_notselected)
            #window['_op_zoomO'].update(button_color=parameters.color_button_notselected)

            control.button_zoomIn = not control.button_zoomIn
            if control.button_zoomIn == True:
                window[event].update(button_color=parameters.color_button_selected)
            else:
                window[event].update(button_color=parameters.color_button_notselected)

            control.mark_image_rectangle = False
            control.button_zoomOut = False
        elif event == '_op_zoomO':
            window['_op_marcar_regiao'].update(button_color=parameters.color_button_notselected)
            window['_op_zoomI'].update(button_color=parameters.color_button_notselected)
            
            control.button_zoomOut = not control.button_zoomOut
            if control.button_zoomOut == True:
                window[event].update(button_color=parameters.color_button_selected)
            else:
                window[event].update(button_color=parameters.color_button_notselected)

            control.mark_image_rectangle = False
            control.button_zoomIn = False
        elif event == sg.WIN_CLOSED or event == 'Exit':
            break    