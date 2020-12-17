% 讀取圖片
img1 = imread('./Cameraman.jpg');
img2 = imread('./Lena.jpg');
img3 = imread('./Peppers.jpg');
%figure,imshow(img1);   %test

%儲存原本的image
I1 = img1;  
I2 = img2;
I3 = img3;

%把transformed過的image先設定為零矩陣
img1_t = zeros(size(img1));
img2_t = zeros(size(img2));
img3_t = zeros(size(img3));

%設定Masks
%mask1 = [0 1 0; 1 -4 1; 0 1 0];
mask2 = [1 1 1; 1 -8 1; 1 1 1];

img1 = padarray(img1,[1,1]);
img1 = double(img1);
img2 = padarray(img2,[1,1]);
img2 = double(img2);
img3 = padarray(img3,[1,1]);
img3 = double(img3);

%利用Laplacian equation
for i=1:size(img1,1)-2
    for j=1:size(img1,2)-2
        img1_t(i,j,1) = sum(sum(mask2.* img1(i:i+2,j:j+2)));
        img1_t(i,j,2) = sum(sum(mask2.* img1(i:i+2,j:j+2)));
        img1_t(i,j,3) = sum(sum(mask2.* img1(i:i+2,j:j+2)));
    end
end

for i=1:size(img2,1)-2
    for j=1:size(img2,2)-2
        img2_t(i,j,1) = sum(sum(mask2.* img2(i:i+2,j:j+2)));
        img2_t(i,j,2) = sum(sum(mask2.* img2(i:i+2,j:j+2)));
        img2_t(i,j,3) = sum(sum(mask2.* img2(i:i+2,j:j+2)));
    end
end

for i=1:size(img3,1)-2
    for j=1:size(img3,2)-2
        img3_t(i,j,1) = sum(sum(mask2.* img3(i:i+2,j:j+2)));
        img3_t(i,j,2) = sum(sum(mask2.* img3(i:i+2,j:j+2)));
        img3_t(i,j,3) = sum(sum(mask2.* img3(i:i+2,j:j+2)));
    end
end

% img1 = uint8(img1);
% img2 = uint8(img2);
% img3 = uint8(img3);


%畫圖
sharp1 = I1 - uint8(img1_t);
subplot(3,2,1);image(I1);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(3,2,2);image(sharp1);title('transformed');
set(gca,'xtick',[],'ytick',[])

sharp2 = I2 - uint8(img2_t);
subplot(3,2,3);image(I2);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(3,2,4);image(sharp2);title('transformed');
set(gca,'xtick',[],'ytick',[])

sharp3 = I3 - uint8(img3_t);
subplot(3,2,5);image(I3);title('Original');
set(gca,'xtick',[],'ytick',[])
subplot(3,2,6);image(sharp3);title('transformed');
set(gca,'xtick',[],'ytick',[])

%儲存圖片
saveas(gcf,'Laplacian','jpg');