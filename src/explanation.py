import PySimpleGUI as sg

def infoTrab():
    layoutInformacao = [
        [sg.Text("""Este é um aplicativo que lê imagens de exames 
mamográficos e possibilita o reconhecimento automático da densidade da 
mama, utilizando técnicas de descrição por textura.""")],
        [sg.Button("_voltar", key='_voltar')]
    ]
    
    window = sg.Window('Informações sobre o trabalho', layoutInformacao)
    event, values = window.read()
    if event == '_voltar':
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
        [sg.Button("Entendido !", key='_voltar')]
    ]

    window = sg.Window('Informações sobre o trabalho', layoutHelp)
    event, values = window.read()
    if event == '_voltar':
        window.close()