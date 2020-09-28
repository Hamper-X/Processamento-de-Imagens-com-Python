import PySimpleGUI as sg
import algorithms
def infoTrab():
    layoutInformacao = [
        [sg.Text("""Este é um aplicativo que lê imagens de exames 
mamográficos e possibilita o reconhecimento automático da densidade da 
mama, utilizando técnicas de descrição por textura.""")],
        [sg.Button("Voltar", key='voltar')]
    ]
    window = sg.Window('Informações sobre o trabalho', layoutInformacao)
    event, values = window.read()
    if event == 'voltar':
        window.close()

def helpTrab():
    layoutHelp = [
        [sg.Text(""" 
• Para ler e visualizar imagens use os formatos PNG, TIFF e DICOM. As imagens podem ter
qualquer resolução e número de tons de cinza.
• Após selecionar a imagem que quer avaliar, você sera redirecionado para a aba principal.
• Você tem a opção de selecionar com o mouse uma região de interesse de 128 x 128 pixels 
a ser reconhecida. Apos selecionar, um contorno de cor verde aparecera em torno da area.
• Você tem a opção de ler um diretório contendo 4 subdiretórios com os arquivos de imagens
previamente
recortadas, associadas às 4 classes BIRADS. Os nomes dos subdiretórios são 1,2,3 e essas imagens 
servirão para treinar e testar o classificador.
• Todas essas opções estarão disponiveis no menu principal, apos a seleção da imagem pelo diretorio.
        """)],
        [sg.Button("Entendido !", key='voltar')]
    ]
    window = sg.Window('Informações sobre o trabalho', layoutHelp)
    event, values = window.read()
    if event == 'voltar':
        window.close()
def start():
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layoutInicial = [
        [sg.Button('Iniciar',key='start',size=(62,1))],
        [sg.Button("Sobre o trabalho", size=(30, 1), key='sobre'),
        sg.Button("Como funciona?", size=(30, 1), key = 'tutorial')],
        [sg.Exit()]
    ]

    window = sg.Window('Processamento de Imagens', layoutInicial)
    while True:
        event, values = window.read()
        # Se a janela for fechada ou o botao EXIT for apertado, ele para o programa.
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'sobre':
            infoTrab()
        if event == 'tutorial':
            helpTrab()
        if event == 'start':
            break
            #Abrir janela principal
    window.close()


def telaInicial():
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
        [sg.Output(size=(55,12))],
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


