# File: style_config.py
import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* --- Global App Styling --- */
        .stApp {
            # background: linear-gradient(to right bottom, #0f0c29, #302b63, #24243e); # Optional darker gradient background
            background-color: #f4f6f9; # A clean light gray background
        }
        
        /* --- Containers and Cards --- */
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        /* --- Custom headers --- */
        h1 {
            color: #1a237e;
            font-weight: 800;
        }
        h2, h3 {
            color: #283593;
        }

        /* --- Stylish Buttons --- */
        .stButton>button {
            background: linear-gradient(45deg, #4b6cb7, #182848);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.5rem 1.5rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(75, 108, 183, 0.4);
        }
        
        /* --- Metrics Styling (for About Page) --- */
        [data-testid="stMetricValue"] {
            color: #1a237e;
            font-size: 2.5rem !important;
        }
        </style>
    """, unsafe_allow_html=True)
