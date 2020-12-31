clc;
clear;
tic;

img1 = imread("./HW2_test_image/HW2_test_image/blurry_moon.tif");
img2 = imread("./HW2_test_image/HW2_test_image/skeleton_orig.bmp");

%建立gaussian filter
Gauss_filter = fspecial('gaussian',[3 3],1);


%儲存原本的image
I1 = img1;  
I2 = img2;

%把transformed過的image先設定為零矩陣
img1_t = zeros(size(img1));
img2_t = zeros(size(img1));

img1 = padarray(img1,[1,1]);
img1 = double(img1);
img2 = padarray(img2,[1,1]);
img2 = double(img2);


%convolution
for i=1:size(img1,1)-2
    for j=1:size(img1,2)-2
        img1_t(i,j) = sum(sum(Gauss_filter.* img1(i:i+2,j:j+2)));
    end
end

sharpmask1 = I1 - uint8(img1_t);
sharp1 = I1 + sharpmask1;

for i=1:size(img2,1)-2
    for j=1:size(img2,2)-2
        img2_t(i,j,1) = sum(sum(Gauss_filter.* img2(i:i+2,j:j+2)));
        img2_t(i,j,2) = sum(sum(Gauss_filter.* img2(i:i+2,j:j+2)));
        img2_t(i,j,3) = sum(sum(Gauss_filter.* img2(i:i+2,j:j+2)));
    end
end

sharpmask2 = I2 - uint8(img2_t);
sharp2 = I2 + sharpmask2;

%畫圖、顯示圖片、儲存圖片

%第一張圖
subplot(2,2,1);imshow(I1);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(2,2,2);imshow(sharp1);title('transformed');
set(gca,'xtick',[],'ytick',[])

%第二張圖
subplot(2,2,3);imshow(I2);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(2,2,4);imshow(sharp2);title('transformed');
set(gca,'xtick',[],'ytick',[])

saveas(gcf,'unsharp_spatial','bmp');

toc;