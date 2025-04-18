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
You are a senior startup analyst at a top-tier venture capital firm. A new startup has been brought to your attention. Please provide a comprehensive evaluation covering the following key areas:

---

**1. Executive Summary**  
Briefly summarize what the startup does and why it matters.

**2. Problem Statement**  
What specific problem is the startup solving?

**3. Solution Offered**  
How does the startup's product or service address the problem?

**4. Market Analysis**  
- Target audience  
- Total Addressable Market (TAM)  
- Growth trends in this sector  
- Market potential in the next 5 years

**5. Business Model**  
Explain how this startup plans to make money. Include pricing, revenue streams, and scalability.

**6. Competitive Landscape**  
- Who are the main competitors?  
- What differentiates this startup?  
- SWOT Analysis (Strengths, Weaknesses, Opportunities, Threats)

**7. Team Assessment**  
Evaluate the founding team’s background, skills, and suitability to execute this idea.

**8. Financial Health**  
- Total funding raised  
- Funding stage (Seed, Series A, etc.)  
- Burn rate (if known)  
- Potential runway

**9. Risks & Challenges**  
List key risks the startup may face (market, tech, legal, execution, etc.)

**10. Investor Recommendation**  
Give a clear opinion:  
Should this startup be considered for investment? Why or why not?

---

**Startup Details:**  
Name: {startup['Startup Name']}  
Description: {startup['Description']}  
Founders: {startup['Founders']}  
Funding: {startup['Funding']}  
Category: {startup['Category']}

Be professional, structured, and insightful in your response.
"""
