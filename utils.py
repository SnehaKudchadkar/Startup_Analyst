import requests
import streamlit as st

def call_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {st.secrets['OPENROUTER_API_KEY']}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

def generate_prompt(startup):
    return f"""
You're a startup analyst. Analyze this startup and give a SWOT analysis, business model, and investment advice.

Startup Name: {startup['Startup Name']}
Description: {startup['Description']}
Founders: {startup['Founders']}
Funding: {startup['Funding']}
Category: {startup['Category']}

Be detailed and structured.
"""
