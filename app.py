import streamlit as st
import pandas as pd
from utils import generate_prompt, call_openrouter

# Page config
st.set_page_config(page_title="Startup Analyst", page_icon="🚀", layout="centered")

# Custom CSS for spacing
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
        }
        .stRadio label {
            font-weight: bold;
        }
        .custom-radio {
            display: flex;
            gap: 2rem;
            align-items: center;
        }
        .custom-radio label {
            display: flex;
            align-items: center;
            font-size: 1.05rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("🚀 Startup Analyst")
st.caption("Leverage AI to get instant insights into startups — upload a file or enter details manually.")

# Choice label
st.markdown("### 🔍 Choose How to Provide Startup Data")

# Horizontal input method radio
col1, col2 = st.columns([1, 1])
with col1:
    input_method = st.radio("Input Method", ["📝 Enter Manually", "📂 Upload CSV File"], index=0, label_visibility="collapsed")

# --- Input UI Logic ---

# Manual Entry First (Default)
if input_method == "📝 Enter Manually":
    st.markdown("#### 🧾 Enter Startup Details")
    with st.form("manual_input", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            startup_name = st.text_input(
                "🔹 Startup Name",
                placeholder="e.g. Physics Wallah"
            )
            founders = st.text_input(
                "👥 Founders",
                placeholder="e.g. Alakh Pandey, Prateek Maheshwari"
            )
            funding = st.text_input(
                "💰 Funding",
                placeholder="e.g. ₹777 Cr in Series A from WestBridge, GSV Ventures"
            )

        with col2:
            website = st.text_input(
                "🌐 Website",
                placeholder="e.g. https://www.pw.live"
            )
            category = st.text_input(
                "🏷️ Category",
                placeholder="e.g. EdTech, Online Learning"
            )
            description = st.text_area(
                "📝 Description",
                placeholder="Brief description of the startup...\n\nExample: Physics Wallah is an Indian edtech platform offering affordable online coaching for JEE, NEET, and other competitive exams, founded by educator Alakh Pandey."
            )

        submitted = st.form_submit_button("🚀 Analyze Startup")

        if submitted:
            if not startup_name or not description:
                st.warning("⚠️ Please fill in at least the Startup Name and Description.")
            else:
                row = {
                    "Startup Name": startup_name,
                    "Description": description,
                    "Founders": founders,
                    "Funding": funding,
                    "Website": website,
                    "Category": category
                }
                st.markdown("---")
                st.subheader(f"📊 Analysis for **{startup_name}**")
                prompt = generate_prompt(row)
                with st.spinner("🔎 Analyzing startup info..."):
                    try:
                        result = call_openrouter(prompt)
                        st.markdown(result)
                    except Exception as e:
                        st.error("❌ Error calling GPT: " + str(e))



# CSV Upload Section
elif input_method == "📂 Upload CSV File":
    st.markdown("#### 📄 Upload your CSV file")
    uploaded_file = st.file_uploader("Choose a CSV file with startup data", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")
        for idx, row in df.iterrows():
            st.markdown("---")
            st.subheader(f"📊 Analysis for **{row['Startup Name']}**")
            prompt = generate_prompt(row)
            with st.spinner("🔎 Analyzing startup info..."):
                try:
                    result = call_openrouter(prompt)
                    st.markdown(result)
                except Exception as e:
                    st.error("❌ Error calling GPT: " + str(e))
