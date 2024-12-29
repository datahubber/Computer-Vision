# Mian Wang
# 2024-10-15

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Part 1 - Visualizing Blurring in 3D

# Load the dog image from the given file (change the file path accordingly)
img_path = 'dog.jpeg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded correctly
if img is None:
    print(f"Error: Unable to load image at {img_path}")
else:
    print("Image loaded successfully!")
    
    # Gaussian blurring
    blur_5x5 = cv2.GaussianBlur(img, (5, 5), 0)
    blur_11x11 = cv2.GaussianBlur(img, (11, 11), 0)

    # 3D plotting function
    def plot_3d_subplot(ax, image, title):
        x = np.arange(0, image.shape[1], 1)
        y = np.arange(0, image.shape[0], 1)
        X, Y = np.meshgrid(x, y)
        ax.plot_surface(X, Y, image, cmap='gray')
        ax.set_title(title)
    
    # Create subplots with 3 columns to display all 3 images
    fig = plt.figure(figsize=(18, 6))
    
    # Subplot for the original image
    ax1 = fig.add_subplot(131, projection='3d')
    plot_3d_subplot(ax1, img, "Original Image in 3D")
    
    # Subplot for the 5x5 Gaussian Blurred image
    ax2 = fig.add_subplot(132, projection='3d')
    plot_3d_subplot(ax2, blur_5x5, "5x5 Gaussian Blurred Image in 3D")
    
    # Subplot for the 11x11 Gaussian Blurred image
    ax3 = fig.add_subplot(133, projection='3d')
    plot_3d_subplot(ax3, blur_11x11, "11x11 Gaussian Blurred Image in 3D")
    
    # Show all 3D plots together
    plt.tight_layout()
    plt.show()

# Answer the question as a comment:
# Q: What do you notice about the 3D graphs as the filter size increases?
# A: As the filter size increases, the 3D graph becomes smoother, indicating that the image's sharp details are blurred out.
