import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from processing_data import preprocess_data, check_missing_values

"""
    @funtion_meaning: describe() - Thống kê mô tả cơ bản gồm (count, sum, mean, std - độ lệch chuẩn, min, Q1 - phân vị 25%, median - trung vị, 
                        Q3 - phân vị 75%, max - giá trị lớn nhất)
    T = Transpose - Chuyển giá trị từ cột thành hàng và ngược lại
"""
def mota_solieu(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=['int64','float64']).describe().T

"""

"""
def describe_categorical(df: pd.DataFrame) -> pd.DataFrame:
    cat_cols = df.select_dtypes(include='category').columns # Tra ra list (subset)
    return pd.DataFrame({
        col: df[col].value_counts(normalize=True) * 100
        for col in cat_cols
    })

# Ham ve bieu do kiem tra tinh phan phoi cua du lieu
def plot_distribution(df: pd.DataFrame, column : str) :
    plt.figure(figsize=(8,4))
    # Bieu do historical 
    sns.histplot(df[column],kde=True,bins=30)
    plt.title(f'Phân phối của trường {column}')
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

#    
def plot_boxplot(df: pd.DataFrame, numerical : str, target_col:str):
    plt.figure(figsize=(8,4))
    sns.boxplot(data=df, x=target_col,y=numerical)
    plt.title(f'{numerical} by {target_col}')
    plt.tight_layout()
    plt.show()

