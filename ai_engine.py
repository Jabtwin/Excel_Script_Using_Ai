import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Tải các biến môi trường từ file .env (dùng cho Local)
load_dotenv()

# Lấy API key: Ưu tiên Streamlit secrets (Cloud), sau đó lấy từ biến môi trường (Local)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    raise ValueError("BẠN QUÊN NHẬP API KEY RỒI! Vui lòng vào Cài đặt (Settings) -> Secrets trên Streamlit Cloud để dán mã API Key vào.")

genai.configure(api_key=api_key)

def call_gemini_agent(prompt: str, system_instruction: str = None) -> str:
    """
    Hàm gọi Gemini API
    """
    try:
        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            system_instruction=system_instruction
        )
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Lỗi khi gọi API Gemini: {str(e)}"
