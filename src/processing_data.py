import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
def load_data(path:str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df
# Xoa khoang trang trong ten cot 
def clean_column_names(df : pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
    # str_col  = df.select_dtypes(include='object').columns
    # df.str_col = df.str_col.apply(lambda x: x.strip)
    return df
# Kiem tra missing data trong bang
def check_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.isnull().sum().to_frame('missing_values')

# Xoa trung lap
def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

# Hàm gán type của dữ liệu
def make_type(df: pd.DataFrame) -> pd.DataFrame:
    cat_cols = ['education', 'self_employed', 'loan_status']
    for col in cat_cols:
        df[col] = df[col].astype('object')
    return df

# Hàm encoding Data type is category - Chuẩn hóa dữ liệu kiểu phân loại
def tranform_object(df: pd.DataFrame) -> pd.DataFrame:
    label_encoder = LabelEncoder()
    # Code ban đầu
    cat_cols = ['education', 'self_employed', 'loan_status']
    for i in cat_cols:
        df[i] = label_encoder.fit_transform(df[i])
    # Code sau khi được rút ngắn

    df[cat_cols] = df[cat_cols].apply(LabelEncoder().fit_transform)
    return df

# Hàm standardization Data - Chuẩn hóa dữ liệu
def standardize_data(df: pd.DataFrame) -> pd.DataFrame:
    scaler_data = StandardScaler()
    numerical_columns = ['no_of_dependents', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
                      'residential_assets_value', 'commercial_assets_value', 'luxury_assets_value',
                      'bank_asset_value']
    df[numerical_columns] = scaler_data.fit_transform(df[numerical_columns])
    return df

def preprocess_data(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_column_names(df)
    # df = check_missing_values(df)
    df = remove_duplicates(df)
    df = make_type(df)
    df = tranform_object(df)
    df = standardize_data(df)
    return df
