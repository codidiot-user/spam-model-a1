import streamlit as st
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

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
except Exception as e:
    st.error(f"Model failed to load: {e}")
    st.stop()

# --- UI & LOGIC ---
st.title("🚀 Spam Detector")

# Main Input
text = st.text_area("Enter message:", height=100)

if st.button("Analyze") and text:
    # Predict
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=96)
    with torch.no_grad():
        outputs = model(**inputs)
    prob = torch.softmax(outputs.logits, dim=-1)[0][1].item()
    label = "Spam/Fake" if prob > 0.3 else "Legitimate"
    
    # Store results in Session State so they persist
    st.session_state['last_text'] = text
    st.session_state['last_label'] = label
    st.session_state['last_prob'] = prob
    st.session_state['analyzed'] = True

# Display Results
if st.session_state.get('analyzed'):
    st.divider()
    
    # Show Prediction
    lbl = st.session_state['last_label']
    score = st.session_state['last_prob']
    st.subheader(f"Result: {lbl} ({score:.1%})")
