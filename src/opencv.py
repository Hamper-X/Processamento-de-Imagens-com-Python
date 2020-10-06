import cv2 as cv
import sys

import frameMain
import control
import parameters

rectangle_offset = 128
offset = 64

window_name = 'image'

global imgPath
global img

# Callback functions
def draw_rectangule(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN and control.mark_image_rectangle :
        global img
        print('x: ' + str(x))
        print('y: ' + str(y))
        #img = cv.imread(param)
        img = imageRead(param)
        cv.rectangle(img, (x-offset,y-offset), (x+offset,y+offset), parameters.color_green, 2, cv.LINE_4)
        #cv.imshow(window_name,img)
        imageShow(window_name, img)

def imageRead(imagePath):
    global imgPath
    imgPath = imagePath
    global img 
    img = cv.imread(imgPath)

    if(needResize(img)):
        img = resize(img)

    return img

def openWindow(window_name, img):
    if(needResize(img)):
        cv.resizeWindow(window_name, parameters.max_canvas[1], parameters.max_canvas[0])
    else:
        cv.resizeWindow(window_name, img.shape[1], img.shape[0])

    cv.namedWindow(window_name)
    imageShow(window_name, img)

def imageShow(window_name, img):
    if(needResize(img)):
        img = resize(img)

    cv.imshow(window_name,img)

def needResize(img):
    return img.shape[0] > parameters.max_canvas[0] or img.shape[1] > parameters.max_canvas[1]

def resize(img):
    return cv.resize(img, parameters.max_canvas)

def abrir_imagem(imagePath):
    imageRead(imagePath)
    if img is None:
        sys.exit("Could not read the image.")
    
    openWindow(window_name, img)
    frameMain.telaInicial()

def marcar_regiao():
    cv.namedWindow(window_name)
    cv.imshow(window_name, img)

    cv.setMouseCallback(window_name,draw_rectangule,param=imgPath)

    frameMain.telaInicial()

    while(1):
        k = cv.waitKey(1) & 0xFF

        if k == ord('q'):
            print('saiii')
            salvar_imagem()
            cv.destroyWindow(window_name)

def salvar_imagem():
    #converter para png
    cv.imwrite("../images/processing.png", img)
