import streamlit as st

# Set the app title
st.title("Jorge - My Streamlit App")

# Add a text input field
name = st.text_input("Enter your name")

# Display a greeting
st.write(f"Hello, {name}!")

