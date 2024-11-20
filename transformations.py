import cv2
import numpy as np

def translate_image(image, tx, ty):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, M, (cols, rows))

def scale_image(image, sx, sy):
    return cv2.resize(image, None, fx=sx, fy=sy, interpolation=cv2.INTER_LINEAR)

def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, M, (cols, rows))

def shear_image(image, shear_x, shear_y):
    rows, cols = image.shape[:2]
    M = np.float32([[1, shear_x, 0], [shear_y, 1, 0]])
    return cv2.warpAffine(image, M, (cols, rows))
