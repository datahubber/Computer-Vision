Final Report: Hand Gesture Tracking in Videos using YOLO V8 for the "Guess Which Hand" Game

**Authors:**
Mian Wang, Mohammad Toutiaee    

**Abstract:**
This project addresses the challenge of recognizing human hand gestures and postures within the context of the "Guess Which Hand" game. The primary problem is to predict which hand holds a hidden object based on video input. Using a dataset of 20 videos featuring annotated hand landmarks, this research aims to develop an AI model capable of accurately tracking hand movements and positions. The project utilizes the YOLOv8 deep learning model for pose estimation, trained after dataset preprocessing, including annotation and augmentation. The model achieved an accuracy of 85% in predicting the hand holding the object. This work contributes to advancing posture recognition, with potential applications in interactive gaming and human-computer interaction.   

**Introduction:**
The "Guess Which Hand" game serves as a practical scenario for developing and testing sophisticated AI models for human posture and gesture recognition. Accurately interpreting subtle hand movements and positions from video data presents significant challenges, including occlusions and varying lighting conditions. The objective of this project is to train a robust AI model that can analyze video footage of the game and predict the location of the hidden object. This research builds upon existing work in real-time object detection and pose estimation, specifically utilizing advancements in deep learning models like YOLO. The contribution lies in applying and evaluating these techniques for fine-grained hand gesture analysis in a dynamic game setting, aiming to improve capabilities in human-computer interaction and motion analysis.   

**Methods:**
The methodology involved several key stages:
Dataset Preparation: A dataset consisting of 20 videos capturing the "Guess Which Hand" game was collected. This dataset underwent preprocessing, which included annotating key body and hand landmarks and applying data augmentation techniques to enhance the model's robustness across diverse scenarios.   
Model Selection and Training: The YOLO (You Only Look Once) object detection model, specifically YOLOv8, was selected for its real-time pose estimation and hand gesture tracking capabilities. While other versions like v10 and v11 were tested, yielding around 70% accuracy, YOLOv8 demonstrated the best performance based on evaluation metrics. The model was trained using frameworks like TensorFlow or PyTorch on the preprocessed dataset.   
Landmark Generation and Prediction: The trained model was used to generate key hand landmarks (e.g., wrist, thumb, index finger) from the video data. Based on the tracked gestures and landmark positions, the model predicted which hand held the object. These predictions were saved in CSV format for further analysis.   

**Experimental Results (Evaluation):**
The performance of the YOLOv8 model was evaluated on the collected video dataset. The primary metric was the accuracy of predicting the hand holding the hidden object.
Prediction Accuracy: The model achieved an accuracy of 85% in correctly identifying the hand holding the object.   

**Discussion (Analysis):**
The results demonstrate the effectiveness of the YOLOv8 model in tracking hand gestures and predicting the hidden object's location in the "Guess Which Hand" game with high accuracy (85%). This indicates the model's capability to handle challenges like subtle movements, occlusions, and varying conditions inherent in real-world video data.   
Impact: This project successfully highlights the potential of AI in interpreting complex human gestures.   
Beneficiaries: The findings can benefit developers and researchers in areas such as interactive gaming, human-computer interaction (HCI), virtual reality, and motion analysis systems.   
Decision Making: The developed techniques could inform the design of more intuitive interfaces or systems that rely on gesture recognition.
Future Work: Future improvements could involve expanding the dataset with more diverse scenarios and participants, exploring different deep learning architectures or fusion models, and refining the model to handle a wider range of gestures or occlusions more effectively. Integrating real-time feedback mechanisms could also enhance interactive applications.

**Statement of Contributions:**
Mian Wang: Responsible for dataset preparation, model selection and training (YOLOv8), landmark generation, results evaluation, and report/poster creation. Mohammad Toutiaee helped with dataset preparation and provided feedback and guidance.  

**Conclusion:**
This project successfully developed and evaluated an AI model using YOLOv8 for hand gesture tracking in the "Guess Which Hand" game, achieving 85% prediction accuracy. It demonstrates the feasibility of using deep learning for detailed posture and gesture analysis from video data. The research contributes to the fields of computer vision and human-computer interaction, offering a foundation for future advancements in gesture-based applications.   

**References:**
Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). You Only Look Once: Unified, Real-Time Object Detection. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 779-788. https://doi.org/10.1109/CVPR.2016.91    
