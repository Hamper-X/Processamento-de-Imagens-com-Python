import os
from PIL import Image
import numpy as np
import mahotas as mt
from sklearn.svm import LinearSVC
import cv2 as cv
import glob
import math

clf_svm = LinearSVC(random_state=9)

#todo: calcular o valor da reamostragem e usar na função resample()
gray_scale_resample = 32

haralick_distance = 16

images_class1_train = []
images_class2_train = []
images_class3_train = []
images_class4_train = []

images_class1_classificate = []
images_class2_classificate = []
images_class3_classificate = []
images_class4_classificate = []

# import matplotlib.pyplot as plt #Used in the comparison below
from random import randint

"""
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

    print('\033[33m', "="*30, 'Leitura concluida, gerando matrizes...\033[m')
    append_images(images_class1_train, diretorio_01, dir_01, 75)
    append_images(images_class2_train, diretorio_02, dir_02, 75)
    append_images(images_class3_train, diretorio_03, dir_03, 75)
    append_images(images_class4_train, diretorio_04, dir_04, 75)

    append_images(images_class1_classificate, diretorio_01, dir_01, 25)
    append_images(images_class2_classificate, diretorio_02, dir_02, 25)
    append_images(images_class3_classificate, diretorio_03, dir_03, 25)
    append_images(images_class4_classificate, diretorio_04, dir_04, 25)
   
    print('\033[31m', "="*30, 'Geração de matrizes concluida.\033[m')

def append_images(images_class_array, directory_list, dir_path, quant):
    i = 0
    while i < quant:
        choose = randint(0,len(directory_list)-1)
        img_name = directory_list[choose]

        if img_name in directory_list:
            images_class_array.append(generatinMatrix(dir_path+img_name))
            directory_list.remove(img_name)
            i += 1

def train(dirPath):
    get_images_train(dirPath)

    array_train = []
    array_classificate = []
    
    haralick_features, haralick_label = get_haralick_arrays()
    #hu_features, hu_labels = get_hu_arrays()

    #train(haralick_features, haralick_label)
    #train(hu_features, hu_labels)

    pass

def get_haralick_arrays():
    train_features = []
    train_labels = []
    
    train1_features, train1_labels = get_img_features(images_class1_train, "1")
    train_features.extend(train1_features)
    train_labels.extend(train1_labels)

    train2_features, train2_labels = get_img_features(images_class2_train, "2")
    train_features.extend(train2_features)
    train_labels.extend(train2_labels)

    train3_features, train3_labels = get_img_features(images_class3_train, "3")
    train_features.extend(train3_features)
    train_labels.extend(train3_labels)

    train4_features, train4_labels = get_img_features(images_class4_train, "4")
    train_features.extend(train4_features)
    train_labels.extend(train4_labels)

    return (train_features, train_labels)

def get_img_features(img_array, label):
    train_features = []
    train_labels = []
    
    for img in img_array:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = resample(gray)

        features = np.zeros((4, 13))
        i = 1
        while i <= haralick_distance:
            feature = get_haralick_features(gray, i)
            features += feature
            i = i*2

        features_mean = features.mean(axis=0)
        train_features.append(features_mean)
        train_labels.append(label)

    return (train_features, train_labels)

def train1(array_train, array_classificate):
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

            features = np.zeros((4, 13))
            i = 1
            while i <= haralick_distance:
                feature = get_haralick_features(gray, i)
                features += feature
                i = i*2

            features_mean = features.mean(axis=0)
            train_features.append(features_mean)
            train_label.append(cur_label)

    print('Training')
    clf_svm.fit(train_features, train_label)

def calculate(img):
    #print('Algoritmo para calcular e exibir as caracteristicas')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = resample(gray)

    features = np.zeros((4, 13))
    while i <= haralick_distance:
        feature = get_haralick_features(gray, i)
        features += feature
        i = i*2

    features_predict = features.mean(axis=0)
    
    prediction = clf_svm.predict(features_predict.reshape(1, -1))[0]

    return prediction

def get_haralick_features(img, size):
    textures = mt.features.haralick(img, distance=size)

    return textures


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
    #im2 = Image.open(imgPath).convert('RGB')
    #im2 = np.array(im2)
    img = cv.imread(imgPath)
    return img
    # print(im2)

def prediction_result(prediction_list):
    a_prediction_result = [0, 0, 0, 0]
    for prediction in prediction_list:
        if int(prediction) == 1:
            a_prediction_result[0] += 1
        elif int(prediction) == 2:
            a_prediction_result[1] += 1
        elif int(prediction) == 3:
            a_prediction_result[2] += 1
        elif int(prediction) == 4:
            a_prediction_result[3] += 1
    
    print('Prediction Result')
    print(a_prediction_result)


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
    
def haralick_test_function():
    train("D:\Maycon\Documentos\codes\python\imagens")
    #train("D:\Maycon\Documentos\codes\python\imagens")

    print('Calculando resultado')
    path = "D:\Maycon\Documentos\codes\python\imagens"
    paths = os.listdir(path)

    for pa in paths:
        images = os.listdir(path + '\\' + pa)
        cont = 0
        prediction_list = []
        for image in images:
            if cont < 25:
                img = cv.imread(path + '\\' + pa + '\\' + image)
                prediction_list.append(calculate(img))
                cont += 1

haralick_test_function()