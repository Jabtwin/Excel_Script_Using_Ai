# 🚀 Google Antigravity Data Engine

![Antigravity Banner](assets/banner.png)

**Google Antigravity Data Engine** là một hệ thống phân tích và xử lý dữ liệu siêu tốc, được thiết kế chuyên biệt để tự động hóa các tác vụ làm sạch dữ liệu (Data Cleaning) và tự động sinh mã code (Google Apps Script / Python) bằng trí tuệ nhân tạo.

## ✨ Tính năng nổi bật
- **Siêu tốc với Polars:** Xử lý hàng triệu dòng dữ liệu dạng bảng (CSV/Excel) chỉ trong chớp mắt, đánh bại hoàn toàn các phần mềm bảng tính truyền thống.
- **Đầu não AI thông minh:** Tích hợp mô hình Google Gemini (2.5) để tự động phân tích cấu trúc dữ liệu, nhận diện điểm bất thường và đưa ra giải pháp code chuẩn xác.
- **Giao diện trực quan:** Được xây dựng bằng Streamlit, hỗ trợ thao tác kéo thả file đơn giản và tương tác với AI bằng ngôn ngữ tự nhiên.

## 🚀 Hướng dẫn cài đặt (Chạy Local)
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```
2. Đổi tên file `.env.example` thành `.env` và điền `GEMINI_API_KEY` của bạn (Lấy từ Google AI Studio).
3. Khởi động hệ thống:
   ```bash
   python -m streamlit run app.py
   ```

## 🌐 Trải nghiệm trực tuyến
Hệ thống có thể được triển khai dễ dàng lên **Streamlit Community Cloud**. Chỉ cần kết nối Repository này, thiết lập biến môi trường `GEMINI_API_KEY` trong mục *Secrets*, và hệ thống sẽ tự động vận hành 24/7.
