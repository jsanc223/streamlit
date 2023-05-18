import streamlit as st
import pandas as pd

# Set the app title
st.title("Jorge - My Streamlit App")

# Add a text input field
name = st.text_input("Enter your name")

# Display a greeting
st.write(f"Hello, {name}!")

# Create a simple pandas DataFrame
df = pd.DataFrame({
    'first column': list(range(1, 5)),
    'second column': list(range(5, 9))
})

# Display the DataFrame in the app
st.write(df)
