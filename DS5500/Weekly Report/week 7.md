Overview
This week marked significant progress in the "Guess Which Hand" project, where the objective is to train an AI model to predict which hand holds a small glass ball by analyzing body postures and hand movements in video data. The project leverages computer vision and deep learning techniques to track hand gestures, recognize subtle movements, and account for specific game dynamics, such as mirrored video perspectives and countdown sequences. This week's efforts focused on collecting new video data, refining the hand tracking pipeline, addressing errors in the prediction logic, and integrating advanced models like YOLOv8 and LSTM for improved detection and temporal analysis.

Tasks Completed
Data Collection:
I collected 20 new videos for the project, bringing the total dataset to a more robust size for training and evaluation. These videos capture various scenarios of the "Guess Which Hand" game, including different players, lighting conditions, and backgrounds. Each video follows the game structure: a countdown ("3, 2, 1") is displayed, after which the player opens their hand to reveal the ball, and the video stops.
Code Development and Refinement:
Initial Pipeline: Built on the previous week's work, the pipeline uses MediaPipe for hand tracking, extracting landmarks such as wrist, thumb, and finger tips to analyze hand positions and movements.
Mirror Effect Correction: Addressed a critical issue where the mirrored video perspective caused incorrect hand labeling. Since the videos are mirrored (e.g., a hand on the left side of the video is actually the right hand), I modified the code to flip MediaPipe's "Left" and "Right" hand labels accordingly.
Countdown Detection: Integrated Tesseract OCR to detect the countdown text ("3", "2", "1") in the video frames. Once the "1" is detected, the system flags the countdown as complete and prepares to lock the prediction of which hand holds the ball.
Ball Detection with YOLOv8: Incorporated YOLOv8 to detect the small glass ball in the video frames. The model was initialized with the pre-trained yolov8n.pt weights, but I noted the need for fine-tuning on a dataset specific to small glass balls for better accuracy.
Temporal Analysis with LSTM: Added an LSTM model (HandStateLSTM) to analyze the sequence of hand states (open vs. closed) over time. This helps confirm which hand is holding the ball after the countdown by modeling the transition from a closed to an open hand state.
Result Locking: Fixed an error where the prediction of which hand holds the ball (left_hand_present or right_hand_present) was changing after the countdown, even though the video stopped. I implemented logic to lock the prediction once the countdown ends and the ball is detected, ensuring consistency in the output CSV.
Dependency Installation and Debugging:
Encountered a ModuleNotFoundError for pytesseract due to missing dependencies. Installed pytesseract, ultralytics, and torch, along with Tesseract OCR on the system, to enable OCR, YOLOv8, and LSTM functionality.
Verified the installation by running the updated code, ensuring all components (MediaPipe, YOLOv8, LSTM, and OCR) work together seamlessly.
Output Generation:
The pipeline processes all videos in the directory and saves results in an output folder, with each video generating a CSV file (e.g., 000001_data_20250322_XXXXXX.csv). The CSV includes frame-by-frame data such as timestamps, hand landmarks, and predictions of which hand holds the ball.
Challenges Faced
Dependency Issues:
The initial run failed due to missing libraries (pytesseract, ultralytics, torch). This was resolved by installing the required packages and ensuring Tesseract OCR was properly set up on the system.
Solution: Provided detailed installation steps for all dependencies, including platform-specific instructions for Tesseract OCR.
Mirrored Video Perspective:
MediaPipe's hand labeling was incorrect due to the mirrored video perspective. For example, a hand on the left side of the video (labeled as "Left" by MediaPipe) was actually the right hand.
Solution: Added a label-flipping step in the pipeline to correct the hand labels based on the mirror effect.
Inconsistent Predictions Post-Countdown:
After the countdown ("3, 2, 1"), the prediction of which hand holds the ball was changing in the output CSV, even though the video stopped after the hand opened.
Solution: Implemented a locking mechanism to fix the prediction once the countdown ends and the ball is detected, ensuring the result remains consistent for all subsequent frames.
Ball Detection Accuracy:
The YOLOv8 model, using pre-trained weights (yolov8n.pt), struggled to accurately detect the small glass ball due to the lack of fine-tuning.
Next Steps: I plan to create a labeled dataset of small glass balls and fine-tune YOLOv8 to improve detection accuracy.
LSTM Model Training:
The HandStateLSTM model is currently untrained, relying on default weights. This limits its ability to accurately predict hand states (open vs. closed) and determine which hand holds the ball.
Next Steps: Collect a dataset of hand state sequences and train the LSTM model to improve temporal analysis.
Results and Observations
Dataset Growth: The addition of 20 new videos enhances the diversity of the dataset, covering more scenarios and improving the model's potential robustness.
Pipeline Functionality: The updated pipeline successfully processes all videos, corrects for the mirror effect, detects the countdown, and locks the prediction of which hand holds the ball after the countdown. The output CSV files are generated as expected, with consistent predictions post-countdown.
Model Limitations:
YOLOv8's ball detection is not yet reliable due to the lack of fine-tuning. This affects the system's ability to confirm the ball's presence after the hand opens.
The untrained LSTM model may not accurately predict hand states, leading to potential errors in determining the holding hand.
Sample Output: For a video like 000001.mp4, the output CSV correctly shows the right hand as holding the ball (after flipping labels) and maintains this prediction after the countdown, aligning with the video's content.
Next Steps for Week 8
Fine-Tune YOLOv8:
Create a labeled dataset of small glass balls using tools like Roboflow.
Fine-tune the YOLOv8 model on this dataset to improve ball detection accuracy.
Update the code to load the fine-tuned model weights.
Train the LSTM Model:
Collect a dataset of hand state sequences (open vs. closed) labeled with the correct hand holding the ball.
Train the HandStateLSTM model using PyTorch and save the trained weights.
Integrate the trained LSTM model into the pipeline for better temporal analysis.
Improve Countdown Detection:
Enhance the OCR detection of the countdown text by preprocessing video frames (e.g., adjusting contrast, cropping to the text region) to improve Tesseract's accuracy.
Explore alternative methods, such as training a small CNN to recognize the countdown digits directly.
Evaluate Model Performance:
Split the dataset into training, validation, and test sets.
Evaluate the model's accuracy in predicting which hand holds the ball, using metrics like precision, recall, and F1-score.
Iterate on the model based on validation results.
Optimize Pipeline:
Optimize the pipeline for faster processing, especially for larger datasets.
Add error handling for edge cases, such as videos with no countdown or missing ball detection.
Skills Applied and Learned
Computer Vision: Leveraged MediaPipe for hand tracking, YOLOv8 for object detection, and Tesseract OCR for text recognition.
Deep Learning: Implemented an LSTM model for temporal analysis of hand states, gaining experience with PyTorch.
Data Processing: Managed video data preprocessing and output generation in CSV format.
Debugging: Resolved dependency issues and pipeline errors, improving my troubleshooting skills in Python and computer vision projects.
Conclusion
Week 7 was a productive week for the "Guess Which Hand" project, with the successful collection of 20 new videos and significant improvements to the hand tracking pipeline. The integration of YOLOv8 and LSTM, along with corrections for the mirror effect and post-countdown prediction consistency, brings the project closer to its goal of accurately predicting which hand holds the ball. However, challenges remain in fine-tuning the YOLOv8 and LSTM models for better accuracy. The next week will focus on training these models and further refining the pipeline to ensure robust performance across all videos.

Researcher: Mian Wang

Date: March 22, 2025
