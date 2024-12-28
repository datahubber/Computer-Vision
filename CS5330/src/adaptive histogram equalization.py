import cv2
import matplotlib.pyplot as plt
from skimage import exposure

# Read the image
image_path = "drone warehouse.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(image)

# Display the original and CLAHE result side by side
plt.figure(figsize=(12, 6))

# Original image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

# CLAHE processed image
plt.subplot(1, 2, 2)
plt.title('CLAHE Image')
plt.imshow(clahe_image, cmap='gray')
plt.axis('off')

# Show both images
plt.tight_layout()
plt.show()
