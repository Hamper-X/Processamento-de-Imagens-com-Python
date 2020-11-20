import os
import math
from random import randint

import cv2 as cv
import numpy as np
import mahotas as mt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from opencv import opencv_utils
import utils

clf_svm = LinearSVC(random_state=9)

# todo: calcular o valor da reamostragem e usar na função resample()
gray_scale_resample = 33

haralick_distance = 16

images_class1_train = []
images_class2_train = []
images_class3_train = []
images_class4_train = []

images_class1_classificate = []
images_class2_classificate = []
images_class3_classificate = []
images_class4_classificate = []

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
        choose = randint(0, len(directory_list)-1)
        img_name = directory_list[choose]

        if img_name in directory_list:
            images_class_array.append(opencv_utils.imageRead(dir_path+img_name))
            directory_list.remove(img_name)
            i += 1

############################# HARALICK AND HU FEATURES #############################


def get_haralick_hu_features(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = utils.resample(img)

    haralick_features = utils.get_haralick_matrix(img).mean(axis=0)
    haralick_features = haralick_features.tolist()
    hu_features = get_hu_moments(img)
    hu_features = hu_features.tolist()[0]

    haralick_features.extend(hu_features)

    return haralick_features


def get_hu_moments(img):
    # Threshold image
    # _, img = cv.threshold(img, 128, 255, cv.THRESH_BINARY)

    # Calculate Moments
    moment = cv.moments(img)

    # Calculate Hu Moments
    hu = cv.HuMoments(moment)
    for i in range(0, 7):
        if hu[i] != 0:
            hu[i] = -1 * np.sign(hu[i]) * np.log10(np.abs(hu[i]))

    # transformar Hu em um vetor unico
    hu = hu.reshape((1, 7))

    return hu


############################# CONFUSION MATRIX #############################
"""
    * Objetivo:
            - Gerar matrix de confusão
            - Metricas de sensibilidade media
            - Especificidade Media
    * Argumentos:   - Vetor de valores reais
                    - Vetor de valores preditos
    * Retorno: --//--
            - Print da matriz de confusão
            - Print da sensibilidade média
            - Print da especificidade média
"""


def get_confusion_matrix(classe, real_values, predicts_classificator):
    print("Matrix de confusão da classe ", classe, ":\n",
          confusion_matrix(real_values, predicts_classificator), "\n")
    sense = 0
    matrix = confusion_matrix(real_values, predicts_classificator)
    a = 0
    b = 0
    for i in matrix:
        for j in i:
            if a == b:
                sense += matrix[a][b]/100
                b += 1
    a += 1
    b = 0
    print("Acuraricia/Sensibilidade = ", (sense), "\n")

    soma = 0
    a = 0
    b = 0
    for i in matrix:
        for j in i:
            if a != b:
                soma += matrix[a][b]/300
            else:
                break
    soma = 1 - soma
    a += 1
    b = 0
    print("Especificidade = ", (soma), "\n")


def makeConfusion():
    expected, actual = classificate_25_images()
    expected_splited = list(chunks(expected, 4))
    actual_splited = list(chunks(actual, 4))
    get_confusion_matrix(1, expected_splited[0], actual_splited[0])
    get_confusion_matrix(2, expected_splited[1], actual_splited[1])
    get_confusion_matrix(3, expected_splited[2], actual_splited[2])
    get_confusion_matrix(4, expected_splited[3], actual_splited[3])


def chunks(lista, n):
    inicio = 0
    for i in range(n):
        final = inicio + len(lista[i::n])
        yield lista[inicio:final]
        inicio = final


############################# TRAIN AND CLASSIFICATE #############################
def train(dirPath):
    get_images_train(dirPath)

    train_features = []
    train_labels = []

    print('Treinando o classificador')
    for img in images_class1_train:
        haralic_hu_features = get_haralick_hu_features(img)
        train_features.append(haralic_hu_features)
        train_labels.append("1")

    for img in images_class2_train:
        haralic_hu_features = get_haralick_hu_features(img)
        train_features.append(haralic_hu_features)
        train_labels.append("2")

    for img in images_class3_train:
        haralic_hu_features = get_haralick_hu_features(img)
        train_features.append(haralic_hu_features)
        train_labels.append("3")

    for img in images_class4_train:
        haralic_hu_features = get_haralick_hu_features(img)
        train_features.append(haralic_hu_features)
        train_labels.append("4")

    clf_svm.fit(train_features, train_labels)

    print('Treinamento finalizado')


def classificate_25_images():
    print('Algoritmo para classificar 25\% das images imagem/região')
    expected_array = []
    actual_array = []

    for img in images_class1_classificate:
        expected_array.append(1)
        actual_array.append(classificate(img))
    for img in images_class2_classificate:
        expected_array.append(2)
        actual_array.append(classificate(img))
    for img in images_class3_classificate:
        expected_array.append(3)
        actual_array.append(classificate(img))
    for img in images_class4_classificate:
        expected_array.append(4)
        actual_array.append(classificate(img))

    return (expected_array, actual_array)


def classificate(img):
    features_predict = get_haralick_hu_features(img)
    features_predict = np.array(features_predict)
    
    try:
        prediction = clf_svm.predict(features_predict.reshape(1, -1))[0]
        return int(prediction)
    except NotFittedError:
        print('Classificador não treinado')
        return 0


def set_gray_scale(grayScale):
   gray_scale_resample = utils.set_gray_scale(grayScale)

############################# TESTS #############################


def haralick_test_function():
    # train("D:\Maycon\Documentos\codes\python\imagens")
    # train("/home/carrocinha/Faculdade/6-periodo/PI/trab/imagens") #lnx
    # train("C:\\Users\\Felipe\\Desktop\\git\\imagens")
    # classificate_25_images()
    train("D:\Maycon\Documentos\codes\python\imagens")

    print('Calculando resultado')

    # path = "/home/carrocinha/Faculdade/6-periodo/PI/trab/imagens" #lnx
    path = "D:\Maycon\Documentos\codes\python\imagens"
    # path = "C:\\Users\\Felipe\\Desktop\\git\\imagens"

    paths = os.listdir(path)

    for pa in paths:
        images = os.listdir(path + '\\' + pa)  # win
        # images = os.listdir(path + '/' + pa) # lnx
        cont = 0
        prediction_list = []
        for image in images:
            if cont < 25:
                img = cv.imread(path + '/' + pa + '\\' + image)  # win
                # img = cv.imread(path + '/' + pa + '/' + image) # lnx
                # img = cv.imread(path + '/' + pa + '/' + image, cv.IMREAD_GRAYSCALE) # lnx

                prediction_list.append(classificate(img))
                cont += 1

# def hu_test_function():
#     # train("D:\Maycon\Documentos\codes\python\imagens")
#     # train("/home/carrocinha/Faculdade/6-periodo/PI/trab/imagens") #lnx
#     train("C:\\Users\\Felipe\\Desktop\\git\\imagens")
#     classificate_25_images()

#     print('Calculando resultado')

#     # path = "/home/carrocinha/Faculdade/6-periodo/PI/trab/imagens" #lnx
#     # path = "D:\Maycon\Documentos\codes\python\imagens"
#     path = "C:\\Users\\Felipe\\Desktop\\git\\imagens"

#     paths = os.listdir(path)

#     for pa in paths:
#         images = os.listdir(path + '\\' + pa)  # win
#         # images = os.listdir(path + '/' + pa) # lnx
#         cont = 0
#         prediction_list = []
#         for image in images:
#             if cont < 25:
#                 img = cv.imread(path + '/' + pa + '\\' + image)  # win
#                 # img = cv.imread(path + '/' + pa + '/' + image) # lnx
#                 # img = cv.imread(path + '/' + pa + '/' + image, cv.IMREAD_GRAYSCALE) # lnx

#                 prediction_list.append(classificate(img))
#                 cont += 1


#haralick_test_function()
# hu_test_function()
