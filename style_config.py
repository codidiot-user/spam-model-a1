# File: style_config.py
import streamlit as st

def load_css():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to right, #ff512f, #dd2476); /* Pink/Orange */
            background-attachment: fixed;
        }
        
        /* Text color must be white to stand out */
        h1, h2, h3, p, label {
            color: white !important;
        }

        /* Make the text input boxes white so users can see what they type */
        .stTextArea textarea {
            background-color: white !important;
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)
