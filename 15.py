#opening and closing

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import binary_erosion, binary_dilation

img = Image.open('cameraman.png').convert('L')
img_array = np.array(img)
binary_img = (img_array > 128).astype(np.uint8)  # Threshold at 128

kernel = np.ones((3, 3), dtype=np.uint8)

# Opening: Erosion followed by Dilation
opened_img = binary_dilation(binary_erosion(binary_img, structure=kernel), structure=kernel)

# Closing: Dilation followed by Erosion
closed_img = binary_erosion(binary_dilation(binary_img, structure=kernel), structure=kernel)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(binary_img, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(opened_img, cmap='gray')
plt.title('Opened Image (Erosion + Dilation)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closed_img, cmap='gray')
plt.title('Closed Image (Dilation + Erosion)')
plt.axis('off')

plt.tight_layout()
plt.show()
