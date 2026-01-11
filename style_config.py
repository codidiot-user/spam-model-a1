# File: style_config.py
import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def load_css():
    # Make sure 'assets/background.jpg' exists or change the name below!
    # For now, let's assume you put an image named 'background.jpg' in assets
    # img_file = "assets/image_3041af.jpg" 
    
    # If you don't have a background image ready, use this placeholder URL:
    background_url = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b"
    
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{background_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* Add a semi-transparent black box behind text so it's readable */
        .stMarkdown, h1, h2, h3 {{
            background-color: rgba(0, 0, 0, 0.6); 
            padding: 10px;
            border-radius: 10px;
            color: white !important;
        }}
        </style>
    """, unsafe_allow_html=True)
