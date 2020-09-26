import PySimpleGUI as sg


def infoTrab():
    layoutInformacao = [
        [sg.Text("""Este trabalho mostra  um aplicativo que leia imagens de exames 
mamográficos e possibilite o reconhecimento automático da densidade da 
mama,utilizando técnicas de descrição por textura.""")],
        [sg.Button("Entendido !", key='voltar')]
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
    imgPath = None
    sg.theme('Dark Blue 3')  # please make your creations colorful
    layoutInicial = [
        [sg.Text('Escolha o diretorio da imagem e depois clique em avançar para iniciar.', size=(62, 0))],
        [sg.InputText(size=(52,0)),
            sg.FileBrowse('Buscar', key="op_diretorio"),
            sg.Button("Avançar",key='next')],
        [sg.Button("Sobre o trabalho", size=(30, 0), key='sobre'),
        sg.Button("Como funciona?", size=(30, 0), key = 'tutorial')],
        [sg.Exit()]
    ]

    window = sg.Window('Teste 02', layoutInicial)
    while True:
        event, values = window.read()
        # Se a janela for fechada ou o botao EXIT for apertado, ele para o programa.
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'sobre':
            infoTrab()
        if event == 'tutorial':
            helpTrab()
        if event == 'op_diretorio':
            imgPath = values['op_diretorio']
        if event == 'next':
            break
    window.close()
    return imgPath
    

# MAIN |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def main():
    start()







































if __name__ == "__main__":
    main()