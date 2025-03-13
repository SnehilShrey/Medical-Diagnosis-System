import streamlit as st
import pickle
import numpy as np
import base64

# Load the models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
lung_disease_model = pickle.load(open('lungs_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
stroke_model = pickle.load(open('stroke_model.sav', 'rb'))
thyroid_model = pickle.load(open('Thyroid_model.sav', 'rb'))

# Add background image
def add_bg_from_local():
    with open("background.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
        }}
       .cloud-box {{
            background: #9A00CC; 
            padding: 15px;
            border-radius: 20px;
            text-align: center;
            font-weight: bold;
            font-size: 36px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
        }}
        .center-heading {{
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            width: 100%;
        }}
        .prediction-output {{
            background: #ffcccc;
            padding: 15px;
            border-radius: 20px;
            font-size: 20px;
            font-weight: bold;
        }}
        .cloud-box-left {{
            text-align: left;
            background: #FFB6C1;
            padding: 10px;
            border-radius: 20px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Streamlit app
def main():
    add_bg_from_local()
    st.markdown('<div class="cloud-box center-heading"style="margin-bottom: 60px;">⚕️Disease Prediction System🩺</div>', unsafe_allow_html=True)
    
    # Dropdown for selecting disease
    st.markdown(
    '<div class="cloud-box-left" style="font-size:18px; font-weight:bold; margin-bottom:-40px;">'
    'Select Disease for Prediction</div>', 
    unsafe_allow_html=True
    )
    disease = st.selectbox("", ['Diabetes', 'Heart Disease', 'Lung Disease', 'Parkinson’s Disease', 'Stroke', 'Hypo-Thyroid'])

    st.markdown('<div style="margin-bottom: 20px;"></div>', unsafe_allow_html=True)
    
    input_labels = []  # Initialize an empty list
    inputs = []  # Initialize inputs list before condition

    if disease == 'Diabetes':
        input_labels = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

    elif disease == 'Heart Disease':
        input_labels = ['Age', 'Sex', 'Chest Pain', 'Resting BP', 'Cholesterol', 'Fasting BS', 'Resting ECG', 'Max HR', 'Exercise Angina', 'Oldpeak', 'Slope', 'CA', 'Thal']

    elif disease == 'Lung Disease':
        input_labels = ['Gender', 'Age', 'Smoking', 'Yellow Fingers', 'Anxiety', 'Peer Pressure', 'Chronic Disease', 'Fatigue', 'Allergy', 'Wheezing', 'Alcohol Consuming', 'Coughing', 'Shortness of Breath', 'Swallowing Difficulty', 'Chest Pain']

    elif disease == 'Parkinson’s Disease':
        input_labels = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'Spread1', 'Spread2', 'D2', 'PPE', 'MDVP:Shimmer(dB)']

    elif disease == 'Stroke':
        input_labels = ['ID', 'Gender', 'Age', 'Hypertension', 'Heart Disease', 'Ever Married', 'Work Type', 'Residence Type', 'Average Glucose Level', 'BMI', 'Smoking Status', 'Stroke History', 'Physical Activity', 'Diet', 'Stress Level', 'Sleep Hours', 'Blood Pressure']

    elif disease == 'Hypo-Thyroid':
        input_labels = ['Age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI', 'Sex']

    # Create input fields inside cloud box for each parameter
    for label in input_labels:
        st.markdown(f'<div class="cloud-box-left"style="font-size:16px; margin-bottom: 5px;">{label}</div>', unsafe_allow_html=True)  # Cloud box for each label
        value = st.number_input(label, label_visibility="collapsed")  # Input field
        inputs.append(value)

    prediction = None  
    
    if st.button('Predict'):
        model = None
    
        if disease == 'Diabetes':
            model = diabetes_model
        elif disease == 'Heart Disease':
            model = heart_disease_model
        elif disease == 'Lung Disease':
            model = lung_disease_model
        elif disease == 'Parkinson’s Disease':
            model = parkinsons_model
        elif disease == 'Stroke':
            model = stroke_model
        elif disease == 'Hypo-Thyroid':
            model = thyroid_model

        if model:  # Ensure model is not None before prediction
            result = model.predict([inputs])
            prediction = 'Positive' if result[0] == 1 else 'Negative'
        
        # Show prediction result in the cloud box with light red-orange color
        st.markdown(f'<div class="prediction-output">{disease} Prediction: {prediction}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()