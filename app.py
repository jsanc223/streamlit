import streamlit as st
from transformers import pipeline

# Initialize the translation and summarization pipelines
translator = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Set the app title
st.title("Jorge -  NLP App")

# Add a radio button to select the task
task = st.radio("Choose a task", ("Translation (English to Spanish)", "Text Summarization"))

# Add a text area input field for the text to process
text_to_process = st.text_area("Enter some text", value="")

# Add a submit button to run the selected task
if st.button("Apply"):

    # Only process if there is text
    if text_to_process:

        if task == "Translation (English to Spanish)":
            # Use the translator to translate the text
            processed_text = translator(text_to_process)[0]['translation_text']

        elif task == "Text Summarization":
            # Use the summarizer to summarize the text
            processed_text = summarizer(text_to_process, do_sample=False)[0]['summary_text']

        # Display the processed text
        st.write(f'Processed text: {processed_text}')
