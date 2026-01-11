# File: app.py (The Home Page)
import streamlit as st

# Set page config MUST be the first line
st.set_page_config(
    page_title="AI Spam Detector",
    page_icon="🚀",
    layout="centered"
)

import os
# Set tokenizer parallelism BEFORE importing transformers
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Import our custom CSS
from style_config import load_css

# --- LOAD CUSTOM CSS ---
load_css()

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    model_path = "logesh1962/sms-spam-detector" 
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    return tokenizer, model

try:
    tokenizer, model = load_model()
except:
    st.error("Model failed to load.")
    st.stop()

# --- MAIN PAGE UI ---

st.title("🚀 AI Spam Detector")
st.markdown("### Intelligent protection against scams.")
st.write("Paste your message below. Our fine-tuned RoBERTa model will analyze its content to determine if it's safe or potentially harmful.")

# Main Input Container
with st.container():
    text = st.text_area("Put your message here to test:", height=120, placeholder="e.g. 'URGENT! You've won a prize. Click link to claim...'")
    
    col_spacer1, col_btn, col_spacer2 = st.columns([1, 2, 1])
    with col_btn:
        analyze_button = st.button("🔍 Analyze Message", use_container_width=True)

if analyze_button and text:
    with st.spinner("Analyzing patterns..."):
        # Predict
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=96)
        with torch.no_grad():
            outputs = model(**inputs)
        prob = torch.softmax(outputs.logits, dim=-1)[0][1].item()
        label = "Spam/Fake" if prob > 0.3 else "Legitimate"
        
        # Store results in Session State
        st.session_state['last_text'] = text
        st.session_state['last_label'] = label
        st.session_state['last_prob'] = prob
        st.session_state['analyzed'] = True

# Display Results
if st.session_state.get('analyzed'):
    st.divider()
    st.header("Analysis Results")
    
    lbl = st.session_state['last_label']
    score = st.session_state['last_prob']
    
    # Visual Result Banner
    if lbl == "Legitimate":
        st.success(f"**✅ Prediction: {lbl.upper()}** (Confidence Score: {1-score:.1%})")
        st.caption("This message appears safe.")
    else:
        st.error(f"**🚨 Prediction: {lbl.upper()}** (Confidence Score: {score:.1%})")
        st.warning("⚠️ Be cautious. This message shows patterns common in phishing or scams.")
