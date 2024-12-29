#Mian Wang
#2024-10-04

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the images
image1 = Image.open("jensen_huang.jpg")
image2 = Image.open("lisa_su.jpg")

# Ensure both images are the same size
image1 = image1.resize((min(image1.size[0], image2.size[0]), min(image1.size[1], image2.size[1])))
image2 = image2.resize(image1.size)

# Convert images to numpy arrays
image1_np = np.array(image1)
image2_np = np.array(image2)

# Apply a low pass filter (11x11 Gaussian filter)
low_pass_image1 = cv2.GaussianBlur(image1_np, (11, 11), 0)
low_pass_image2 = cv2.GaussianBlur(image2_np, (11, 11), 0)

# Create high pass filter by subtracting low pass from the original and adding 127
high_pass_image2 = image2_np - low_pass_image2 + 127

# Combine both images with equal weighting
combined_image = cv2.addWeighted(low_pass_image1, 0.5, high_pass_image2, 0.5, 0)

# Hidden step: Perform a simple sharpening on the combined image
kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
sharpened_image = cv2.filter2D(combined_image, -1, kernel)

# Display the result in a 3x1 grid
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(cv2.cvtColor(low_pass_image1, cv2.COLOR_BGR2RGB))
axs[0].set_title("Low Pass Filter Image")
axs[0].axis('off')

axs[1].imshow(cv2.cvtColor(high_pass_image2, cv2.COLOR_BGR2RGB))
axs[1].set_title("High Pass Filter Image")
axs[1].axis('off')

axs[2].imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
axs[2].set_title("Combined Image")
axs[2].axis('off')

plt.show()
