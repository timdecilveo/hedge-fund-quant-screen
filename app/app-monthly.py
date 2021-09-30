import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn import metrics

# set the 'Date' column as the index
monthly_data = pd.read_csv("../data/hf_monthly.csv", parse_dates=["Date"], index_col="Date")
df_monthly = pd.DataFrame(monthly_data)

def plots(data_frame):
    plt.figure()
    data_frame.plot(xlabel="Date", ylabel="Monthly Performance", figsize=(20, 20), colormap="cubehelix")
    data_frame.plot(subplots=True, layout=(3, 5), figsize=(20, 20), xlabel="Date", ylabel="", colormap="cubehelix")
    plt.show(block=True)


cols = df_monthly.columns

def performance_statistics(data_frame):
    # #
    # Performance Statistics
    # #
    average_return = data_frame[cols].mean()
    median_return = data_frame[cols].median()
    max_return = data_frame[cols].max()
    min_return = data_frame[cols].min()
    st_dev = data_frame[cols].std()

    print(f"average_return:\n{average_return}")
    print(f"----")
    print(f"median_return:\n{median_return}")
    print(f"----")
    print(f"max_return:\n{max_return}")
    print(f"----")
    print(f"min_return:\n{min_return}")
    print(f"----")
    print(f"st_dev:\n{st_dev}")
    print(f"---------------------")

    # #
    # Risk Ratios
    # #
    average_return_over_st_dev = average_return / st_dev
    # gain_to_pain = df_monthly[cols].mean()
    # information_ratio = df_monthly[cols].mean()
    skew = df_monthly[cols].skew(axis=0)
    kurtosis = df_monthly[cols].kurtosis(axis=0) # https://www.usepandas.com/data-analysis/kurtosis
    excess_kurtosis = kurtosis - 3

    # if kurtosis < 0 & skew < 0:
    #     kurtosis_times_skew = -(kurtosis * skew)
    # else:
    #     kurtosis_times_skew =kurtosis * skew
    # kurtosis_times_skew = -(kurtosis * skew) if kurtosis < 0 and skew < 0 else (kurtosis * skew)
    # excess_kurtosis_times_skew = -(excess_kurtosis*skew) if excess_kurtosis < 0 and skew < 0 else (excess_kurtosis*skew)

    print(f"average_return_over_st_dev:\n{average_return_over_st_dev}")
    print(f"----")
    # print(f"gain_to_pain:\n{gain_to_pain}")
    # print(f"----")
    # print(f"information_ratio:\n{information_ratio}")
    # print(f"----")
    print(f"skew:\n{skew}")
    print(f"----")
    print(f"kurtosis:\n{kurtosis}")
    print(f"----")
    print(f"excess_kurtosis:\n{excess_kurtosis}")
    print(f"----")
    # print(f"kurtosis_times_skew:\n{kurtosis_times_skew}")
    print(f"----")
    # print(f"excess_kurtosis_times_skew:\n{excess_kurtosis_times_skew}")
    print(f"----")

    print(f"---------------------")


# plots(df_monthly)
performance_statistics(df_monthly)