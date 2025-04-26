//laplacian
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def laplacian_sharpen(image):
    laplacian_kernel = np.array([[0, -1, 0],

                                 [-1, 4, -1],

                                 [0, -1, 0]])

    height, width = image.shape
    sharpened_image = np.zeros((height, width), dtype=np.float32)
    padded_image = np.pad(image, pad_width=1, mode='edge')
    for i in range(height):
        for j in range(width):
            region = padded_image[i:i+3, j:j+3]
            sharpened_value = np.sum(region * laplacian_kernel)
            sharpened_image[i, j] = np.clip(image[i, j] + sharpened_value, 0, 255)
    return sharpened_image.astype(np.uint8)
image_path = 'path_to_your_image.jpg'  
image = Image.open(image_path).convert('L')  
image_array = np.array(image)
sharpened_image = laplacian_sharpen(image_array)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Sharpened Image')
plt.imshow(sharpened_image, cmap='gray')
plt.axis('off')
plt.show()



//averaging filter

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def averaging_filter(img_a):
    mask =np.array(([1,1,1],[1,1,1],[1,1,1]))
    m,n = img_a.shape
    img_avg=np.zeros([m,n])

    for i in range(1,m-2):
        for j in range(1,n-2):
            img_avg[i,j] = (1/9)*np.sum(img_a[i-1:i+2 , j-1:j+2]*mask)
    plt.figure(figsize=(12,8))
    plt.subplot(1,2,1)
    plt.imshow(img_a ,cmap='gray')
    plt.title('original Image')
    plt.axis('off')
    
    plt.subplot(1,2,2)
    plt.imshow(img_avg*255,cmap='gray')
    plt.title('avg mask applied')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    img = Image.open('cameraman.png').convert('L')
    img_a = np.array(img)
    averaging_filter(img_a)
