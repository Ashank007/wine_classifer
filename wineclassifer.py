import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

@st.cache_resource
def load_trained_model():
    model_path = "/workspaces/wine_classifer/wine-classifier.keras"  
    model = load_model(model_path)
    return model

model = load_trained_model()
st.title("Wine Quality Classifier")

def number_input(label):
    value = st.text_input(label, "")
    try:
        return float(value) if value else 0.0  
    except ValueError:
        st.error(f"Invalid input for {label}. Please enter a valid number.")
        return None

fixed_acidity = number_input("Enter Fixed Acidity:")
volatile_acidity = number_input("Enter Volatile Acidity:")
citric_acid = number_input("Enter Citric Acid:")
residual_sugar = number_input("Enter Residual Sugar:")
chlorides = number_input("Enter Chlorides:")
free_sulfur_dioxide = number_input("Enter Free Sulfur Dioxide:")
total_sulfur_dioxide = number_input("Enter Total Sulfur Dioxide:")
density = number_input("Enter Density:")
pH = number_input("Enter pH:")
sulphates = number_input("Enter Sulphates:")
alcohol = number_input("Enter Alcohol:")

if st.button("Predict"):

    if None in [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                pH, sulphates, alcohol]:
        st.error("Please correct invalid inputs before proceeding.")
    else:
    
        input_data = np.array([[
            fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
            chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
            pH, sulphates, alcohol
        ]])


        prediction = model.predict(input_data)
        if prediction[0] > 0.5:
            st.success("The wine is of **Good Quality**.")
        else:
            st.error("The wine is of **Bad Quality**.")

st.info("Provide all inputs to classify the wine quality.")
