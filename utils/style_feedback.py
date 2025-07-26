import streamlit as st
import groq

api_key = st.secrets["GROQ_API_KEY"]

client = groq.Groq(api_key=api_key)

def style_improvements(text):
    prompt = f"""
You are a professional resume coach. Improve the following resume by:
- Replacing weak phrases with powerful action verbs
- Enhancing tone to make it professional
- Fixing wordiness and unclear statements

Resume:
{text}
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
