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
