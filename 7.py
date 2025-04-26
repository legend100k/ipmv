//ideal lpf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from math import sqrt

img = Image.open('character.tif').convert('L')  # Convert to grayscale
img_array = np.array(img)  #Original image array

plt.figure(figsize=(15, 12))
plt.subplot(1, 5, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')

original = np.fft.fft2(img)
plt.subplot(1,5,2),
plt.imshow(np.log(1+np.abs(original)), "gray"), 
plt.title("Spectrum")

center = np.fft.fftshift(original)
plt.subplot(1,5,3), 
plt.imshow(np.log(1+np.abs(center)), "gray"), 
plt.title("Centered Spectrum")

inv_center = np.fft.ifftshift(center)
plt.subplot(1,5,4), plt.imshow(np.log(1+np.abs(inv_center)), "gray"), plt.title("Decentralized")

processed_img = np.fft.ifft2(inv_center)
plt.subplot(1,5,5), 
plt.imshow(np.abs(processed_img), "gray"),
plt.title("Processed Image")
plt.show()

##Ideal Low pass filter
def distance(point1,point2):
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)  ###sqrt((u-p/2)**2  + (v -Q/2)**2)

def idealFilterLP(D0,imgShape):
    base = np.zeros(imgShape[:2])
    rows, cols = imgShape[:2]
    center = (rows/2,cols/2)     ### P/2, Q/2
    for x in range(cols):
        for y in range(rows):
            if (distance((y,x),center) < D0): #low pass filter
            
                base[y,x] = 1
    return base
original = np.fft.fft2(img)            ##DFT of original image
center = np.fft.fftshift(original)     ### shifting DFT to centre

plt.figure(figsize=(15, 12))
plt.subplot(1, 5, 1)
plt.imshow(img_array, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1,5,2), 

plt.imshow(np.log(1+np.abs(center)), "gray"),
plt.title("Spectrum")  ## Displaying spectrum

LowPass = idealFilterLP(20,np.shape(img))
plt.subplot(1,5,3), 
plt.imshow(np.abs(LowPass), "gray"), 
plt.title("Low pass filter")   ## original and pass filter

LowPassCenter = center * LowPass   ### Multiplication of image and mask (centre is image )
plt.subplot(1,5,4), 
plt.imshow(np.log(1+np.abs(LowPassCenter)), "gray"),
plt.title("Centered Spectrum multiply Low Pass Filter")


inv_center = np.fft.ifftshift(LowPassCenter)
processed_img = np.fft.ifft2(inv_center)
plt.subplot(1,5,5),
plt.imshow(np.abs(processed_img), "gray"), 
plt.title("Processed Image")

plt.show()
