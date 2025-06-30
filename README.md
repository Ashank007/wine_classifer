# 🍷 Wine Quality Classifier using Artificial Neural Network (ANN)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Accuracy](https://img.shields.io/badge/Test%20Accuracy-82%25-brightgreen.svg)]()
[![Model Parameters](https://img.shields.io/badge/Parameters-133%2C857-blueviolet)]()


## 📌 Overview

This project is a deep learning-based **Wine Quality Classifier** built using an **Artificial Neural Network (ANN)**.  
The model predicts the **quality score** of wine based on its **11 chemical properties** with a test accuracy of **82%** and a total of **133,857 trainable parameters**.



## 📊 Dataset Features

The dataset contains **11 input features**, all of which are **numerical** descriptors of wine chemistry:

| Feature              | Description |
|----------------------|-------------|
| Fixed Acidity        | Non-volatile acids that contribute to wine stability |
| Volatile Acidity     | Acetic acid (high values result in vinegar taste) |
| Citric Acid          | Adds freshness and flavor |
| Residual Sugar       | Sugar left after fermentation |
| Chlorides            | Salt content in wine |
| Free Sulfur Dioxide  | Prevents microbial growth |
| Total Sulfur Dioxide | Total SO₂ content |
| Density              | Wine’s density compared to water |
| pH                   | Acidity level |
| Sulphates            | Preservative in wine |
| Alcohol              | Alcohol content (%) |

The **target variable** is `quality`, a score representing wine quality on an integer scale.


## 🧠 Model Architecture

- **Input Layer**: 11 neurons (for 11 features)
- **Hidden Layers**: Fully connected dense layers with `ReLU` activation
- **Output Layer**: Sigmoid activation for classification

**Summary:**
- 🔢 **Parameters**: 133,857  
- 🧮 **Loss Function**: Categorical Crossentropy  
- ⚙️ **Optimizer**: Adam  
- 📈 **Metric**: Accuracy  
- ✅ **Training Accuracy**: ~84%  
- ✅ **Test Accuracy**: ~82%


## 🧪 Dataset Preprocessing

- ✅ Checked for missing values and outliers  
- 📊 Scaled features using **MinMaxScaler**  
- 🔀 Split dataset into **training (80%)** and **test (20%)** sets

## 🚀 Getting Started

### 🔧 Prerequisites

- Python **3.7+**
- pip installed (`pip --version`)

### 🛠 Installation

```
# Clone the repository
git clone https://github.com/Ashank007/wine_classifer.git
cd wine_classifer
```

# Install dependencies
```
pip install -r requirements.txt
```
## ▶️ Running the Model

You can launch the model using Streamlit:
```
streamlit run wineclassifer.py
```

## 📁 Project Structure
```
.
├── README.md               # Project documentation
├── requirements.txt        # Required Python packages
├── wineclassifer.py        # Streamlit app code
├── wine-classifier.h5      # Saved Keras model (HDF5 format)
└── wine-classifier.keras   # Alternative Keras format
```

## 📈 Results
Metric	Value
```
Training Accuracy	84%
Test Accuracy	82%
```

The model generalizes well on unseen data, demonstrating strong predictive performance for wine quality classification.

## 🧰 Tech Stack

- Python (3.7+)

- TensorFlow/Keras – for model building & training

- Streamlit – for app interface

- NumPy & Pandas – data manipulation

- Matplotlib & Seaborn – visualization

- Scikit-learn – scaling & evaluation

## 📄 License

This project is licensed under the MIT License.