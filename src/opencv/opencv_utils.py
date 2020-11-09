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

    return img


def openWindow(window_name, img):
    cv.namedWindow(window_name)

    imageShow(window_name, img)


def imageShow(window_name, img):
    cv.imshow(window_name, img)
    cv.waitKey(1)


def cropImage(window_name, img):
    img = img[
        (control.pixel_checked[1]-(parameters.offset-2)):(control.pixel_checked[1]+(parameters.offset-2)),
        (control.pixel_checked[0]-(parameters.offset-2)):(control.pixel_checked[0]+(parameters.offset-2))
    ]
    return img


def zoom(x, y, window_name, img, op):
    quad = quadrant(img, x, y)
    zoom_offset = 15
    dim = (img.shape[1], img.shape[0])

    if quad == 1:
        img = img[
            (0):(img.shape[0] - zoom_offset),
            (0):(img.shape[1] - zoom_offset)
        ]
    elif quad == 2:
        img = img[
            (0):(img.shape[0] - zoom_offset),
            (zoom_offset):(img.shape[1])
        ]
    elif quad == 3:
        img = img[
            (zoom_offset):(img.shape[0]),
            (0):(img.shape[1] - zoom_offset)
        ]
    elif quad == 4:
        img = img[
            (zoom_offset):(img.shape[0]),
            (zoom_offset):(img.shape[1])
        ]

    print(img.shape)
    if op == '+':
        pass
        img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    else:
        img = cv.resize(img, None, fx=0.9, fy=0.9)

    return img


def quadrant(img, x, y):
    if x < (img.shape[0] / 2) and y < (img.shape[1] / 2):
        return 1
    elif x > (img.shape[0] / 2) and y < (img.shape[1] / 2):
        return 2
    elif x < (img.shape[0] / 2) and y > (img.shape[1] / 2):
        return 3
    elif x > (img.shape[0] / 2) and y > (img.shape[1] / 2):
        return 4


def save_image(img):
    cv.imwrite('../images/processing_image.png', img)
    img = cv.imread('../images/processing_image.png')

    return img
