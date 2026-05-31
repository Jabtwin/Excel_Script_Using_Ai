import streamlit as st
import os
from data_processor import read_data, get_data_info
from ai_engine import call_gemini_agent

st.set_page_config(page_title="Excel Script Using AI", layout="wide", page_icon="📊")

# --- CUSTOM CSS CHO GIAO DIỆN PASTEL ---
st.markdown("""
<style>
    /* Bo tròn toàn bộ giao diện khối */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Thiết kế nút bấm (Button) */
    .stButton > button {
        border-radius: 20px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        font-weight: 600;
        border: none;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    }
    
    /* Khung nhập liệu (Text Area) */
    .stTextArea textarea {
        border-radius: 15px;
        border: 1px solid #E2E8F0;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.02);
    }
    .stTextArea textarea:focus {
        border-color: #FFB7B2;
        box-shadow: 0 0 0 2px rgba(255,183,178,0.2);
    }
    
    /* Khung upload file */
    [data-testid="stFileUploadDropzone"] {
        border-radius: 15px;
        border: 2px dashed #FFB7B2 !important;
        background-color: #FAFAFA;
    }
    
    /* Các thông báo hộp màu */
    [data-testid="stAlert"] {
        border-radius: 12px;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    }
</style>
""", unsafe_allow_html=True)

st.title("📊 Excel Script Using AI")
st.markdown("Hệ thống phân tích và xử lý dữ liệu siêu tốc bằng Polars và AI.")

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
