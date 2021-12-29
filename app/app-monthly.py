import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
from performance_statistics import PerformanceStatistics as perf
from stats import Stats

# import performance_statistics as perf

# import zipline
# import pyfolio as pf

# set the 'Date' column as the index
monthly_data = pd.read_csv("../data/hf_monthly.csv", parse_dates=["Date"], index_col="Date")
df_monthly = pd.DataFrame(monthly_data)
start_date = '1993-02-28'
ending_date = '2019-02-28'
end_date = '2019-02-28'

# def plots(data_frame):
#     plt.figure()
#     data_frame.plot(xlabel="Date", ylabel="Monthly Performance", figsize=(20, 20), colormap="cubehelix")
#     data_frame.plot(subplots=True, layout=(3, 5), figsize=(20, 20), xlabel="Date", ylabel="", colormap="cubehelix")
#     plt.show(block=True)

# plots(df_monthly)
# perf.cagr(df_monthly)
# perf.performance_statistics(df_monthly, start_date, end_date)
print(f"df_monthly:\n{df_monthly}")
print("--------")

average_return = Stats(df_monthly, start_date, ending_date).average_return()
print(f"average_return:\n{average_return}")
print("--------")

cagr = Stats(df_monthly, start_date, ending_date).compounded_annual_growth_rate()
print(f"cagr:\n{cagr}")
print("--------")