import cv2 as cv

import parameters

def imageRead(imagePath):
    img = cv.imread(imagePath)

    if(needResize(img)):
        img = resize(img)

    return img

def openWindow(window_name, img):
    cv.namedWindow(window_name)

    if(needResize(img)):
        cv.resizeWindow(window_name, parameters.max_canvas[1], parameters.max_canvas[0])
    else:
        cv.resizeWindow(window_name, img.shape[1], img.shape[0])
        
    imageShow(window_name, img)

def imageShow(window_name, img):
    if(needResize(img)):
        img = resize(img)

    cv.imshow(window_name,img)

def needResize(img):
    return img.shape[0] > parameters.max_canvas[0] or img.shape[1] > parameters.max_canvas[1]

def resize(img):
    return cv.resize(img, parameters.max_canvas)