Progress Summary:
This week, I started implementing YOLO for object detection in the video to identify which hand, if any, contains the object. The key steps attempted include:

Setting up YOLO for object detection and testing initial configurations.

Running YOLO on sample video frames to detect the object and extract bounding boxes.

Updating the CSV file with initial results, marking frames where the object is detected.

Identifying challenges in differentiating the object from background noise and ensuring accurate detection.

Challenges Encountered:

The object is only visible in a few frames, making detection challenging.

Some frames have false positives or failed detections due to motion blur and occlusions.

Refining object detection thresholds to balance accuracy and sensitivity.

Next Steps:

Fine-tune YOLO parameters to improve object detection accuracy.

Implement post-processing techniques to filter out false positives.

Fully update the CSV file with labeled frames indicating object presence.

Conduct further testing and validation to ensure reliable detection results.

Skills and Tools Utilized:

Object Detection with YOLO

Video Frame Processing

CSV Data Annotation

Python, OpenCV, TensorFlow/PyTorch

