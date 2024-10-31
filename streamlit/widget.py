import streamlit as st
import pandas as pd
st.title("streamlit Text input")

name = st.text_input("Enter your name")

age = st.slider("select you age", 1, 100,25)

if name:
    st.write(f"Hello {name}")
    
if age:
    st.write("your age is " + str(age))
    
options = ['pythons', 'java', 'c++', 'ruby']
choice = st.selectbox("select your language", options)
st.write("you selected", choice)

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
})

st.write("here is the df")
st.write(df)

uploaded_file = st.file_uploader("choose a csv file",type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("uploaded df")
    st.write(df)