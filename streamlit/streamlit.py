
import streamlit as st

# Add a title to the sidebar
st.sidebar.title("Sidebar Title")

# Add a slider to the sidebar
slider_value = st.sidebar.slider("Select a value", 0, 100, 50)

# Add a selectbox to the sidebar
selectbox_value = st.sidebar.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

# Display the selected values in the main page
st.write("Slider value:", slider_value)
st.write("Selected option:", selectbox_value)