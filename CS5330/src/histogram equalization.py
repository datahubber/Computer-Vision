import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the color image
img = cv2.imread("flowers.jpg")

# Split the image into its three channels: Blue, Green, and Red
b_channel, g_channel, r_channel = cv2.split(img)

# Perform histogram equalization on each channel
equalized_b = cv2.equalizeHist(b_channel)
equalized_g = cv2.equalizeHist(g_channel)
equalized_r = cv2.equalizeHist(r_channel)

# Merge the equalized channels back into a color image
equalized_img = cv2.merge([equalized_b, equalized_g, equalized_r])

# Convert the images from BGR to RGB for correct display in Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
equalized_img_rgb = cv2.cvtColor(equalized_img, cv2.COLOR_BGR2RGB)

# Display the original and equalized images side by side for comparison
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

# Equalized Image
plt.subplot(1, 2, 2)
plt.imshow(equalized_img_rgb)
plt.title("Equalized Image")
plt.axis('off')

plt.show()
