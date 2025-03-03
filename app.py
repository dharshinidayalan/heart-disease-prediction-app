import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

# Streamlit App Title
st.title("Heart Disease Prediction App")

# User Input Fields
age_category = st.selectbox("Age Category", [
    "18-24", "25-29", "30-34", "35-39", "40-44", "45-49", 
    "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80 or older"
])
sex_male = st.radio("Sex", ["Male", "Female"])
smoking_yes = st.radio("Do you smoke?", ["Yes", "No"])
race_white = st.radio("Race", ["White", "Other"])
mental_health = st.slider("Mental Health (Bad days in last 30 days)", 0, 30, 5)
sleep_time = st.slider("Average Sleep Time (Hours)", 1, 12, 7)
physical_health = st.slider("Physical Health (Bad days in last 30 days)", 0, 30, 5)
bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=25.0)
physical_activity_yes = st.radio("Do you engage in physical activity?", ["Yes", "No"])
gen_health_good = st.radio("Is your general health good?", ["Yes", "No"])

# Convert categorical values to numerical format
age_mapping = {
    "18-24": 1, "25-29": 2, "30-34": 3, "35-39": 4, "40-44": 5,
    "45-49": 6, "50-54": 7, "55-59": 8, "60-64": 9, "65-69": 10,
    "70-74": 11, "75-79": 12, "80 or older": 13
}
age_category = age_mapping[age_category]
sex_male = 1 if sex_male == "Male" else 0
smoking_yes = 1 if smoking_yes == "Yes" else 0
race_white = 1 if race_white == "White" else 0
physical_activity_yes = 1 if physical_activity_yes == "Yes" else 0
gen_health_good = 1 if gen_health_good == "Yes" else 0

# Prediction Button
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[age_category, sex_male, smoking_yes, race_white, mental_health, sleep_time, 
                            physical_health, bmi, physical_activity_yes, gen_health_good]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display Result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease!")
    else:
        st.success("✅ Low Risk of Heart Disease.")
