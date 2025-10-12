import streamlit as st

st.set_page_config(page_title="Dynamic Pricing - Airbnb", layout="wide")

st.title("🏠 Airbnb Dynamic Pricing Dashboard")
st.markdown("""
Welcome to the **Dynamic Pricing App**!

This dashboard allows you to explore and analyze Airbnb pricing trends using data and machine learning insights.
""")

# Example input section
st.header("🔢 Predict Price")
neighborhood = st.text_input("Neighborhood")
bedrooms = st.slider("Number of Bedrooms", 1, 10, 2)
bathrooms = st.slider("Number of Bathrooms", 1, 5, 1)
nights = st.slider("Number of Nights", 1, 30, 3)

# Dummy model example (replace with your own model later)
predicted_price = 5000 + (bedrooms * 2000) + (bathrooms * 1500)
st.metric(label="Estimated Price (KSh)", value=f"{predicted_price:,.0f}")

st.success("Model prediction demo complete — replace this with your trained model later!")
