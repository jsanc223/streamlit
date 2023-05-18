import streamlit as st
from transformers import pipeline

# Initialize the translation pipeline
translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")

# Set the app title
st.title("Jorge - My Streamlit App")

# Add a text input field
#name = st.text_input("Enter your name")

# Display a greeting
#st.write(f"Hello, {name}!")

# Add a text input field for the text to translate
text_to_translate = st.text_input("Enter some text to translate to Spanish")

# Only translate if there is text to translate
if text_to_translate:
    # Use the translator to translate the text
    translation = translator(text_to_translate)[0]['translation_text']

    # Display the translated text
    st.write(translation)
