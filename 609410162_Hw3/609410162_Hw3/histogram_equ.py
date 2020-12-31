from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def histoequ(img, L=256):
    
    #計算histogram
    histo_gram = np.bincount(img.flatten(), minlength=L)
    '''print(histo_gram)''' #test

    #描繪出function
    uniform_hist = (L - 1)*(np.cumsum(histo_gram)/(img.size * 1.0))
    uniform_hist = uniform_hist.astype('uint8')
    '''print(uniform_hist)'''     #test

    #設定pixel的強度
    h = img.shape[0]
    w = img.shape[1]
    uniform_gray = np.zeros(img.shape, dtype='uint8')
    for i in range(h):
        for j in range(w):
            uniform_gray[i,j] = uniform_hist[img[i,j]]

    return uniform_gray

if __name__ == "__main__":
    
    img1 = mpimg.imread('./Cameraman.jpg')  #讀取圖片
    '''print(img1)''' #test
    img2 = mpimg.imread('./Lena.jpg')
    img3 = mpimg.imread('./Peppers.jpg')

    uniform_gray1 = histoequ(img1)    #histogram equalization
    uniform_gray2 = histoequ(img2)
    uniform_gray3 = histoequ(img3)

    #畫出直方圖
    plt.figure('histogram')
    plt.subplot(3,2,1)
    plt.title('original')
    plt.hist(img1.flatten(),color="green")
    plt.subplot(3,2,3)
    plt.hist(img2.flatten(),color="green")
    plt.subplot(3,2,5)
    plt.hist(img3.flatten(),color="green")

    
    plt.subplot(3,2,2)
    plt.title('transformed')
    plt.hist(uniform_gray1.flatten(),color="blue")
    plt.subplot(3,2,4)
    plt.hist(uniform_gray2.flatten(),color="blue")
    plt.subplot(3,2,6)
    plt.hist(uniform_gray3.flatten(),color="blue")

    plt.savefig('histogram.jpg')
    plt.show()

    #畫出調整前後的結果
    #調整前
    plt.figure('histoequ_transformed')
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
    #調整後
    plt.subplot(3,2,2)
    plt.title('transformed')
    plt.imshow(uniform_gray1)
    plt.axis('off')

    plt.subplot(3,2,4)
    plt.title('transformed')
    plt.imshow(uniform_gray2)
    plt.axis('off')

    plt.subplot(3,2,6)
    plt.title('transformed')
    plt.imshow(uniform_gray3)
    plt.axis('off')

    #儲存image
    plt.savefig('histoequ_transformed.jpg')
    plt.show()
    