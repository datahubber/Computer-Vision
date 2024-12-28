import cv2

# Read the "cookie.jpg" image
image_path = "cookie.jpg"
image = cv2.imread(image_path)

# Check if the image is loaded correctly
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(blurred, 100, 200)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw only contours larger than a minimum area
boundary_contour_image = image.copy()
min_contour_area = 500  # Adjust this value as needed
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
cv2.drawContours(boundary_contour_image, filtered_contours, -1, (0, 255, 0), 2)

# Display the original, edges, and boundary contour images
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Filtered Contours", boundary_contour_image)

# Save the result to a file (optional)
cv2.imwrite("filtered_cookie_contours.jpg", boundary_contour_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
