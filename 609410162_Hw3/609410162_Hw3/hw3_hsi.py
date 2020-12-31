from cv2 import cv2
import converter
import histo_powerlow
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# import picture & create HSI copy using algorithm
img1 = mpimg.imread('./aloe.jpg', 1)
img2 = mpimg.imread('./church.jpg')
img3 = mpimg.imread('./house.jpg')
img4 = mpimg.imread('./kitchen.jpg')

# RGB轉HSI
hsi1 = converter.RGB_TO_HSI(img1)
hsi2 = converter.RGB_TO_HSI(img2)
hsi3 = converter.RGB_TO_HSI(img3)
hsi4 = converter.RGB_TO_HSI(img4)

# image enhance
pl_hsi1 = histo_powerlow.powerlow(hsi1)
pl_hsi2 = histo_powerlow.powerlow(hsi2)
pl_hsi3 = histo_powerlow.powerlow(hsi3)
pl_hsi4 = histo_powerlow.powerlow(hsi4)

# # HSI轉RGB
# tb_rgb1 = converter.HSI_TO_RGB(pl_hsi1)
# tb_rgb2 = converter.HSI_TO_RGB(pl_hsi2)
# tb_rgb3 = converter.HSI_TO_RGB(pl_hsi3)
# tb_rgb4 = converter.HSI_TO_RGB(pl_hsi4)

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
plt.imshow(pl_hsi1)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('transformed')
plt.imshow(pl_hsi2)
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
plt.imshow(pl_hsi3)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('transformed')
plt.imshow(pl_hsi4)
plt.axis('off')

plt.tight_layout()
plt.show()
