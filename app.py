# Load the required packages

import streamlit as st
from groq import Groq

# Init streamlit app

st.set_page_config(page_title="GenAI Project using Llama 3.3")

# Load the api key

api_key = st.secrets["API_KEY"]

# Init groq api
client = Groq(api_key= api_key)

# Write a function to generate response from model

def model_response(text: str, model_name="llama-3.3-70b-versatile"):
    stream = client.chat.completions.create(
        messages = [
            {
                "role" : "system",
                "content" : "You are a helpful assistant"
            },
            {
                "role" : "user",
                "content" : text
            }
        ],
        model = model_name,
        stream = True
    )

    for chunk in stream:
        response = chunk.choices[0].delta.content
        if response is not None:
            yield response

# Add title to streamlit app

st.title("ChatBot - Llama 3.3 MOdel")
st.subheader("by Nakul Pandit")

# Provide text for user input
user_input = st.text_area("Ask a question : ")

# create a submit button
submit = st.button("Generate", type="primary")

# If button clicked
if submit:
    st.subheader("Model Response")
    st.write_stream(model_response(user_input))
