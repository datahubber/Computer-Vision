import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open video stream from webcam.")
    exit()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture video frame.")
        break

    # Apply Canny edge detection
    edges = cv2.Canny(frame, 100, 200)

    # Display the raw video feed
    cv2.imshow('Raw Video Feed', frame)

    # Display the Canny edge detector video feed
    cv2.imshow('Canny Edge Detector', edges)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()
