import matplotlib.pyplot as plt     #顯示圖片
import matplotlib.image as mpimg    #讀取圖片
import numpy as np

img1 = mpimg.imread('./Cameraman.jpg')   #打開image，記得路徑要把\改/
img2 = mpimg.imread('./Lena.jpg') 
img3 = mpimg.imread('./Peppers.jpg')

for gamma in [0.1,0.5,1.0,1.5,2.0]:     #可調整參數來決定要變暗或變亮
    gamma_transformed1 = np.array(255*(img1 / 255) ** gamma, dtype = 'uint8')     # s = c * r ^ gamma 
    gamma_transformed2 = np.array(255*(img2 / 255) ** gamma, dtype = 'uint8')
    gamma_transformed3 = np.array(255*(img3 / 255) ** gamma, dtype = 'uint8')

#顯示三張原始圖片
#original
plt.subplot(3,2,1)
plt.title('original')
plt.imshow(img1)
plt.axis('off')

plt.subplot(3,2,3)
plt.title('original')
plt.imshow(img2)
plt.axis('off')

plt.subplot(3,2,5)
plt.title('original')
plt.imshow(img3)
plt.axis('off')

#顯示三張transform後的圖片
#transformed
plt.subplot(3,2,2)
plt.title('transformed')
plt.imshow(gamma_transformed1)
plt.axis('off')

plt.subplot(3,2,4)
plt.title('transformed')
plt.imshow(gamma_transformed2)
plt.axis('off')

plt.subplot(3,2,6)
plt.title('transformed')
plt.imshow(gamma_transformed3)
plt.axis('off')

#儲存image
plt.savefig('power_law_transformed.jpg')
plt.show()