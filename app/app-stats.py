import os
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
from directories import Directory
from stats import Stats

beginning_date = '1993-02-28'
ending_date = '2019-02-28'
end_date = '2019-02-28'

directory = os.listdir(f"../data-files")
file_list = Directory(directory).files()

average_return = Stats(beginning_date, ending_date).average_return()
# median_return = Stats(beginning_date, ending_date).median_return()
# max_return = Stats(beginning_date, ending_date).max_return()
# min_return = Stats(beginning_date, ending_date).min_return()
# st_dev = Stats(beginning_date, ending_date).st_dev()
# print(f"average_return:\n{average_return}")
# print("---------")
# print(f"median_return:\n{median_return}")
# print("---------")
# print(f"max_return:\n{max_return}")
# print("---------")
# print(f"min_return:\n{min_return}")
# print("---------")
# print(f"st_dev:\n{st_dev}")
# print("---------")



# print(f"average_return:\n{average_return}")
# print("--------")

# cagr = Stats(df_monthly, beginning_date, ending_date).compounded_annual_growth_rate()
# print(f"cagr:\n{cagr}")
# print("--------")