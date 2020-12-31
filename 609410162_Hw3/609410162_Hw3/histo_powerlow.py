from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


def powerlow(img):
    for gamma in [0.1]:  # 可調整參數來決定要變暗或變亮，     # s = c * r ^ gamma
        gamma_transformed = np.array(255*(img / 255) ** gamma, dtype='uint8')
    return gamma_transformed


def histoequ(img, L=256):

    # 計算histogram
    histo_gram = np.bincount(img.flatten(), minlength=L)
    '''print(histo_gram)'''  # test

    # 描繪出function
    uniform_hist = (L - 1)*(np.cumsum(histo_gram)/(img.size * 1.0))
    uniform_hist = uniform_hist.astype('uint8')
    '''print(uniform_hist)'''  # test

    # 設定pixel的強度
    h = img.shape[0]
    w = img.shape[1]
    l = img.shape[2]
    uniform_gray = np.zeros(img.shape, dtype='uint8')

    for i in range(h):
        for j in range(w):
            for k in range(l):
                uniform_gray[i, j, k] = uniform_hist[img[i, j, k]]

    return uniform_gray
