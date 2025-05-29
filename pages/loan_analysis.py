# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from src.processing_data import preprocess_data

# # ==== Load data ====
# DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'loan_approval_dataset.csv')
# df = preprocess_data(DATA_PATH)

# # ==== Sidebar filter ====
# st.sidebar.header("🎛️ Bộ lọc dữ liệu")

# education_filter = st.sidebar.multiselect("🎓 Education", df["education"].unique(), default=df["education"].unique())
# self_employed_filter = st.sidebar.multiselect("🏢 Self Employed", df["self_employed"].unique(), default=df["self_employed"].unique())
# property_filter = st.sidebar.multiselect("🏘️ Property Area", df["property_area"].unique(), default=df["property_area"].unique())
# loan_status_filter = st.sidebar.multiselect("📄 Loan Status", df["loan_status"].unique(), default=df["loan_status"].unique())

# filtered_df = df[
#     (df["education"].isin(education_filter)) &
#     (df["self_employed"].isin(self_employed_filter)) &
#     (df["property_area"].isin(property_filter)) &
#     (df["loan_status"].isin(loan_status_filter))
# ]

# st.title("📊 Phân tích khoản vay & Yếu tố ảnh hưởng")

# # ==== Section 1: Tổng quan khoản vay ====
# st.subheader("1️⃣ Tổng quan khoản vay")
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("💰 Số tiền vay trung bình (triệu)", f"{filtered_df['loan_amount'].mean()/1e6:.2f}")
# with col2:
#     st.metric("📈 Thu nhập trung bình (triệu)", f"{filtered_df['income_annum'].mean()/1e6:.2f}")
# with col3:
#     st.metric("⏳ Thời hạn vay phổ biến", f"{filtered_df['loan_term'].mode()[0]} tháng")

# col4, col5 = st.columns(2)
# with col4:
#     fig, ax = plt.subplots()
#     sns.histplot(filtered_df['loan_amount'], kde=True, bins=20, ax=ax, color='teal')
#     ax.set_title("Phân phối số tiền vay")
#     st.pyplot(fig)

# with col5:
#     fig, ax = plt.subplots()
#     sns.histplot(filtered_df['income_annum'], kde=True, bins=20, ax=ax, color='salmon')
#     ax.set_title("Phân phối thu nhập")
#     st.pyplot(fig)

# # ==== Section 2: So sánh theo trạng thái duyệt vay ====
# st.subheader("2️⃣ So sánh giữa nhóm Được duyệt và Từ chối")
# col6, col7 = st.columns(2)

# with col6:
#     fig, ax = plt.subplots()
#     sns.boxplot(x="loan_status", y="loan_amount", data=filtered_df, ax=ax, palette="Set2")
#     ax.set_title("Số tiền vay theo trạng thái duyệt")
#     st.pyplot(fig)

# with col7:
#     fig, ax = plt.subplots()
#     sns.boxplot(x="loan_status", y="income_annum", data=filtered_df, ax=ax, palette="Set1")
#     ax.set_title("Thu nhập theo trạng thái duyệt")
#     st.pyplot(fig)

# # ==== Section 3: Các yếu tố ảnh hưởng đến duyệt vay ====
# st.subheader("3️⃣ Phân tích yếu tố ảnh hưởng")

# col8, col9 = st.columns(2)

# with col8:
#     st.markdown("**Tỷ lệ duyệt vay theo Education**")
#     edu_approval = pd.crosstab(filtered_df['education'], filtered_df['loan_status'], normalize='index') * 100
#     st.bar_chart(edu_approval['Approved'])

# with col9:
#     st.markdown("**Tỷ lệ duyệt vay theo Self Employed**")
#     emp_approval = pd.crosstab(filtered_df['self_employed'], filtered_df['loan_status'], normalize='index') * 100
#     st.bar_chart(emp_approval['Approved'])

# col10, col11 = st.columns(2)

# with col10:
#     st.markdown("**Tỷ lệ duyệt vay theo Property Area**")
#     prop_approval = pd.crosstab(filtered_df['property_area'], filtered_df['loan_status'], normalize='index') * 100
#     st.bar_chart(prop_approval['Approved'])

# with col11:
#     st.markdown("**Heatmap tương quan các biến số**")
#     num_df = filtered_df[['income_annum', 'loan_amount', 'loan_term']].copy()
#     fig, ax = plt.subplots()
#     sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", ax=ax)
#     st.pyplot(fig)

# # ==== Hiển thị bảng dữ liệu đã lọc ====
# with st.expander("📋 Xem bảng dữ liệu đã lọc"):
#     st.dataframe(filtered_df)
