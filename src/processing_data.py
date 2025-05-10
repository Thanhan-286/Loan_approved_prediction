import pandas as pd
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

# Hàm chuẩn hóa 
def convert_types(df: pd.DataFrame) -> pd.DataFrame:
    cat_cols = ['education', 'self_employed', 'loan_status']
    for col in cat_cols:
        df[col] = df[col].astype('category')
    return df

def preprocess_data(path: str) -> pd.DataFrame:
    df = load_data(path)
    df = clean_column_names(df)
    # df = check_missing_values(df)
    df = remove_duplicates(df)
    df = convert_types(df)
    return df


