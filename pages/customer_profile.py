# import streamlit as st
# import seaborn as sns
# import pandas as pd
# import sys
# sys.path.append('/home/thanhan/Project_of_An/Prediction Loan approved/prediction_loan_approval')
# import os
# PATH_FILE = os.path.dirname(__file__)
# PATH_DATA = os.path.join(PATH_FILE,'..','data','loan_approval_dataset.csv')
# import matplotlib.pyplot as plt
# from src.processing_data import preprocess_data
# from src.filter import apply_common_filter 

# # ========== Load và lọc dữ liệu ==========
# df = preprocess_data(PATH_DATA)
# filtered_df = apply_common_filter(df)

# # ========== Dashboard chinh ==========

# col1, col2, col3 = st.columns(3)
# with col1:
#     fig1, ax1 = plt.subplot()
#     sns.countplot(data=filtered_df,x='education',hue='loan_status',ax=ax1)
#     ax1.set_title('🎓 Education')
#     ax1.tick_params(labelrotaion=45)
#     st.pyplot(fig=fig1,use_container_width=True)# 
# with col2:
#     fig2, ax2 = plt.subplot()
#     sns.countplot(data=filtered_df,x ='self_employed', hue='loan_status',ax=ax2)
#     ax2.set_title("🏢 Self-employed")
#     ax2.tick_params(labelrotation = 45)
#     st.pyplot(fig=fig2,use_container_width=True)
# with col3:
#     fig3, ax3 = plt.subplot()
#     sns.countplot(data=filtered_df,x = 'no_of_dependents',ax=ax3)
#     ax3.set_title('👨‍👩‍👧‍👦 Người phụ thuộc')
#     st.pyplot(fig=fig3,use_container_width=True)

# # === Layout: hàng 2 – Boxplot & Histogram thu nhập ===

# st.subheader("💰 Phân tích thu nhập")
# col4, col5 = st.columns(2)
# with col4:
#     fig4, ax4 = plt.subplot(figsize=(4,3))
#     sns.boxplot(data=filtered_df, x= 'loan_status',y='income_annum',ax= ax4)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/thanhan/Project_of_An/Prediction Loan approved/prediction_loan_approval')
import os
import seaborn as sns
#  Cấu hình matplotlib cho streamlit
plt.rcParams.update({'figure.figsize':(4,4)})
sns.set_style('whitegrid')

# Thêm đường dẫn src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
from src.processing_data import preprocess_data


def run():
    st.set_page_config(layout='wide')
    st.title('🚹 Hồ sơ khách hàng vay vốn')

    # Đọc dữ liệu
    CURRENT_PATH = os.path.dirname(__file__)
    DATA_PATH = os.path.join(CURRENT_PATH,'..','data','loan_approval_dataset.csv')

    # ============= 🎛️ Bộ lọc trong sidebar =============
    with st.sidebar:
        st.subheader("🎛️ Bộ lọc")
        gen