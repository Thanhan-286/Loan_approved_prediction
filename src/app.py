import os
import streamlit as st
import pandas as pd
import numpy as np

path_data = 'data/loan_approval_dataset.csv'

df = pd.read_csv(path_data)
df.rename(columns= lambda x: x.strip(), inplace=True)
print(df)

