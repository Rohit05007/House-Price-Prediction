import streamlit as st
import pandas as pd
from model_loader import load_model

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="House Price AI",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction App")
st.write("Fill all details carefully before prediction")

# ---------------- LOAD MODEL ----------------
try:
    model = load_model()
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ---------------- INPUT FIELDS ----------------
st.header("📌 Enter Property Details")

longitude = st.number_input("Longitude", value=0.0)
latitude = st.number_input("Latitude", value=0.0)
housing_median_age = st.number_input("Housing Median Age", value=0.0)

total_rooms = st.number_input("Total Rooms", value=0.0)
total_bedrooms = st.number_input("Total Bedrooms", value=0.0)

population = st.number_input("Population", value=0.0)
households = st.number_input("Households", value=0.0)

median_income = st.number_input("Median Income", value=0.0)

st.subheader("🌊 Ocean Proximity")

inland = st.selectbox("INLAND", [0, 1])
island = st.selectbox("ISLAND", [0, 1])
near_bay = st.selectbox("NEAR BAY", [0, 1])
near_ocean = st.selectbox("NEAR OCEAN", [0, 1])

# ---------------- PREDICTION ----------------
st.markdown("---")

if st.button("🚀 Predict House Price", use_container_width=True):

    if (
        longitude == 0 or
        latitude == 0 or
        housing_median_age == 0 or
        total_rooms == 0 or
        total_bedrooms == 0 or
        population == 0 or
        households == 0 or
        median_income == 0
    ):
        st.error("⚠️ Please fill all fields before prediction.")
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

        try:
            prediction = model.predict(input_data)[0]

            st.success("🎯 Prediction Successful!")
            st.subheader("🏠 Estimated House Price")
            st.success(f"💰 ${prediction:,.2f}")

        except Exception as e:
            st.error(f"Prediction Error: {e}")
            
