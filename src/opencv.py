import cv2 as cv
import sys

import configs
import frameMain

rectangle_offset = 128
offset = 64

window_name = 'image'

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        print('x: ' + str(x))
        print('y: ' + str(y))
        cv.rectangle(param, (x-offset,y-offset), (x+offset,y+offset), configs.color_green, 2, cv.LINE_4)
        cv.imshow(window_name,param)
        #cv.circle(img,(x,y),100,(255,0,0),-1)

def openImage(filepath):
    print('OPEN')
    img = cv.imread(filepath)

    if img is None:
        sys.exit("Could not read the image.")

    cv.namedWindow(window_name)
    cv.imshow(window_name, img)
    
    cv.setMouseCallback(window_name,draw_circle, param=img)
    
    while(1):
        k = cv.waitKey(1) & 0xFF

        if k == ord('q'):
            cv.imwrite("../images/teste1.png", img)
            cv.destroyWindow(window_name)
            frameMain.telaInicial("../images/teste1.png")