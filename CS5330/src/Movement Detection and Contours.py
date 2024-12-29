# Mian Wang
# 2024-11-01

import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0) 

# Read the first frame
ret, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    # Capture the current frame
    ret, current_frame = cap.read()
    if not ret:
        break

    # Convert current frame to grayscale
    gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the current and previous frames
    frame_diff = cv2.absdiff(prev_frame, gray_frame)

    # Apply a binary threshold to the difference image
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to draw bounding boxes
    for contour in contours:
        # Ignore small contours to avoid noise
        if cv2.contourArea(contour) < 1000:
            continue

        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Movement Detection", current_frame)
    cv2.imshow("Threshold", thresh)

    # Update the previous frame
    prev_frame = gray_frame

    # Break loop on 'q' key press
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
