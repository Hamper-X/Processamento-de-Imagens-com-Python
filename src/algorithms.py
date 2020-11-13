import os
from PIL import Image
import numpy as np
import mahotas as mt
from sklearn.svm import LinearSVC
import cv2 as cv
import glob
import math

clf_svm = LinearSVC(random_state=9)

# import matplotlib.pyplot as plt #Used in the comparison below

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

    print('\033[33m', "="*30, 'Leitura concluida, gerando matrizes...\033[m')
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

    print('Imagens lidas' + str(len(imgMatrix)))
    print('\033[31m', "="*30, 'Geração de matrizes concluida.\033[m')


def train(dirPath):
    print('\033[34m', "="*30, 'Algoritmo para treinar o classificador\033[m')

    train_features = []
    train_label = []

    train_names = os.listdir(dirPath)
    for train_name in train_names:
        cur_label = train_name
        cur_path = dirPath + "/" + train_name
        for file in glob.glob(cur_path + "/*.png"):
            img = cv.imread(file)

            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray = resample(gray)

            i = 1
            while i <= 16:
                features = get_haralick_features(gray, i)
                train_features.append(features)
                train_label.append(cur_label)

                i = i*2

    clf_svm.fit(train_features, train_label)


def calculate(img):
    print('Algoritmo para calcular e exibir as caracteristicas')

    features = get_haralick_features(img, 2)

    prediction = clf_svm.predict(features.reshape(1, -1))[0]
    cv.putText(img, prediction, (20, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 3)

    return features


def get_haralick_features(img, size):
    textures = mt.features.haralick(img, distance=size)

    haralick_mean = textures.mean(axis=0)

    return haralick_mean


def resample(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = math.ceil(img[i][j]/8)

    return img


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
    # print(im2)


train("D:\Maycon\Documentos\codes\python\imagens")
img = cv.imread(
    "D:\Maycon\Documentos\codes\python\imagens\\1\p_d_left_cc(12).png")
calculate(img)
