import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
import pyfolio as pf


# set the 'Date' column as the index
monthly_data = pd.read_csv("../data/hf_monthly.csv", parse_dates=["Date"], index_col="Date")
df_monthly = pd.DataFrame(monthly_data)
# df_ind= pd.DataFrame(pd.read_csv("../data/hf_monthly.csv", parse_dates=["Date"]))

def plots(data_frame):
    plt.figure()
    data_frame.plot(xlabel="Date", ylabel="Monthly Performance", figsize=(20, 20), colormap="cubehelix")
    data_frame.plot(subplots=True, layout=(3, 5), figsize=(20, 20), xlabel="Date", ylabel="", colormap="cubehelix")
    plt.show(block=True)


cols = df_monthly.columns

def performance_statistics(data_frame):
    # ### Statistics
    average_return = data_frame[cols].mean()
    median_return = data_frame[cols].median()
    max_return = data_frame[cols].max()
    min_return = data_frame[cols].min()
    st_dev = data_frame[cols].std()

    # ### Risk Ratios
    average_return_over_st_dev = average_return / st_dev
    gain_to_pain = df_monthly[cols].sum() / abs(df_monthly[df_monthly[cols] < 0].sum())
    # information_ratio = df_monthly[cols].mean()
    skew = df_monthly[cols].skew(axis=0)
    kurtosis = df_monthly[cols].kurtosis(axis=0)
    excess_kurtosis = kurtosis - 3
    kurtosis_times_skew = kurtosis * skew
    excess_kurtosis_times_skew = excess_kurtosis * skew
    # downside_deviation = 
    # tail_ratio = 
    # treynor_ratio = 

    # simple_tear_sheet = pf.create_simple_tear_sheet(df_monthly[cols])
    # full_tear_sheet = pf.create_full_tear_sheet(df_monthly[cols])
    # print(f"simple_tear_sheet:\n{simple_tear_sheet}")
    # print(f"full_tear_sheet:\n{full_tear_sheet}")
    ts = pf.create_returns_tear_sheet(df_monthly['Tim_Trend_2'])
    print(f"ts:\n{ts}")

    # # print(f"information_ratio:\n{information_ratio}")
    # # print(f"----")

    # ### Convert to DataFrames
    df_average_return = pd.DataFrame([average_return], index=['Average Return'])
    df_median_return = pd.DataFrame([median_return], index=['Median Return'])
    df_max_return = pd.DataFrame([max_return], index=['Maximum Return'])
    df_min_return = pd.DataFrame([min_return], index=['Minimum Return'])
    df_st_dev = pd.DataFrame([st_dev], index=['Standard Deviation'])
    df_average_return_over_st_dev = pd.DataFrame([average_return_over_st_dev], index=['Avg. Return / Std. Dev.'])
    df_gain_to_pain = pd.DataFrame([gain_to_pain], index=['Gain to Pain Ratio'])
    # df_information_ratio
    df_skew = pd.DataFrame([skew], index=['Skew'])
    df_kurtosis = pd.DataFrame([kurtosis], index=['Kurtosis'])
    df_excess_kurtosis = pd.DataFrame([excess_kurtosis], index=['Excess Kurtosis'])
    df_kurtosis_times_skew = pd.DataFrame([kurtosis_times_skew], index=['Kurtosis * Skew'])
    df_excess_kurtosis_times_skew = pd.DataFrame([excess_kurtosis_times_skew], index=['Excess Kurtosis * Skew'])


    extend_perf_stats = []
    extend_perf_stats.extend(
        [
            df_average_return,
            df_median_return,
            df_max_return,
            df_min_return,
            df_st_dev,
            df_average_return_over_st_dev,
            df_gain_to_pain,
            # df_information_ratio,
            df_skew,
            df_kurtosis,
            df_excess_kurtosis,
            df_kurtosis_times_skew,
            df_excess_kurtosis_times_skew,
        ]
    )
    performance_stats = pd.concat(extend_perf_stats)

    print(f"performance_stats:\n{performance_stats}")
    print(f"--------- END ---------")



# plots(df_monthly)
performance_statistics(df_monthly)