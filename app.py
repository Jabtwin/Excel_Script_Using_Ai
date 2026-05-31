import streamlit as st
import os
from data_processor import read_data, get_data_info
from ai_engine import call_gemini_agent

st.set_page_config(page_title="Antigravity Data Engine", layout="wide", page_icon="🚀")

st.title("🚀 Google Antigravity Data Engine")
st.markdown("Hệ thống phân tích dữ liệu siêu tốc bằng Polars và AI (Gemini 1.5 Pro).")

# Kiểm tra API Key
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except (FileNotFoundError, KeyError):
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "your_api_key_here":
    st.warning("⚠️ Chưa cấu hình GEMINI_API_KEY. Vui lòng thiết lập trong mục Secrets (Cloud) hoặc file .env (Local)")

# Khu vực Upload File
uploaded_file = st.file_uploader("Kéo thả file CSV hoặc Excel vào đây", type=["csv", "xlsx"])

if uploaded_file is not None:
    file_type = "csv" if uploaded_file.name.endswith(".csv") else "xlsx"
    
    with st.spinner("Đang tải dữ liệu bằng Polars..."):
        try:
            df = read_data(uploaded_file, file_type)
            st.success("Tải dữ liệu thành công!")
            
            # Hiển thị vài dòng mẫu
            st.subheader("Dữ liệu xem trước (5 dòng đầu)")
            st.dataframe(df.head(5).to_pandas(), use_container_width=True)
            
            data_info = get_data_info(df)
            
            # Form nhập yêu cầu
            st.subheader("Yêu cầu của bạn")
            user_prompt = st.text_area("Bạn muốn AI làm gì với dữ liệu này?", 
                                       placeholder="Ví dụ: Lọc các đơn hàng lỗi, tính tổng doanh thu...")
            
            if st.button("Phân tích bằng AI", type="primary"):
                if not user_prompt:
                    st.error("Vui lòng nhập yêu cầu!")
                else:
                    with st.spinner("Đầu não AI đang xử lý..."):
                        system_prompt = """Bạn là một Kỹ sư Hệ thống Dữ liệu. 
                        Nhiệm vụ của bạn là đọc yêu cầu, thiết lập các ràng buộc cho file dữ liệu, và viết code Python/Google Apps Script xử lý dữ liệu."""
                        
                        full_prompt = f"Thông tin dữ liệu:\n{data_info}\n\nYêu cầu của người dùng:\n{user_prompt}\n\nHãy phân tích và đưa ra giải pháp."
                        
                        response = call_gemini_agent(full_prompt, system_prompt)
                        
                        st.subheader("🤖 Phản hồi từ Gemini:")
                        st.markdown(response)
                        
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {str(e)}")
