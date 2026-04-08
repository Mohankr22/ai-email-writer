import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("AI Email Writer")

purpose = st.text_input("Enter Purpose")
tone = st.selectbox("Select Tone", ["Formal", "Friendly", "Apology", "Request"])

points = st.text_area("Enter Key Points")

if st.button("Generate Email"):

    prompt = f"""
    Write an email based on:

    Purpose: {purpose}
    Tone: {tone}
    Key Points: {points}

    Give output in this format:
    1. Professional Email
    2. Follow-up Email
    3. Short Version
    4. 5 Subject Lines
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Groq supported model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )  
    

    st.write(response.choices[0].message.content)