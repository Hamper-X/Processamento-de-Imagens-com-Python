import cv2 as cv
import sys

import control
import parameters
from opencv import opencv_utils

rectangle_offset = 128
offset = 64

window_name = 'image'

global imgPath
global img

# Callback functions
def draw_rectangule(event,x,y,flags,param):
    #todo: tratar se a imagem está carregada
    if event == cv.EVENT_LBUTTONDOWN and control.mark_image_rectangle and not control.image_cropped :
        control.image_checked = True
        control.pixel_checked = (x,y)
        
        print(param)
        global img
        print('x: ' + str(x))
        print('y: ' + str(y))
        
        img = opencv_utils.imageRead(param)
        
        cv.rectangle(img, (x-parameters.offset,y-parameters.offset), (x+parameters.offset,y+parameters.offset), parameters.color_green, 2, cv.LINE_4)
        
        opencv_utils.openWindow(window_name, img)

#Core functions
def abrir_imagem(imagePath):
    global imgPath
    imgPath = imagePath
    global img 
    img = opencv_utils.imageRead(imagePath)
    
    if img is None:
        sys.exit("Could not read the image.")
    
    opencv_utils.openWindow(window_name, img)

    cv.setMouseCallback(window_name,draw_rectangule,param=imgPath)

def cortar_imagem():
    if control.image_checked and not control.image_cropped:
        global img
        img = opencv_utils.cropImage(window_name, img)
        opencv_utils.imageShow(window_name, img)
        control.image_cropped = True

def salvar_imagem():
    try:
        opencv_utils.save_image(img)
    except NameError:
        print('Imagem não carregada')

def zoom(op):
    global img
    img = opencv_utils.zoom(window_name, img, op)

def reset_image():
    try:
        global img
        img = opencv_utils.imageRead(imgPath)
        opencv_utils.openWindow(window_name, img)
        
        control.image_cropped = False
        control.image_checked = False
    except NameError:
        print('Imagem não carregada')
