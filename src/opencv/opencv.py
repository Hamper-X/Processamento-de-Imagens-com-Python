import cv2 as cv
import sys

import control
import parameters
from opencv import opencv_utils

rectangle_offset = 128
offset = 64

window_name = 'Image'

global imgPath
#global img
global imgDefault

imgQueue = []
imgQueueUncolor = []

# Callback functions
def set_callbacks(event,x,y,flags,param):
    #todo: tratar se a imagem está carregada
    if event == cv.EVENT_LBUTTONDOWN and control.button_zoomIn:
        zoom(x, y, '+')
    elif event == cv.EVENT_LBUTTONDOWN and control.button_zoomOut:
        zoom(x, y, '-')
    elif event == cv.EVENT_LBUTTONDOWN and control.mark_image_rectangle and not control.image_cropped:
        draw_rectangle(x,y)
        
def zoom(x,y,op):
    global imgDefault
    if op == '+':
        #print(imgQueue)
        #img = imgDefault.copy()
        img = imgQueue[len(imgQueue)-1]
        img = opencv_utils.zoom(x,y, window_name, img, '+')
        opencv_utils.show_zoom_image(window_name, img)
        imgQueue.append(img)
        imgDefault = img
        print('LENGHT' + str(len(imgQueue)))

        img = imgQueueUncolor[len(imgQueueUncolor)-1]
        img = opencv_utils.zoom(x,y, window_name, img, '+')
        imgQueueUncolor.append(img)
    else:
        #print(imgQueue)
        print('zoom out')
        print('LENGHT' + str(len(imgQueue)))
        if len(imgQueue) > 2:
            print('OUTT')
            imgQueue.pop()
            imgQueueUncolor.pop()
            img = imgQueue[-1]
            imgDefault = img
            #opencv_utils.imageShow(window_name, imgAfter)
            opencv_utils.imageShow(window_name, img)
            cv.resizeWindow(window_name, parameters.max_canvas[1], parameters.max_canvas[0])
            
        elif len(imgQueue) == 2:
            print('last')
            img = imgQueue[0].copy()
            opencv_utils.imageShow(window_name, img)
            cv.resizeWindow(window_name, parameters.max_canvas[1], parameters.max_canvas[0])
            imgDefault = img
            imgQueueUncolor.clear()
            imgQueueUncolor.append(img)
            imgQueue.pop()
            

def draw_rectangle(x,y):
    global imgDefault
    print('ha')
    control.image_checked = True
    control.pixel_checked = (x,y)
    
    print('x: ' + str(x))
    print('y: ' + str(y))
    
    img = imgQueueUncolor[len(imgQueueUncolor)-1].copy()
    cv.imshow(window_name, img)
    
    cv.rectangle(img, (x-parameters.offset,y-parameters.offset), (x+parameters.offset,y+parameters.offset), parameters.color_green, 2, cv.LINE_4)
    
    opencv_utils.openWindow(window_name, img)

    imgQueue.append(img)
    if len(imgQueue) == 1:
        print('FIRST RETANCGLE')
        #imgQueue.append(img)

#Core functions
def abrir_imagem(imagePath):
    global imgPath
    imgPath = imagePath
    global imgDefault 
    imgDefault = opencv_utils.imageRead(imagePath)

    imgQueue.clear()
    imgQueueUncolor.clear()
    imgQueue.append(imgDefault)
    imgQueueUncolor.append(imgDefault)

    if imgDefault is None:
        sys.exit("Could not read the image.")
    
    opencv_utils.openWindow(window_name, imgDefault)

    cv.setMouseCallback(window_name,set_callbacks,param=imgPath)

def cortar_imagem():
    if control.image_checked and not control.image_cropped:
        global imgDefault
        imgDefault = opencv_utils.cropImage(window_name, imgDefault)
        opencv_utils.imageShow(window_name, imgDefault)
        control.image_cropped = True

def salvar_imagem():
    try:
        opencv_utils.save_image(imgDefault)
    except NameError:
        print('Imagem não carregada')

def reset_image():
    try:
        global imgDefault
        imgDefault = opencv_utils.imageRead(imgPath)
        opencv_utils.openWindow(window_name, imgDefault)
        
        control.image_cropped = False
        control.image_checked = False

        imgQueue.clear()
        imgQueueUncolor.clear()
    except NameError:
        print('Imagem não carregada')
