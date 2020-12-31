from cv2 import cv2
import math
import histo_powerlow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import mahotas
import mahotas.demos
from pylab import gray, imshow, show
import numpy as np


# import picture & create HSI copy using algorithm
img1 = mpimg.imread('./aloe.jpg')
img2 = mpimg.imread('./church.jpg')
img3 = mpimg.imread('./house.jpg')
img4 = mpimg.imread('./kitchen.jpg')

lab_img1 = mahotas.colors.rgb2lab(img1)
lab_img2 = mahotas.colors.rgb2lab(img2)
lab_img3 = mahotas.colors.rgb2lab(img3)
lab_img4 = mahotas.colors.rgb2lab(img4)

tr_img1 = histo_powerlow.powerlow(lab_img1)
tr_img2 = histo_powerlow.powerlow(lab_img2)
tr_img3 = histo_powerlow.powerlow(lab_img3)
tr_img4 = histo_powerlow.powerlow(lab_img4)

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
plt.imshow(tr_img1)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('transformed')
plt.imshow(tr_img2)
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
plt.imshow(tr_img3)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('transformed')
plt.imshow(tr_img4)
plt.axis('off')

plt.tight_layout()
plt.show()
