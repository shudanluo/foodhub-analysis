import pandas as pd
from typing import List, Dict

df = pd.read_csv("C:\\Users\\luosh\\foodhub-analysis\\data\\foodhub_order.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
                 