import cv2
import numpy as np
import matplotlib.pyplot as plt

dog_img = cv2.imread("dog.jpeg", 0)
inverted_dog_img = 255 - dog_img
cv2.imshow("Inverted Dog", inverted_dog_img)
# Wait for a key press indefinitely or for a specific delay (0 means indefinitely)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
