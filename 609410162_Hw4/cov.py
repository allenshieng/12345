import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from cv2 import cv2

#   convolution function


def convo(image, f):
    # height and width of the image
    image_height = image.shape[0]
    image_width = image.shape[1]

    # height and width of the filter
    f_height = f.shape[0]
    f_width = f.shape[1]
    H = (f_height - 1) // 2
    W = (f_width - 1) // 2

    # output numpy matrix with height and width
    out = np.zeros((image_height, image_width))
    # iterate over all the pixel of image X
    for i in np.arange(H, image_height-H):
        for j in np.arange(W, image_width-W):
            sum = 0
            # iterate over the filter
            for k in np.arange(-H, H+1):
                for l in np.arange(-W, W+1):
                    # get the corresponding value from image and filter
                    a = image[i+k, j+l]
                    w = f[H+k, W+l]
                    sum += (w * a)
            out[i, j] = sum
    # return convolution
    return out
