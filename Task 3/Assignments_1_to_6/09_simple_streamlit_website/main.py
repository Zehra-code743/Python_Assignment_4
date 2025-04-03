import streamlit as st
import random
import datetime

# Set page configuration
st.set_page_config(page_title="📅 Simple Calendar App", page_icon="📆", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .stSelectbox>div>div {
        border-radius: 10px;
        padding: 10px;
        color: black !important;
        background-color: white !important;
    }
    .stSelectbox div[data-baseweb="select"]>div {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🌟 Welcome to My Beautiful Calendar App")
st.write("This app will display a random date between 1st January 2025 and 31st December 2025.")

# Generate a random date
random_day = random.randint(1, 365)
random_date = datetime.datetime(2025, 1, 1) + datetime.timedelta(days=random_day - 1)

# Display the random date
st.success(f"📆 The random date is: {random_date.strftime('%B %d, %Y')}")

# User input for month and year
month = st.selectbox("Select a month", [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
])
year = st.selectbox("Select a year", [2025, 2026, 2027, 2028, 2029, 2030])

# Calculate the number of days in the selected month
month_days = {
    "January": 31, "February": 29 if year % 4 == 0 else 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31, "September": 30,
    "October": 31, "November": 30, "December": 31
}
num_days = month_days[month]

# Validate the selected date
if random_date.day > num_days:
    st.error(f"🚨 The selected date is not valid for {month} {year}")
else:
    st.success(f"✅ The selected date is valid for {month} {year}")
    st.info(f"📅 The random date falls on {month} {random_date.day}, {year}")
    st.write(f"🔜 The next date after the random date is: {month} {(random_date.day + 1) % num_days + 1}, {year}")
    st.write(f"🔙 The previous date before the random date is: {month} {(random_date.day - 1) % num_days + 1}, {year}")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Build With ❤️ By Shan-E-Zehra</p>", unsafe_allow_html=True)
