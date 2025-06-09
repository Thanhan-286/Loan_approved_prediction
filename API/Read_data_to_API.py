import pandas as pd 
import sys
import os
from sklearn.preprocessing import LabelEncoder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.processing_data import preprocess_data
path_df = 'data/loan_approval_dataset.csv'

df = preprocess_data(path=path_df)


print(df)
