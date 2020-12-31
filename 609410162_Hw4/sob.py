import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from cv2 import cv2
from cov import convo


img1 = cv2.imread("./image1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("./image2.jpg", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("./image3.jpg", cv2.IMREAD_GRAYSCALE)


Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
Gy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])


sob_x1 = convo(img1, Gx)
sob_y1 = convo(img1, Gy)

sob_x2 = convo(img2, Gx)
sob_y2 = convo(img2, Gy)

sob_x3 = convo(img3, Gx)
sob_y3 = convo(img3, Gy)

# calculate the gradient magnitude(梯度大小) of vectors
sob_out1 = np.sqrt(np.power(sob_x1, 2) + np.power(sob_y1, 2))
sob_out2 = np.sqrt(np.power(sob_x2, 2) + np.power(sob_y2, 2))
sob_out3 = np.sqrt(np.power(sob_x3, 2) + np.power(sob_y3, 2))

# mapping values from 0 to 255
sob_out1 = (sob_out1 / np.max(sob_out1)) * 255
sob_out2 = (sob_out2 / np.max(sob_out2)) * 255
sob_out3 = (sob_out3 / np.max(sob_out3)) * 255

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
plt.imshow(sob_out1, cmap='gray', interpolation='bicubic')
plt.axis('off')

plt.subplot(3, 2, 4)
plt.title('transformed')
plt.imshow(sob_out2, cmap='gray', interpolation='bicubic')
plt.axis('off')

plt.subplot(3, 2, 6)
plt.title('transformed')
plt.imshow(sob_out3, cmap='gray', interpolation='bicubic')
plt.axis('off')

# 儲存image
plt.savefig('transformed.jpg')
plt.show()
