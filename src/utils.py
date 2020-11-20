import math
import numpy as np
import mahotas as mt
import cv2 as cv

gray_scale_resample = 33 

def set_gray_scale(grayScale):
    if grayScale.isdigit():
        grayScale = int(grayScale)
        if grayScale > 0 and grayScale <= 32:
            gray_scale_resample = grayScale + 1
            print('Escala de cinza da reamostragem alterada para ' + str(grayScale))
        else:
            print('Informe um valor maior que 0 e menor ou igual a 32')
    else:
        print('Valor invalido')

    return grayScale

def resample(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = math.ceil(img[i][j] % gray_scale_resample)

    return img

def get_haralick_matrix(gray_img):
    features = np.zeros((4, 13))
    i = 1
    while i <= 16:
        feature = get_haralick_features(gray_img, i)
        features += feature
        i = i*2

    return features

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

def get_haralick_features(img, size):
    textures = mt.features.haralick(img, distance=size)

    return textures
