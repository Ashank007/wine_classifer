# Wine Classifier with Artificial Neural Network

## Overview
This project is a **Wine Quality Classifier** built using an **Artificial Neural Network (ANN)**. The classifier predicts the quality of wine based on its chemical properties. The model achieves an accuracy of **84%** and was trained with **133,857 parameters**. 

## Dataset
The dataset used in this project consists of **11 features** that represent the chemical properties of wine. These features are:

- **Fixed Acidity**: Non-volatile acids involved in wine stability.
- **Volatile Acidity**: Acetic acid in wine that leads to an unpleasant vinegar taste.
- **Citric Acid**: Adds freshness and flavor to wine.
- **Residual Sugar**: The amount of sugar remaining after fermentation.
- **Chlorides**: Salt content in the wine.
- **Free Sulfur Dioxide**: SO₂ that is not bound and helps prevent microbial growth.
- **Total Sulfur Dioxide**: The total amount of SO₂ (bound and free).
- **Density**: The wine's mass relative to water.
- **pH**: Measure of wine's acidity.
- **Sulphates**: Adds to wine's sulfur dioxide levels for preservation.
- **Alcohol**: Alcohol content in wine.
- **Quality**: Target variable; wine quality score (integer).

## Model Architecture
The model is built using an **Artificial Neural Network (ANN)**. 

### Key Details:
- **Parameters**: 133,857
- **Layers**: 
  - **Input Layer**: 11 neurons (one for each feature)
  - **Hidden Layers**: Fully connected layers with appropriate activation functions
  - **Output Layer**: Neurons for classification
- **Activation Functions**: 
  - **Hidden layers**: ReLU (Rectified Linear Unit)
  - **Output layer**: Softmax (for multi-class classification)

### Training
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Evaluation Metric**: Accuracy
- **Training Accuracy**: 84%

## Dependencies
The project is implemented in Python and uses the following libraries:
- **TensorFlow/Keras**: For building and training the ANN.
- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and preprocessing.
- **Matplotlib/Seaborn**: For data visualization.
- **Scikit-learn**: For data splitting and evaluation metrics.

## Getting Started
Follow these steps to run the project on your system.

### Prerequisites
Ensure that Python 3.7 or later is installed on your system. 

### Installation
1. Clone this repository:
   ```bash
   git clone <https://github.com/Ashank007/wine_classifer>

2. Navigate to the project directory:
    cd wine-classifier
3. Install the required dependencies:
    pip install -r requirements.txt

## Dataset Preprocessing
The dataset was preprocessed using the following steps:
1. Checked for missing values and outliers.
2. Scaled the features using MinMaxScaler to normalize the data.
3. Split the dataset into training and test sets (80:20 ratio).

## Results
1. The model was evaluated on the test set and achieved:
    Accuracy: **84%**

## Performance Insights
The model demonstrates strong predictive capabilities for identifying wine quality based on its chemical composition.
