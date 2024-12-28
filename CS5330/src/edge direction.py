import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create the matrix from the image
matrix = np.array([
    [0, 255, 255],
    [0, 0, 255],
    [0, 0, 0]
], dtype=np.uint8)

# Apply the Sobel operator to compute gradients
# Compute Gx (horizontal gradient)
Gx = cv2.Sobel(matrix, cv2.CV_64F, 1, 0, ksize=3)

# Compute Gy (vertical gradient)
Gy = cv2.Sobel(matrix, cv2.CV_64F, 0, 1, ksize=3)

# Compute the edge magnitude
magnitude = np.sqrt(Gx**2 + Gy**2)

# Compute the edge direction
direction = np.arctan2(Gy, Gx) * 180 / np.pi  # Convert from radians to degrees

# Display the results
print("Gx (Horizontal Gradient):\n", Gx)
print("Gy (Vertical Gradient):\n", Gy)
print("Edge Magnitude:\n", magnitude)
print("Edge Direction (in degrees):\n", direction)

# Plotting the edge magnitude and direction
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Edge Magnitude")
plt.imshow(magnitude, cmap='gray')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title("Edge Direction")
plt.imshow(direction, cmap='gray')
plt.colorbar()

plt.show()
