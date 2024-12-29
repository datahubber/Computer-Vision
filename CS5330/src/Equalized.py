# Mian Wang
# Date: September 23, 2024

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to perform manual histogram equalization
def manual_histogram_equalization(image):
    # Flatten the image to a 1D array
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])

    # Compute the CDF (Cumulative Distribution Function)
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()  # Normalize

    # Create a mapping of old pixel values to new pixel values
    cdf_m = np.ma.masked_equal(cdf, 0)  # Mask zeros
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())  # Normalize CDF
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # Fill masked values

    # Map the image using this CDF
    equalized_image = cdf[image]

    return equalized_image, cdf_normalized

# Load dark and light images
dark_image = cv2.imread('dark_image.jpg', cv2.IMREAD_GRAYSCALE)
light_image = cv2.imread('light_image.jpg', cv2.IMREAD_GRAYSCALE)

# Perform manual histogram equalization on both images
dark_manual_equalized_image, dark_cdf_normalized = manual_histogram_equalization(dark_image)
light_manual_equalized_image, light_cdf_normalized = manual_histogram_equalization(light_image)

# Perform OpenCV histogram equalization for comparison
dark_opencv_equalized_image = cv2.equalizeHist(dark_image)
light_opencv_equalized_image = cv2.equalizeHist(light_image)

# Display results for dark image
plt.figure(figsize=(14, 8))

plt.subplot(2, 3, 1)
plt.imshow(dark_image, cmap='gray')
plt.title('Dark Original Image')

plt.subplot(2, 3, 2)
plt.imshow(dark_manual_equalized_image, cmap='gray')
plt.title('Dark Manually Equalized')

plt.subplot(2, 3, 3)
plt.imshow(dark_opencv_equalized_image, cmap='gray')
plt.title('Dark OpenCV Equalized')

# Display results for light image
plt.subplot(2, 3, 4)
plt.imshow(light_image, cmap='gray')
plt.title('Light Original Image')

plt.subplot(2, 3, 5)
plt.imshow(light_manual_equalized_image, cmap='gray')
plt.title('Light Manually Equalized')

plt.subplot(2, 3, 6)
plt.imshow(light_opencv_equalized_image, cmap='gray')
plt.title('Light OpenCV Equalized')

plt.show()
