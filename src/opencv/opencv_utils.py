import cv2 as cv

import parameters
import control

def imageRead(imagePath):
    img = cv.imread(imagePath)

    if(needResize(img)):
        img = resize(img)

    return img

def openWindow(window_name, img):
    cv.namedWindow(window_name)

    if(needResize(img)):
        cv.resizeWindow(window_name, parameters.max_canvas[1], parameters.max_canvas[0])
        img = resize(img)
    else:
        cv.resizeWindow(window_name, img.shape[1], img.shape[0])
        img = resize(img)
      
    imageShow(window_name, img)
      
def imageShow(window_name, img):
    cv.imshow(window_name,img)
    cv.waitKey(1)

def cropImage(window_name, img):
    img = img[
        (control.pixel_checked[1]-parameters.offset):(control.pixel_checked[1]+parameters.offset),
        (control.pixel_checked[0]-parameters.offset):(control.pixel_checked[0]+parameters.offset)
        ]
    imageShow(window_name, img)

def zoom(window_name, img, op):
    if op == '+':
        #imgZoom = cv.resize(img, None, fx=parameters.zoom_offset, fy=parameters.zoom_offset)
        img = cv.resize(img,None,fx=1.1, fy=1.1)
    else:
        img = cv.resize(img,None,fx=0.9, fy=0.9)

    
    imageShow(window_name, img)
    cv.resizeWindow(window_name, parameters.max_canvas[1], parameters.max_canvas[0])
    return img


def needResize(img):
    return img.shape[0] > parameters.max_canvas[0] or img.shape[1] > parameters.max_canvas[1]

def resize(img):
    return cv.resize(img, parameters.max_canvas)