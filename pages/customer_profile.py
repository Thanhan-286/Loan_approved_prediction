import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Cấu hình thư mục và import hàm tiền xử lý
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.processing_data import preprocess_data
def run():
    # ====== Load dữ liệu ======
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_PATH = os.path.join(CURRENT_DIR, '..', 'data', 'loan_approval_dataset.csv')
    df = preprocess_data(DATA_PATH)

    # ====== Bộ lọc ở sidebar ======
    st.sidebar.header("🎛️ Bộ lọc khách hàng")
    education_filter = st.sidebar.multiselect("🎓 Education", df["education"].unique(), default=df["education"].unique())
    self_employed_filter = st.sidebar.multiselect("🏢 Self Employed", df["self_employed"].unique(), default=df["self_employed"].unique())
    loan_status_filter = st.sidebar.multiselect("📄 Loan Status", df["loan_status"].unique(), default=df["loan_status"].unique())

    filtered_df = df[
        (df["education"].isin(education_filter)) &
        (df["self_employed"].isin(self_employed_filter)) &
        (df["loan_status"].isin(loan_status_filter))
    ]

    # ====== Tabs giao diện ======
    st.title("👤 Phân tích hồ sơ khách hàng")
    tab1, tab2, tab3 = st.tabs(["📊 Tổng quan", "📉 Phân tích chi tiết", "📋 Dữ liệu"])

    # ==== TAB 1: Tổng quan khách hàng ====
    with tab1:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Tổng khách hàng", filtered_df.shape[0])
        with col2:
            avg_income = filtered_df['income_annum'].mean() / 1e6
            st.metric("Thu nhập trung bình (triệu)", f"{avg_income:.2f}")
        with col3:
            st.metric("Tỷ lệ duyệt (%)", f"{(filtered_df[filtered_df['loan_status'] == 'Approved'].shape[0] / filtered_df.shape[0] * 100):.2f}%" if filtered_df.shape[0] else "0.00%")
            # Tỷ lệ duyệt bằng : 

        col4, col5,col6 = st.columns(3)
        with col4:
            st.subheader("📌 Phân phối theo học vấn")
            fig1, ax1 = plt.subplots(figsize=(3, 2))
            sns.countplot(data=filtered_df, x="education", hue="loan_status", ax=ax1)
            ax1.set_xlabel("Education")
            ax1.set_ylabel("Count")
            st.pyplot(fig1)
        with col5:
            st.subheader("📌 Tình trạng tự kinh doanh")
            fig2, ax2 = plt.subplots(figsize=(4, 3))
            sns.countplot(data=filtered_df, x="self_employed", hue="loan_status", ax=ax2)
            ax2.set_xlabel("Self Employed")
            st.pyplot(fig2)
        with col6:
            st.subheader("📌 Số người phụ thuộc")
            fig3, ax3 = plt.subplots(figsize=(4, 3))
            sns.countplot(data=filtered_df, x="no_of_dependents", hue="loan_status", ax=ax3)
            ax3.set_xlabel("No. of Dependents")
            st.pyplot(fig3)

    # ==== TAB 2: Phân tích chi tiết ====
    with tab2:
        st.subheader("📊 Mối quan hệ giữa Thu nhập và Khoản vay")
        fig4, ax4 = plt.subplots(figsize=(5, 4))
        sns.scatterplot(data=filtered_df, x="income_annum", y="loan_amount", hue="loan_status", ax=ax4)
        ax4.set_xlabel("Thu nhập hàng năm")
        ax4.set_ylabel("Khoản vay")
        st.pyplot(fig4)

        st.subheader("📊 Tài sản và Tình trạng vay")
        asset_df = filtered_df.copy()
        asset_df["total_assets"] = (
            asset_df["residential_assets_value"] +
            asset_df["commercial_assets_value"] +
            asset_df["luxury_assets_value"] +
            asset_df["bank_asset_value"]
        )

        fig5, ax5 = plt.subplots(figsize=(5, 4))
        sns.boxplot(data=asset_df, x="loan_status", y="total_assets", ax=ax5)
        ax5.set_ylabel("Tổng giá trị tài sản")
        st.pyplot(fig5)

    # ==== TAB 3: Hiển thị dữ liệu gốc ====
    with tab3:
        st.subheader("📋 Dữ liệu khách hàng đã lọc")
        st.dataframe(filtered_df.head(50), use_container_width=True)
