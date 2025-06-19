import missingno as msno
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,LabelEncoder,MinMaxScaler,OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import os
import sys
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

#Tạo path để đưa vào xử lý
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from src.processing_data import preprocess_data
# CURRENT_DIR = os.path.dirname(__file__)
# DATA_PATH = os.path.join(CURRENT_DIR,'..','data','loan_approval_dataset.csv')


path_da = 'data/loan_approval_dataset.csv'
df = pd.read_csv(path_da)

# Xóa bỏ các khoảng trắng trong bộ dữ liệu và header của columns
df.columns = list(df.columns.str.strip())
df = df.map(lambda x : x.strip() if isinstance (x,str) else x)
df.drop(columns=['loan_id'],inplace=True)
print(df.columns)
# Chia tập train và test khác nhau
# Kiểu dữ liệu category data
cat_colums = ['education', 'self_employed','loan_status']
cat_transform = Pipeline(
    steps=[
        ("imputer",SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder())
    ]
)
# Kiểu dữ liệu numberical data
num_columns = df.select_dtypes(include=['int64','float64']).columns.tolist()
num_tranforms = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('num',num_tranforms,num_columns),
        ('cat',cat_transform, cat_colums),
    ]
)

# Chia dữ liệu train và test
x = df.drop(columns=['loan_status'])
y = df.loan_status
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Tạo pipeline cho từng model
full_pp = Pipeline(
    steps=[
        ('preprocessor',preprocessor),
        ('Logistic_re',LogisticRegression(random_state=42))
    ]
)

logistic_reg = full_pp.fit(x_train,y_train)
y_pre = logistic_reg.predict(x_test)

accuracy = accuracy_score(y_test,y_pre)




# Tạo thành các pipeline của từng model
print(accuracy)
