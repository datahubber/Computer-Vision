# Mian Wang
# 2024-10-15

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Part 2 - Edge Detection

# Load the dog image (change the file path accordingly)
img_path = 'dog.jpeg' 
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Sobel filter application
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

# Apply different cutoff values
def apply_cutoff(image, cutoff):
    result = np.zeros_like(image)
    result[image > cutoff] = 255
    return result

sobel_cutoff_50 = apply_cutoff(sobel_combined, 50)
sobel_cutoff_150 = apply_cutoff(sobel_combined, 150)

# Canny edge detection
canny_edges = cv2.Canny(img, 100, 100)

# Apply Gaussian Blur and then Canny edge detection
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
canny_on_blurred = cv2.Canny(blurred_img, 100, 100)

# Display results in a grid
fig, axs = plt.subplots(2, 4, figsize=(12, 8))
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original')

axs[0, 1].imshow(sobel_cutoff_50, cmap='gray')
axs[0, 1].set_title('Sobel Cutoff 50')

axs[0, 2].imshow(sobel_cutoff_150, cmap='gray')
axs[0, 2].set_title('Sobel Cutoff 150')

axs[0, 3].imshow(canny_edges, cmap='gray')
axs[0, 3].set_title('Canny')

axs[1, 0].imshow(blurred_img, cmap='gray')
axs[1, 0].set_title('Blurred')

axs[1, 1].imshow(apply_cutoff(np.sqrt(cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)**2 + 
                                        cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)**2), 50), cmap='gray')
axs[1, 1].set_title('Sobel Blurred 50')

axs[1, 2].imshow(apply_cutoff(np.sqrt(cv2.Sobel(blurred_img, cv2.CV_64F, 1, 0, ksize=3)**2 + 
                                        cv2.Sobel(blurred_img, cv2.CV_64F, 0, 1, ksize=3)**2), 150), cmap='gray')
axs[1, 2].set_title('Sobel Blurred 150')

axs[1, 3].imshow(canny_on_blurred, cmap='gray')
axs[1, 3].set_title('Canny on Blurred')

# Hide axes for clarity
for ax in axs.flat:
    ax.axis('off')

plt.tight_layout()
plt.show()

# Answer the questions from the assignment as comments:
# Q1: What did you notice when you went from a lower threshold value to a higher one?
# A1: With a higher cutoff value, fewer edges are detected, and only the most prominent edges remain.

# Q2: What did you notice before and after applying a Gaussian Blur to the image?
# A2: Applying a Gaussian Blur before edge detection reduces noise and leads to smoother edges, but some fine details may be lost.
