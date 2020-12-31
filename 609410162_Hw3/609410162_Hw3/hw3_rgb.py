from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2


def powerlow(img):
    for gamma in [6.5]:  # 可調整參數來決定要變暗或變亮，     # s = c * r ^ gamma
        gamma_transformed = np.array(255*(img / 255) ** gamma, dtype='uint8')
    return gamma_transformed


def powerlow2(img):
    for gamma in [1.5]:  # 可調整參數來決定要變暗或變亮，     # s = c * r ^ gamma
        gamma_transformed = np.array(255*(img / 255) ** gamma, dtype='uint8')
    return gamma_transformed


def histoequ(img, L=256):

    # 計算histogram
    histo_gram = np.bincount(img.flatten(), minlength=L)
    '''print(histo_gram)'''  # test

    # 描繪出function
    uniform_hist = (L - 1)*(np.cumsum(histo_gram)/(img.size * 1.0))
    # uniform_hist = uniform_hist.astype('uint8')
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


if __name__ == "__main__":

    img1 = mpimg.imread('./aloe.jpg')  # 讀取圖片
    img2 = mpimg.imread('./church.jpg')
    img3 = mpimg.imread('./house.jpg')
    img4 = mpimg.imread('./kitchen.jpg')

    # histogram equalization
    uniform_rgb1 = histoequ(img1)
    uniform_rgb2 = histoequ(img2)

    # power low
    powerlow_img3 = powerlow(img3)
    powerlow_img4 = powerlow2(img4)


# 畫出調整前後的結果
# 第一、二張
# 原圖

plt.figure('histoequ_transformed')
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(img1)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('original')
plt.imshow(img2)
plt.axis('off')

# 調整後
plt.subplot(2, 2, 2)
plt.title('transformed')
plt.imshow(uniform_rgb1)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('transformed')
plt.imshow(uniform_rgb2)
plt.axis('off')

plt.tight_layout()
plt.show()

# 第三、四張
# 原圖

plt.figure('histoequ_transformed')
plt.subplot(2, 2, 1)
plt.title('original')
plt.imshow(img3)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('original')
plt.imshow(img4)
plt.axis('off')

# 調整後

plt.subplot(2, 2, 2)
plt.title('transformed')
plt.imshow(powerlow_img3)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('transformed')
plt.imshow(powerlow_img4)
plt.axis('off')

plt.tight_layout()
plt.show()


# # 儲存image
# plt.savefig('histoequ_transformed.jpg')
