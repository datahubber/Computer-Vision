Project Overview:
The research focuses on hand gesture tracking in videos, specifically for the game "Guess Which Hand." The objective is to train an AI model to recognize body postures, hand positions, and subtle movements, using this game as a basis for developing posture recognition capabilities.

Progress Summary:

Implemented OpenPose for extracting body and hand landmarks from video frames.

Developed annotation techniques for accurate frame labeling.

Successfully generated a CSV output file containing landmark data for each frame.

Captured video data at 30 FPS for precise motion tracking.

Conducted initial exploratory data analysis (EDA) to assess data quality and coverage.

Data Collection Summary:

Data Description:

The dataset consists of video frames annotated with key body and hand landmarks.

CSV files store numerical representations of landmark positions.

Key Findings from EDA:

Verified consistency of extracted landmarks.

Identified some minor annotation errors that require refinement.

Plotted sample hand trajectories to confirm movement patterns.

Challenges Encountered:

Handling variability in hand positions due to different player postures.

Ensuring accurate annotations across frames.

Balancing data preprocessing with computational efficiency.

Next Steps:

Improve annotation accuracy and preprocessing techniques.

Train an initial deep learning model using YOLO, HRNet, or OpenPose.

Validate model performance and refine parameters.

Expand the dataset to improve generalization and robustness.

Skills and Tools Utilized:

Computer Vision

Machine Learning

Data Annotation

Motion Tracking

OpenPose, TensorFlow/PyTorch

The project has made progress in data collection and preprocessing, setting a strong foundation for the next phase of model training and evaluation.
