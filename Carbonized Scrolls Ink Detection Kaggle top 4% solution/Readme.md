# Situation
Nearly 2000 years ago, the eruption of Mount Vesuvius buried a Roman villa in Herculaneum, next to Pompeii, preserving a library of thousands of scrolls. These scrolls, carbonized by the volcano’s heat, became impossible to open without breaking. Discovered a few hundred years ago, the scrolls have awaited modern techniques to uncover their contents. Recent advances now provide an opportunity to read these scrolls using 3D X-ray scans, despite the ink not being readily visible in such scans.  

# Task
Participants in the $100,000 Vesuvius Challenge are tasked with detecting ink on the carbonized scrolls and enabling their contents to be read. The primary goal is to use 3D X-ray scans and modern machine learning techniques to identify ink traces and reconstruct the texts. This sub-competition focuses on the challenge of detecting ink on fragments of the scrolls, supported by aligned datasets of X-ray scans, infrared photographs, and hand-labeled binary masks indicating ink presence.  

# Action
utilizes deep learning, specifically a U-Net-based segmentation model with a ResNet encoder, to identify regions likely containing ink. The decoder consists of two stages, with the first stage operating on multiple 2D slices from the 3D volume and the second stage refining the results. Includes attention mechanisms to improve the model's focus on relevant features. Mixup augmentations and Test Time Augmentations (TTA). Applies post-processing using a denoising algorithm to clean up predictions.  

# Result
Silver medal, rank 46th out of 1249 teams.
