import os
from PIL import Image
import numpy as np
from random import randint
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
        return False

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
    
    # print(imgMatrix)
    # print('Imagens lidas' + str(len(imgMatrix)))
    # print('\033[31m',"="*30,'Geração de matrizes concluida.\033[m')

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
    #print('Image path ' + imgPath)
    im2 = Image.open(imgPath).convert('RGB')                  
    im2 = np.array(im2) 
    return im2
    #print(im2)

"""
    * Objetivo:     Validar dado de entrada alterando a escala de cinza
    * Argumentos:   Escala de cinza fornecida
    * Retorno:      Valor da escala de cinza verificada/default
"""
def valid_gray_scale(grayScale):
    valor = 32
    if grayScale.isdigit():
        valor = grayScale
    return valor

# AREA DE SELEÇÃO ALEATORIA |=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

"""
    * Objetivo:     Separar 75% das imagens escolhidas de forma aleatória, mas balanceadas entre as classes, das 25% que serão usadas posteriormente.
    * Argumentos:   Diretorio de localização da pasta contendo os 4 sub diretorios e o valor booleano. True: retorna vetor com 75% | False retorna vetor de 25%
    * Retorno:      Vetor com caminho das imagens para
"""
def get_100_path(dirPath,choose):
    img25_global = []
    img75_global = []
    contador = 0
    used = []
    sort_validation = True
    
    dir_01 = dirPath + '/1/'
    dir_02 = dirPath + '/2/'
    dir_03 = dirPath + '/3/'
    dir_04 = dirPath + '/4/'

    try:
        diretorio_01 = os.listdir(dir_01)
        diretorio_02 = os.listdir(dir_02)
        diretorio_03 = os.listdir(dir_03)
        diretorio_04 = os.listdir(dir_04)
    except FileNotFoundError:
        print('Diretórios 1/2/3/4 não encontrados')
        return False

    # Get random positions 75%
    while contador<75:
        index = randint(0,100)
        for values in used:
            if values == index:
                sort_validation = False
        if sort_validation == True:
            used.append(index)
            contador += 1
        sort_validation = True


    # Alocar 75%
    for positions in used:
        img75_global.append(diretorio_01[positions])
        img75_global.append(diretorio_02[positions])
        img75_global.append(diretorio_03[positions])
        img75_global.append(diretorio_04[positions])


    # Alocar 25% restantes
    x = 0
    while x<100:
        for positions in used:
            if positions == x:
                sort_validation = False
        if sort_validation == True:
            img25_global.append(diretorio_01[x])
            img25_global.append(diretorio_02[x])
            img25_global.append(diretorio_03[x])
            img25_global.append(diretorio_04[x])
        x += 1

    if choose == True:
        return img75_global
    else:
        return img25_global
    

"""
    * Objetivo:     Separar 75% das imagens escolhidas de forma aleatória, mas balanceadas entre as classes, das 25% que serão usadas posteriormente.
    * Argumentos:   Diretorio de localização da pasta contendo os 4 sub diretorios e o valor booleano. True: retorna vetor com 75% | False retorna vetor de 25%
    * Retorno:      Vetor com matriz das imagens para treino.
"""
def get_100_matrix(dirPath,choose):
    img25_global = []
    img75_global = []
    contador = 0
    used = []
    sort_validation = True

    matrix_img01 = []
    matrix_img02 = []
    matrix_img03 = []
    matrix_img04 = []
    
    dir_01 = dirPath + '/1/'
    dir_02 = dirPath + '/2/'
    dir_03 = dirPath + '/3/'
    dir_04 = dirPath + '/4/'

    try:
        diretorio_01 = os.listdir(dir_01)
        diretorio_02 = os.listdir(dir_02)
        diretorio_03 = os.listdir(dir_03)
        diretorio_04 = os.listdir(dir_04)
    except FileNotFoundError:
        print('Diretórios 1/2/3/4 não encontrados')
        return False
    
    for imgWay in diretorio_01:
        #print("imgWay = ",dir_01+imgWay)
        matrix_img01.append(generatinMatrix(dir_01+imgWay))
    for imgWay in diretorio_02:
        #print("imgWay = ",dir_02+imgWay)
        matrix_img02.append(generatinMatrix(dir_02+imgWay))
    for imgWay in diretorio_03:
        #print("imgWay = ",dir_03+imgWay)
        matrix_img03.append(generatinMatrix(dir_03+imgWay))
    for imgWay in diretorio_04:
        #print("imgWay = ",dir_04+imgWay)
        matrix_img04.append(generatinMatrix(dir_04+imgWay))

    # Get random positions 75%
    while contador<75:
        index = randint(0,100)
        for values in used:
            if values == index:
                sort_validation = False
        if sort_validation == True:
            used.append(index)
            contador += 1
        sort_validation = True


    # Alocar 75%
    for positions in used:
        img75_global.append(matrix_img01[positions])
        img75_global.append(matrix_img02[positions])
        img75_global.append(matrix_img03[positions])
        img75_global.append(matrix_img04[positions])


    # Alocar 25% restantes
    x = 0
    while x<100:
        for positions in used:
            if positions == x:
                sort_validation = False
        if sort_validation == True:
            img25_global.append(matrix_img01[x])
            img25_global.append(matrix_img02[x])
            img25_global.append(matrix_img03[x])
            img25_global.append(matrix_img04[x])
        x += 1

    if choose == True:
        return img75_global
    else: 
        return img25_global
    