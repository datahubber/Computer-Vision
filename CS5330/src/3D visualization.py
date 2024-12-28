import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the image
img = Image.open('drone warehouse.jpg').convert('L')  # Convert image to grayscale

# Convert the image to a numpy array
img_array = np.array(img)

# Get the dimensions of the image
rows, cols = img_array.shape

# Create meshgrid for 3D plotting
X, Y = np.meshgrid(np.arange(cols), np.arange(rows))

# Create a figure for the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with a color map
ax.plot_surface(X, Y, img_array, cmap='plasma')

# Customize the plot (optional)
ax.set_title('3D Visualization of Image')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Pixel Intensity')

# Show the plot
plt.show()
