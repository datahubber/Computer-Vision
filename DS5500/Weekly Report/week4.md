Weekly Report 4

Progress Summary:
This week, significant progress was made in implementing OpenPose for landmark detection and annotation of video frames. The key achievements include:

Developed code to utilize OpenPose for extracting body and hand landmarks from video frames.

Implemented annotation of frames with key landmarks.

Successfully generated a CSV output file containing landmark data for each frame.

Used a frame rate of 30 FPS to ensure smooth data capture.

Captured and stored data for each frame, enabling further analysis.

Project Overview:
The research focuses on hand gesture tracking in videos, specifically for the game "Guess Which Hand." In this game, one player hides an object in one hand and presents both hands to another player, who then guesses which hand holds the object. The goal is to train an AI model to recognize body postures, hand positions, and subtle movements, using this game as a basis for developing posture recognition capabilities.

Methodology:

Data Collection: Video or image data capturing players' postures and hand movements during the game.

Preprocessing: Annotation and augmentation of the dataset to improve model robustness.

Pose Estimation Models: Deep learning models such as YOLO, HRNet, or OpenPose will be explored using frameworks like TensorFlow or PyTorch.

Training and Validation: Iterative model training with continuous validation to enhance accuracy.

Next Steps:

Continue refining the annotation process to ensure accuracy in landmark detection.

Implement additional preprocessing techniques to improve data quality.

Explore model training using the collected dataset.

Evaluate initial model performance and make necessary adjustments.
