# Mian Wang
# Date: September 23, 2024

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using cv2
image = cv2.imread('flowers.jpg')

# Convert the image to grayscale using the Average Method
def average_method(image):
    return np.mean(image, axis=2).astype(np.uint8)

# Convert the image to grayscale using the NTSC method
def ntsc_method(image):
    return (0.299 * image[:, :, 2] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 0]).astype(np.uint8)

# Grayscale using the built-in method for comparison
gray_cv2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply both methods
gray_avg = average_method(image)
gray_ntsc = ntsc_method(image)

# Display the results
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gray_avg, cmap='gray')
plt.title('Average Method')

plt.subplot(1, 3, 3)
plt.imshow(gray_ntsc, cmap='gray')
plt.title('NTSC Method')

plt.show()
