//power law
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('cameraman.png').convert("L")
img_a = np.array(img ,dtype = np.float32) /255.0

img_power = np.uint8((img_a ** 2)*255)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img_a,cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(img_power,cmap="gray")
plt.title("Power Law gamma 0.5 ")
plt.axis("off")
plt.tight_layout()
plt.show()
