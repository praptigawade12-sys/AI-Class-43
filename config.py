import os
import streamlit as st
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#if "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" in st.secrets:
#  GROQ_API_KEY = st.secrets["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"]
#else:
#  GROQ_API_KEY = os.getenv("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")
#print("CONFIG DEBUG:", GROQ_API_KEY)

if not GROQ_API_KEY:
  raise ValueError("GROQ_API_KEY is missing")
