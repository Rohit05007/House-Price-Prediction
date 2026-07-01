import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="House Price AI", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction AI App")
st.write("Fill all details carefully before prediction")

# ---------------- LOAD MODEL ----------------
model_path = os.path.join("model", "house_price_model.pkl")

if not os.path.exists(model_path):
    st.error("❌ Model file not found in 'model/house_price_model.pkl'")
    st.stop()

model = joblib.load(model_path)

# ---------------- INPUT FIELDS ----------------
st.header("📌 Enter Property Details")

longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
housing_median_age = st.number_input("Housing Median Age")

total_rooms = st.number_input("Total Rooms")
total_bedrooms = st.number_input("Total Bedrooms")

population = st.number_input("Population")
households = st.number_input("Households")

median_income = st.number_input("Median Income")

st.subheader("🌊 Ocean Proximity (Select 1 if true else 0)")

inland = st.selectbox("INLAND", [0, 1])
island = st.selectbox("ISLAND", [0, 1])
near_bay = st.selectbox("NEAR BAY", [0, 1])
near_ocean = st.selectbox("NEAR OCEAN", [0, 1])

# ---------------- PREDICTION ----------------
st.markdown("---")

if st.button("🚀 Predict House Price"):

    # ✅ Validation (NO ZERO INPUT ALLOWED)
    if (
        longitude == 0 or latitude == 0 or
        housing_median_age == 0 or
        total_rooms == 0 or
        total_bedrooms == 0 or
        population == 0 or
        households == 0 or
        median_income == 0
    ):
        st.error("⚠️ Please fill all fields before prediction (0 not allowed)")
    else:

        input_data = pd.DataFrame([[
            longitude,
            latitude,
            housing_median_age,
            total_rooms,
            total_bedrooms,
            population,
            households,
            median_income,
            inland,
            island,
            near_bay,
            near_ocean
        ]], columns=[
            "longitude",
            "latitude",
            "housing_median_age",
            "total_rooms",
            "total_bedrooms",
            "population",
            "households",
            "median_income",
            "ocean_proximity_INLAND",
            "ocean_proximity_ISLAND",
            "ocean_proximity_NEAR BAY",
            "ocean_proximity_NEAR OCEAN"
        ])

        prediction = model.predict(input_data)[0]

        st.success("🎯 Prediction Successful!")

        st.write("### 🏠 Estimated House Price")
        st.write(f"💰 **{prediction:,.2f}**")