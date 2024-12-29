#Mian Wang
#Sep 28 2024

import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

# Load the image and convert to grayscale
image_path = "dog.jpeg"  
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Function to add salt and pepper noise
def add_salt_and_pepper_noise(image, noise_level):
    noisy_image = np.copy(image)
    num_salt = np.ceil(noise_level * image.size * 0.5)
    num_pepper = np.ceil(noise_level * image.size * 0.5)

    # Add Salt
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255

    # Add Pepper
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0

    return noisy_image

# Function to apply neighborhood filter
def apply_filter(image, kernel_size):
    return cv2.filter2D(image, -1, np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size))

# Add different levels of noise
noise_levels = [0.01, 0.10, 0.50]
noisy_images = [add_salt_and_pepper_noise(image, noise_level) for noise_level in noise_levels]

# Apply filters (3x3 and 5x5) with zero padding
filtered_3x3 = [apply_filter(img, 3) for img in noisy_images]
filtered_5x5 = [apply_filter(img, 5) for img in noisy_images]

# Display the images in a 3x3 grid
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

# Titles for subplots
titles = ['1% Noise', '10% Noise', '50% Noise',
          '3x3 Filter on 1%', '3x3 Filter on 10%', '3x3 Filter on 50%',
          '5x5 Filter on 1%', '5x5 Filter on 10%', '5x5 Filter on 50%']

# Plot original noisy images in the first row
for i in range(3):
    axs[0, i].imshow(noisy_images[i], cmap='gray')
    axs[0, i].set_title(titles[i])
    axs[0, i].axis('off')

# Plot 3x3 filter results in the second row
for i in range(3):
    axs[1, i].imshow(filtered_3x3[i], cmap='gray')
    axs[1, i].set_title(titles[i + 3])
    axs[1, i].axis('off')

# Plot 5x5 filter results in the third row
for i in range(3):
    axs[2, i].imshow(filtered_5x5[i], cmap='gray')
    axs[2, i].set_title(titles[i + 6])
    axs[2, i].axis('off')

plt.tight_layout()
plt.show()
