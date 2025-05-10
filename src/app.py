import streamlit as st
import os
import sys
import matplotlib.pyplot as plt
sys.path.append('/home/thanhan/Project_of_An/Prediction Loan approved/prediction_loan_approval')
# from pages.customer_profile import run as run_profile
# ===== Cấu hình trang chính =====
st.set_page_config(page_title='📊 Loan Dashboard',layout='wide')

# ===== Navigation =====
st.sidebar.title("📁 Điều hướng trang")
page = st.sidebar.radio("Chọn trang:", [
    "🏠 Tổng quan",
    "👤 Hồ sơ khách hàng",
    "📈 Phân tích khoản vay",
    "🤖 Dự đoán duyệt vay"
])

# ===== Load đúng trang dựa vào lựa chọn =====
if page == "🏠 Tổng quan":
    from pages.overviews import run as run_overview
    run_overview()
elif page == "👤 Hồ sơ khách hàng":
    from pages.customer_profile import run as run_profile
    run_profile()