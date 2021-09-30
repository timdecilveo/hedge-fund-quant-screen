import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn import metrics


df_monthly = pd.read_csv('../data/hf_monthly.csv')
print(f"df_monthly.head():\n{df_monthly.head()}")
print(f"----------------------")
print(f"df_monthly.info():\n{df_monthly.info()}")
print(f"----------------------")
print(f"df_monthly.columns:\n{df_monthly.columns}")
print(f"----------------------")
print(f"df_monthly.describe():\n{df_monthly.describe()}")
print(f"------------------------------------------")

