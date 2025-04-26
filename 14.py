//erosion
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image and convert to binary (thresholding)
img = np.array(Image.open('cameraman.png').convert('L')) > 128  # Convert directly to binary

# Define 3x3 kernel (structuring element)
kernel_size = 3  # Using 3x3 kernel

# Custom Erosion function using bit-stuffing logic with count
def custom_erode(img, kernel_size):
    pad_h, pad_w = kernel_size // 2, kernel_size // 2
    img_pad = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    output = np.zeros_like(img)

    # Loop through the image
    for i in range(pad_h, img_pad.shape[0] - pad_h):
        for j in range(pad_w, img_pad.shape[1] - pad_w):
            count = 0  # Initialize count for matching 1's in the region

            # Loop over the kernel area in the image
            for ki in range(kernel_size):
                for kj in range(kernel_size):
                    if img_pad[i - pad_h + ki, j - pad_w + kj] == 1:
                        count += 1
            
            # If the count equals the total number of elements in the kernel (kernel_size^2), set pixel to 1
            if count == kernel_size ** 2:
                output[i - pad_h, j - pad_w] = 1

    return output

# Apply the custom erosion function
eroded = custom_erode(img, kernel_size)

# Display results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(eroded, cmap='gray')
plt.title('Eroded Image (Custom Logic)')
plt.axis('off')

plt.tight_layout()
plt.show()

//dilation
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def dilation(img_array, kernel):
    h, w = img_array.shape
    kh, kw = kernel.shape
    pad_h, pad_w = kh // 2, kw // 2

    img_pad = np.pad(img_array, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')
    output = np.zeros_like(img_array)

    for i in range(h):
        for j in range(w):
            for ki in range(kh):
                for kj in range(kw):
                    if img_pad[i + ki, j + kj] == 1:   # if any pixel is 1
                        output[i, j] = 1
                        break
                else:
                    continue
                break
    return output

# Load and binarize image
img = Image.open('cameraman.png').convert('L')
img_array = np.array(img)
binary_img = (img_array > 128).astype(np.uint8)

# Define a simple 3x3 kernel
kernel = np.ones((3, 3), dtype=np.uint8)

# Perform Dilation
dilated_img = dilation(binary_img, kernel)

# Plot
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(binary_img, cmap='gray')
plt.title('Original Binary Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilated_img, cmap='gray')
plt.title('Dilated Image')
plt.axis('off')

plt.tight_layout()
plt.show()

