
import streamlit as st
st.sidebar.title("Sidebar Title")

slider_value = st.sidebar.slider("Select a value", 0, 100, 50)

selectbox_value = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

st.write("Slider value:", slider_value)
st.write("Selected option:", selectbox_value)