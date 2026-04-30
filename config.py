import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY  = NONE
if "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" in st.secrets:
  GROQ_API_KEY = st.secrets["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"]
else:
  GROQ_API_KEY = os.getenv("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")
