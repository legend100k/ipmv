//log
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('albert.jpeg').convert('L')
img_a = np.array(img)

c=0.25
log_img = c*np.log(1 + img_a)
log_image = np.array(log_image, dtype=np.uint8)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_a,cmap="gray")
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(log_img,cmap='gray')
plt.title('Log transformed Image')
plt.axis('off')
plt.tight_layout()
plt.show()
