import os
from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt #Used in the comparison below

"""
    * Objetivo:     Gerar treinamento da imagem escolhida com base nas imagens do diretorio.
    * Argumentos:   Diretorio da pasta com as imagens
    * Retorno:      Booleano mostrando se deu certo ou não.
"""
def get_images_train(dirPath):
    dir_01 = dirPath + '/1/'
    dir_02 = dirPath + '/2/'
    dir_03 = dirPath + '/3/'
    dir_04 = dirPath + '/4/'

    # diretorio_0X corresponde a uma lista com nomes das imagens de cada pasta numerada de 1 a 4.
    # Para pegar a imagem, use a lista de nomes
    try:
        diretorio_01 = os.listdir(dir_01)
        diretorio_02 = os.listdir(dir_02)
        diretorio_03 = os.listdir(dir_03)
        diretorio_04 = os.listdir(dir_04)
    except FileNotFoundError:
        print('Diretórios 1/2/3/4 não encontrados')
        return

    print('\033[33m',"="*30,'Leitura concluida, gerando matrizes...\033[m')
    imgMatrix = []
    for imgWay in diretorio_01:
        #print("imgWay = ",dir_01+imgWay)
        imgMatrix.append(generatinMatrix(dir_01+imgWay))
    for imgWay in diretorio_02:
        #print("imgWay = ",dir_02+imgWay)
        imgMatrix.append(generatinMatrix(dir_02+imgWay))
    for imgWay in diretorio_03:
        #print("imgWay = ",dir_03+imgWay)
        imgMatrix.append(generatinMatrix(dir_03+imgWay))
    for imgWay in diretorio_04:
        #print("imgWay = ",dir_04+imgWay)
        imgMatrix.append(generatinMatrix(dir_04+imgWay))
    
    print(imgMatrix)
    print('Imagens lidas' + str(len(imgMatrix)))
    print('\033[31m',"="*30,'Geração de matrizes concluida.\033[m')

def train():
    print('\033[34m',"="*30,'Algoritmo para treinar o classificador\033[m')

def calculate():
    print('Algoritmo para calcular e exibir as caracteristicas')

def classificate():
    print('Algoritmo para classificar imagem/região')

"""
    * Objetivo:     Gerar uma matriz a partir da imagem
    * Argumentos:   Diretorio de localização da imagem
    * Retorno:      Matriz gerada pela imagem
"""
def generatinMatrix(imgPath):
    print('Image path ' + imgPath)
    im2 = Image.open(imgPath).convert('RGB')                  
    im2 = np.array(im2) 
    return im2
    #print(im2)