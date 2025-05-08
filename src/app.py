import os
import streamlit as st
import pandas as pd
import numpy as np
from processing_data import preprocess_data, check_missing_values
path_data = '../data/loan_approval_dataset.csv'

df = preprocess_data(path_data)
df = check_missing_values(df)
print(df)

import os
import streamlit as st
import pandas as pd
import numpy as np
from processing_data import preprocess_data, check_missing_values
path_data = '../data/loan_approval_dataset.csv'

df = preprocess_data(path_data)
df = check_missing_values(df)
print(df)

