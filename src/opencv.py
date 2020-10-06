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
        img = cv.imread(param)
        cv.rectangle(img, (x-offset,y-offset), (x+offset,y+offset), parameters.color_green, 2, cv.LINE_4)
        cv.imshow(window_name,img)


def abrir_imagem(imagePath):
    global imgPath
    imgPath = imagePath
    global img 
    img = cv.imread(imgPath)
    
    if img is None:
        sys.exit("Could not read the image.")

    cv.namedWindow(window_name)
    cv.imshow(window_name, img)
    
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
    print('train')
    print(img)
    cv.imwrite("../images/processing.png", img)
