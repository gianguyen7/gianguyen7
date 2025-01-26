## Distinguishing AI-Generated Images from Real Photography
This repository contains the work completed for the project **"Distinguishing AI-Generated Images from Real Photography"**, as part of the **UC Berkeley MIDS W207: Applied Machine Learning** course in Summer 2024.

### Overview
#### Why This Matters
By 2026, an estimated 90% of online content could be synthetically generated using AI, posing challenges to media integrity, cybersecurity, and public trust in visual content. This project explores methods to identify AI-generated images and offers insights into improving model performance while addressing ethical concerns.

#### Objectives
- Enhance media integrity by verifying image authenticity.
- Improve AI/ML models for robust image classification.
- Detect and prevent the spread of deepfakes and manipulated images.
- Address ethical issues related to content manipulation in media.

### Dataset and Architecture
#### Dataset
- Source: [Kaggle Dataset - AI vs Real Images](https://www.kaggle.com/datasets/tristanzhang32/ai-generated-images-vs-real-images)
- Composition:
    - AI-generated images: 24,0006
    - Real photographs: 24,000
    - Train set: 38,650 images
    - Test set: 3,000 images

From the original dataset, we manually annotated the data to exclude paintings, drawings, and any synthetic images that might confuse the machine learning model.
#### Data Engineering Workflow
1. Upload dataset to AWS S3 bucket
2. Preprocess data on an EC2 instance using batch processing
3. Store interim datasets back in S3
4. Load interim datasets for modeling and evaluation

### Methodology
#### Data Preprocessing
- Cleaning: Removed corrupted and incomplete images.
- Augmentation: Rotated, flipped, and adjusted brightness and contrast to create additional training samples.
- Normalization: Standardized pixel values for consistent input scaling.
- Resizing: Adjusted all images to uniform dimensions required by CNN models.

#### Models
1. Baseline Model (Dummy Classifier):
    - Accuracy: Training (57.6%), Validation (57.8%)
2. Simple CNN:
    - Accuracy: Training (73.5%), Validation (65.6%)
3. CNN with Hyperparameter Tuning:
    - Accuracy: Training (84.8%), Validation (82.2%), Test (79.8%)

### Results
- The tuned CNN effectively balances precision and recall, achieving robust performance in detecting both real and AI-generated images.
- The model struggles with artwork and paintings due to textual complexities.

### Challenges and Limitations
- Computation: Limited processing power without GPU access restricted full dataset utilization.
- Data Diversity: The dataset lacked sufficient variability in styles and subjects.
- Annotation Bias: Manual annotation introduced potential inconsistencies.

### Future Work
- Expand computational resources to process the entire dataset.
- Introduce more diverse datasets for better generalization.
- Experiment with advanced hyperparameters and architectures.
- Enhance sensitivity and specificity to reduce misclassification.

### Tools and Technologies
- Cloud: AWS S3, EC2
- Programming: Python, TensorFlow
- Libraries:
    - Data manipulation: pandas, numpy
    - Visualization: matplotlib, seaborn
    - Machine learning: TensorFlow, scikit-learn

### Authors
- Gia Nguyen
- Akin Akinlabi
- Cat Weiss
- Deva Empranthiri
