import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from cv2 import cv2
from cov import convo


img1 = cv2.imread("./image1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("./image2.jpg", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("./image3.jpg", cv2.IMREAD_GRAYSCALE)


lapla = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

lapla_img1 = convo(img1, lapla)

lapla_img2 = convo(img2, lapla)

lapla_img3 = convo(img3, lapla)


# calculate the gradient magnitude(梯度大小) of vectors
lapla_img1 = np.sqrt(np.power(lapla_img1, 2))
lapla_img2 = np.sqrt(np.power(lapla_img2, 2))
lapla_img3 = np.sqrt(np.power(lapla_img3, 2))

# mapping values from 0 to 255
lapla_img1 = (lapla_img1 / np.max(lapla_img1)) * 255
lapla_img2 = (lapla_img2 / np.max(lapla_img2)) * 255
lapla_img3 = (lapla_img3 / np.max(lapla_img3)) * 255

# 顯示三張原始圖片
# original
plt.subplot(3, 2, 1)
plt.title('original')
plt.imshow(img1, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 3)
plt.title('original')
plt.imshow(img2, cmap='gray')
plt.axis('off')

plt.subplot(3, 2, 5)
plt.title('original')
plt.imshow(img3, cmap='gray')
plt.axis('off')

# 顯示三張transform後的圖片
# transformed
plt.subplot(3, 2, 2)
plt.title('transformed')
plt.imshow(lapla_img1, cmap='gray', interpolation='bicubic')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.title('transformed')
plt.imshow(lapla_img2, cmap='gray', interpolation='bicubic')
plt.axis('off')

plt.subplot(3, 2, 6)
plt.title('transformed')
plt.imshow(lapla_img3, cmap='gray', interpolation='bicubic')
plt.axis('off')

# 儲存image
plt.savefig('transformed.jpg')
plt.show()
