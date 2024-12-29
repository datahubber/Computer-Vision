# Mian Wang
# 2024-10-15

import cv2
import numpy as np

# Load the image you provided
image_path = 'drone warehouse.jpg'
image = cv2.imread(image_path)

# Step 1: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Step 3: Use Canny Edge Detection to detect edges in the image
edges = cv2.Canny(blurred_image, threshold1=50, threshold2=150)

# Step 4: Invert the edges to highlight the important parts
inverted_edges = cv2.bitwise_not(edges)

# Step 5: Colorize the edges with a green color (simulating night vision)
colored_edges = cv2.applyColorMap(inverted_edges, cv2.COLORMAP_SUMMER)

# Step 6: Display or save the resulting image
cv2.imshow('Night Vision Effect', colored_edges)

# Save the output image
cv2.imwrite('night_vision_effect.png', colored_edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
