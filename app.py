import streamlit as st
import joblib
import os

# Load the pre-trained model
model_path = 'C:\\Users\\AHMAD TURAB\\Desktop\\svm.pkl'  # Change this if deploying
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please check the path.")
    st.stop()

# Set the title of the app
st.title("SVM Prediction Application")

# Create input fields for user data
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
estimated_salary = st.number_input("Estimated Salary", min_value=15000, max_value=150000, value=50000)

# Encode gender input
gender_encoded = 1 if gender == "Male" else 0

# Button to make prediction
if st.button("Predict"):
    # Prepare input data for prediction
    input_data = [[gender_encoded, age, estimated_salary]]
    
    # Make prediction
    prediction = model.predict(input_data)

    # Display the prediction result
    st.write(f"Prediction: {'Purchased' if prediction[0] == 1 else 'Not Purchased'}")
