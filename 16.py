//Stastical Features
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('cameraman.png').convert('L')
img_a = np.array(img)

N = img_a.size
mean = np.sum(img_a)/N
variance = np.sum((img_a - mean)**2/N)
SD = np.sqrt(variance)
skewness = np.sum(((img_a - mean)/SD)**3/N)
kurtosis = np.sum(((img_a - mean)/SD)**4/N)
median = np.median(img_a)

plt.subplot(1,1,1)
plt.imshow(img_a,cmap='gray')
plt.title('stastical features')
plt.axis('off')

print('mean is:' ,mean)
print('variance is:' , variance)
print('SD is:' , SD)
print('skewness is:' , skewness)
print('Kurtosis is:' , kurtosis)
print('median is:' ,median)
