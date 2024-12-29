#Mian Wang
#2024-10-22


import cv2
import numpy as np

# Load the image (use image path here)
image = cv2.imread('blocks.jpg')

# Check if the image was loaded properly
if image is None:
    print("Error: Image not loaded. Check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a GaussianBlur to remove noise and smooth the edges
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# Apply adaptive threshold to create a binary image
# Lower threshold to capture blocks with less noise
_, thresh = cv2.threshold(blurred, 198, 255, cv2.THRESH_BINARY_INV)

# Use a kernel for morphological closing to clean up noise
kernel = np.ones((7, 7), np.uint8)
cleaned_thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Find contours in the thresholded image
contours, _ = cv2.findContours(cleaned_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop through each contour
for contour in contours:
    # Filter out small contours that may be noise by adjusting the area threshold
    area = cv2.contourArea(contour)
    if area < 1000:  # Increase the minimum area threshold for better contour filtering
        continue
    
    # Draw contour in green
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    # Compute the center of the contour using image moments
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0

    # Draw the center point in red and label it
    cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Show the final image with contours and center points
cv2.imshow("Image with Contours and Centers", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite('output_image_with_contours_updated_final.png', image)
