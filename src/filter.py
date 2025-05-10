"""
File nay se su dung de tao bo loc chung giua cac bao cao
"""

import streamlit as st
import pandas as pd

def apply_common_filter(df:pd.DataFrame) -> pd.DataFrame:
    """
    🔎 Áp dụng bộ lọc chung cho các trang Streamlit
    """
    # Giá trị trong bộ lọc
    st.sidebar.header('Bộ lọc dữ liệu')
    education_filter = st.sidebar.multiselect("🎓Education", df["education"].unique(),default=df.education.unique())
    self_employed_filter = st.sidebar.multiselect('🏢 Self Employed',df.self_employed.unique(),default=df.self_employed.unique())

    # Lọc dữ liệu
    filtered_df = df[
        (df['education'].isin(education_filter)) &
        (df.self_employed.isin(self_employed_filter))
    ]
    return filtered_df