"""
INSTRUÇÕES PARA EXECUÇÃO |===================================
    1) Installar python
    2) Instalar PySimpleGui: pip install --force-reinstall PySimpleGUI
        2.1) Caso não tenha instalado a versão mais recente, dar um pip upgrade
    3) Instalar opencv-pythob: pip install opencv-python
        3.1) Caso a auto instalação instale a versão menos atualizada, basta usar o pip install --upgrade pip 
""""""
INSTRUÇÕES E DOCUMENTAÇÃO |===================================
    * Values
        -> para pegar o valor do values, basta fazer: values['key']
"""

import PySimpleGUI as sg
import interfaceOptions

    

# MAIN |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def main():
    resp = interfaceOptions.start()
    if resp == True:
        interfaceOptions.telaInicial()
    
    





































if __name__ == "__main__":
    main()
