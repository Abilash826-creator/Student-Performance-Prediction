import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("student_model.pkl")

st.set_page_config(page_title="Student Performance Prediction", page_icon="🎓")

st.title("🎓 Student Performance Prediction")

st.write("Enter the student details below:")

# User Inputs
gender = st.selectbox("Gender", ["female", "male"])

race = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parent_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox(
    "Lunch",
    ["free/reduced", "standard"]
)

test_prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

math_score = st.number_input("Math Score", 0, 100, 60)
reading_score = st.number_input("Reading Score", 0, 100, 60)
writing_score = st.number_input("Writing Score", 0, 100, 60)

# Manual Encoding
gender_map = {"female": 0, "male": 1}
race_map = {
    "group A": 0,
    "group B": 1,
    "group C": 2,
    "group D": 3,
    "group E": 4
}
parent_map = {
    "associate's degree": 0,
    "bachelor's degree": 1,
    "high school": 2,
    "master's degree": 3,
    "some college": 4,
    "some high school": 5
}
lunch_map = {
    "free/reduced": 0,
    "standard": 1
}
prep_map = {
    "completed": 0,
    "none": 1
}

if st.button("Predict"):

    data = pd.DataFrame([[
        gender_map[gender],
        race_map[race],
        parent_map[parent_education],
        lunch_map[lunch],
        prep_map[test_prep],
        math_score,
        reading_score,
        writing_score
    ]], columns=[
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course",
        "math score",
        "reading score",
        "writing score"
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")