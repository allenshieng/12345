clc;
clear;
tic;

img1 = imread("./HW2_test_image/HW2_test_image/blurry_moon.tif");
img2 = imread("./HW2_test_image/HW2_test_image/skeleton_orig.bmp");

%儲存原本的image
I1 = img1;  
I2 = img2;

%把transformed過的image先設定為零矩陣
img1_t = zeros(size(img1));
img2_t = zeros(size(img2));


img1 = padarray(img1,[1,1]);
img1 = double(img1);
img2 = padarray(img2,[1,1]);
img2 = double(img2);

%設定Masks
mask = [1 1 1; 1 -8 1; 1 1 1];

%利用Laplacian equation
for i=1:size(img1,1)-2
    for j=1:size(img1,2)-2
        img1_t(i,j) = sum(sum(mask.* img1(i:i+2,j:j+2)));
    end
end

for i=1:size(img2,1)-2
    for j=1:size(img2,2)-2
        img2_t(i,j,1) = sum(sum(mask.* img2(i:i+2,j:j+2)));
        img2_t(i,j,2) = sum(sum(mask.* img2(i:i+2,j:j+2)));
        img2_t(i,j,3) = sum(sum(mask.* img2(i:i+2,j:j+2)));
    end
end

%畫圖、顯示圖片、儲存圖片
sharp1 = I1 - uint8(img1_t);
subplot(2,2,1);imshow(I1);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(2,2,2);imshow(sharp1);title('transformed');
set(gca,'xtick',[],'ytick',[])

sharp2 = I2 - uint8(img2_t);
subplot(2,2,3);imshow(I2);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(2,2,4);imshow(sharp2);title('transformed');
set(gca,'xtick',[],'ytick',[])

saveas(gcf,'lapla_spatial','bmp');

toc;