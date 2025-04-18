import streamlit as st
import pandas as pd
from utils import generate_prompt, call_openrouter

st.set_page_config(page_title="Startup Analyst", page_icon="🚀")
st.title("🚀 AI-Powered Startup Analyst")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    for idx, row in df.iterrows():
        st.subheader(f"📊 Analysis for {row['Startup Name']}")
        prompt = generate_prompt(row)
        with st.spinner("Analyzing..."):
            try:
                result = call_openrouter(prompt)
                st.markdown(result)
            except Exception as e:
                st.error("Error calling GPT: " + str(e))
