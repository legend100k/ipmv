//histogram equlisation
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img= Image.open('albert.jpeg').convert('L')
img_a = np.array(img)

hist_original ,bins = np.histogram(img_a.flatten(),bins = 256 ,range =[0,256])

hist=np.zeros(256 ,dtype=int)
for pixel in img_a.flatten():
    hist[pixel]+=1

cdf = np.zeros(256,dtype=int)
cdf[0]= hist[0]
for i in range(1,256):
    cdf[i] = cdf[i-1] + hist[i]

cdf_min = cdf.min()
total_pixels = img_a.size
eq_map = ((cdf - cdf_min)*255/(total_pixels - cdf_min)).astype('uint8')

eq_img = eq_map[img_a]

eq_hist, _ =np.histogram(eq_img.flatten() ,bins=256,range =[0,256])

plt.figure(figsize=(12,10))

plt.subplot(2,2,1)
plt.imshow(img_a,cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.subplot(2,2,2)
plt.plot(hist_original,lw=2)
plt.title("Original Historgam")
plt.xlabel('pixel Intensity')
plt.ylabel('Freq')

plt.subplot(2,2,3)
plt.imshow(eq_img,cmap='gray')
plt.title("Equalized Image")
plt.axis('off')
plt.subplot(2,2,4)
plt.plot(eq_hist,lw=2)
plt.title("Equalized Historgam")
plt.xlabel('pixel Intensity')
plt.ylabel('Freq')

plt.tight_layout()
plt.show()
