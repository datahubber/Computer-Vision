# Mian Wang
# Date: September 23, 2024

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Function to apply "thermal vision" effect based on brightness
def thermal_vision(image):
    # Normalize the grayscale image to range from 0 to 255
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Create an empty image with 3 channels for color
    thermal_image = np.zeros((normalized_image.shape[0], normalized_image.shape[1], 3), dtype=np.uint8)

    # Iterate through all pixels and assign colors based on brightness
    for i in range(normalized_image.shape[0]):
        for j in range(normalized_image.shape[1]):
            pixel_value = normalized_image[i, j]

            if pixel_value < 85:
                # Darker pixel - Blue color [255, 0, 0]
                thermal_image[i, j] = [255, 0, 0]  # Blue
            elif 85 <= pixel_value < 170:
                # Medium brightness - Green color [127, 255, 127]
                thermal_image[i, j] = [127, 255, 127]  # Green
            else:
                # Brighter pixel - Red color [0, 0, 255]
                thermal_image[i, j] = [0, 0, 255]  # Red

    return thermal_image

# Load and check if the images exist
flowers_image_path = 'flowers.jpg'
drone_image_path = 'drone warehouse.jpg'

if not os.path.exists(flowers_image_path):
    print(f"Error: '{flowers_image_path}' not found.")
if not os.path.exists(drone_image_path):
    print(f"Error: '{drone_image_path}' not found.")

# Load the images in grayscale
flowers_image = cv2.imread(flowers_image_path, cv2.IMREAD_GRAYSCALE)
drone_image = cv2.imread(drone_image_path, cv2.IMREAD_GRAYSCALE)

# Check if images are loaded correctly
if flowers_image is None:
    print(f"Error: Could not load '{flowers_image_path}'")
if drone_image is None:
    print(f"Error: Could not load '{drone_image_path}'")

# Apply thermal vision effect if images are loaded successfully
if flowers_image is not None and drone_image is not None:
    flowers_thermal = thermal_vision(flowers_image)
    drone_thermal = thermal_vision(drone_image)

    # Display the original and thermal images side by side for both images
    plt.figure(figsize=(14, 10))

    # For flowers.jpg
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(cv2.imread(flowers_image_path), cv2.COLOR_BGR2RGB))
    plt.title('Flowers - Original')

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(flowers_thermal, cv2.COLOR_BGR2RGB))
    plt.title('Flowers - Thermal Vision')

    # For drone-warehouse.jpg
    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(cv2.imread(drone_image_path), cv2.COLOR_BGR2RGB))
    plt.title('Drone Warehouse - Original')

    plt.subplot(2, 2, 4)
    plt.imshow(cv2.cvtColor(drone_thermal, cv2.COLOR_BGR2RGB))
    plt.title('Drone Warehouse - Thermal Vision')

    plt.show()
