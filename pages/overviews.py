import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Cấu hình matplotlib để fit Streamlit
plt.rcParams.update({'figure.figsize': (4, 4)})

# Thêm đường dẫn src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.processing_data import preprocess_data


def run():
    # st.set_page_config(page_title='Tong quan du lieu',layout="wide")  # Giao diện rộng
    st.title('📊 Tổng quan dữ liệu vay vốn')
    # Load data
    CURRENT_DIR = os.path.dirname(__file__)
    DATA_PATH = os.path.join(CURRENT_DIR, '..', 'data', 'loan_approval_dataset.csv')
    df = preprocess_data(DATA_PATH)

    # ================= 🎛️ Bộ lọc =================
    with st.sidebar:
        st.subheader("🎛️ Bộ lọc dữ liệu")
        education_filter = st.multiselect("🎓 Education", df["education"].unique(), default=df["education"].unique())
        self_employed_filter = st.multiselect("🏢 Self Employed", df["self_employed"].unique(), default=df["self_employed"].unique())
        loan_status_filter = st.multiselect("📄 Loan Status", df["loan_status"].unique(), default=df["loan_status"].unique())

    # Lọc dữ liệu
    filtered_df = df[
        (df["education"].isin(education_filter)) &
        (df["self_employed"].isin(self_employed_filter)) &
        (df["loan_status"].isin(loan_status_filter))
    ]

    # ================= 📌 Số liệu chính =================
    col1, col2, col3, col4 = st.columns(4)
    approved = filtered_df[filtered_df['loan_status'].str.strip() == 'Approved'].shape[0]
    rate = (approved / filtered_df.shape[0] * 100) if filtered_df.shape[0] else 0
    income_avg = filtered_df.income_annum.mean()/1e6
    loan_avg = filtered_df.loan_amount.mean()/1e6
    income_sum = filtered_df.income_annum.sum()
    ratio = (filtered_df.loan_amount.sum() / income_sum * 100) if income_sum > 0 else 0 # Bang (total loan_amount / income_sum *100) 

    col1.metric('Tổng số hồ sơ', filtered_df.shape[0])
    col2.metric("Được duyệt", approved)
    col3.metric('Tỷ lệ duyệt (%)', f'{rate:.2f}%')
    col4.metric('Tỷ lệ vay/GDP (%)', f'{ratio:.2f}')

    # ================= Biểu đồ + bảng = tabs =================
    tab1, tab2 = st.tabs(["📈 Biểu đồ", "📋 Dữ liệu đã lọc"])

    with tab1:
        st.subheader("🔎 Phân phối kết quả duyệt vay")
        status_counts = filtered_df.loan_status.value_counts()
        fig1, ax1 = plt.subplots()
        status_counts.plot.pie(
            autopct='%1.1f%%',
            # startangle=90,
            ax=ax1,
            shadow=True,
            explode=[0.1 if i == status_counts.idxmax() else 0 for i in status_counts.index]
        )
        ax1.set_ylabel("")
        st.pyplot(fig1)

    with tab2:
        st.dataframe(filtered_df.head(20), use_container_width=True, height=250)
