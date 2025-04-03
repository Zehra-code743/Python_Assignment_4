import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) using weight and height.
    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: BMI value
    """
    return weight / (height ** 2)

# Function to determine BMI category
def bmi_category(bmi):
    """
    Determines the BMI category based on the BMI value.
    :param bmi: Calculated BMI value
    :return: BMI category as a string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Streamlit UI
st.set_page_config(page_title="BMI Calculator", page_icon="⚖", layout="centered")
st.title("🌿 BMI Calculator")

# Styling Streamlit UI with custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    .stNumberInput>div>div>input {
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# User Input Section
st.write("Enter your details below:")
weight = st.number_input("Enter your weight in kg", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height in meters", min_value=0.5, format="%.2f")

# BMI Calculation Button
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        st.write('Build With ❤ By Shan E Zehra')
        
        # Display Results
        st.success(f"Your BMI is: {bmi:.2f}")
        st.info(f"BMI Category: {category}")
    else:
        st.error("Please enter valid numerical values for weight and height!")
