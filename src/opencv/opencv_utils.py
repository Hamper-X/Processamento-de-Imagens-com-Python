import cv2 as cv
import pydicom as dicom
#from pydicom.data import get_testdata_files 

import parameters
import control

def imageRead(imagePath):
    if(imagePath[-4:] == '.dcm' or imagePath[-4:] == '.DCM'):
        img = dicom.dcmread(imagePath).pixel_array*128
        img = save_image(img)   
    else:    
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
      
    imageShow(window_name, img)
      
def imageShow(window_name, img):
    cv.imshow(window_name,img)
    cv.waitKey(1)

def cropImage(window_name, img):
    img = img[
        (control.pixel_checked[1]-(parameters.offset-2)):(control.pixel_checked[1]+(parameters.offset-2)),
        (control.pixel_checked[0]-(parameters.offset-2)):(control.pixel_checked[0]+(parameters.offset-2))
        ]
    return img    

def zoom(window_name, img, op):
    if op == '+':
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

def save_image(img):
    cv.imwrite('../images/processing_image.png' ,img)
    img = cv.imread('../images/processing_image.png')
    
    return img   