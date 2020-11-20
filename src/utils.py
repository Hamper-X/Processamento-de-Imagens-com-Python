import math
import numpy as np
import mahotas as mt

def set_gray_scale(grayScale):
    if grayScale.isdigit():
        grayScale = int(grayScale)
        if grayScale > 0 and grayScale <= 32:
            grayScale += 1
            print('Escala de cinza da reamostragem alterada para ' + str(grayScale))
        else:
            print('Informe um valor maior que 0 e menor ou igual a 32')
    else:
        print('Valor invalido')

    return grayScale

def resample(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = math.ceil(img[i][j] % 8)

    return img

def get_haralick_matrix(gray_img):
    features = np.zeros((4, 13))
    i = 1
    while i <= 16:
        feature = get_haralick_features(gray_img, i)
        features += feature
        i = i*2

    return features

def get_haralick_features(img, size):
    textures = mt.features.haralick(img, distance=size)

    return textures
