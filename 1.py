from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_path = 'cameraman.png'
img = Image.open(img_path).convert("L")

img_a = np.array(img)

negative_a = 255 - img_a
negative = Image.fromarray(negative_a)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_a , cmap ="gray")
plt.title("Original Image ")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(negative_a ,cmap="gray")
plt.title("Image Negative")
plt.axis("off")
