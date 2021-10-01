import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
# import zipline
# import pyfolio as pf


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
    # ### --- Statistics --- ###
    # cagr = 
    average_return = data_frame[cols].mean()
    median_return = data_frame[cols].median()
    max_return = data_frame[cols].max()
    min_return = data_frame[cols].min()
    st_dev = data_frame[cols].std()

    max_drawdown = data_frame[cols].cumsum()
    max2here = max_drawdown.cummax()
    dd2here = max_drawdown - max2here
    mxdd = dd2here.min()

    # plt.figure()
    # max_drawdown.plot()
    # plt.show(block=True)




    # ### --- Risk Ratios --- ###
    average_return_over_st_dev = average_return / st_dev
    gain_to_pain = data_frame[cols].sum() / abs(data_frame[data_frame[cols] < 0].sum())
    # information_ratio = data_frame[cols].mean()
    skew = data_frame[cols].skew(axis=0)
    kurtosis = data_frame[cols].kurtosis(axis=0)
    excess_kurtosis = kurtosis - 3
    kurtosis_times_skew = kurtosis * skew
    excess_kurtosis_times_skew = excess_kurtosis * skew
    # downside_deviation = 
    # tail_ratio = 
    # treynor_ratio = 
    
    z = norm.ppf(0.05)
    var_gauss = -(average_return + z * data_frame[cols].std(ddof=0)) # Parametric/Gaussian VaR (NEW)
    # Cornish-Fisher VaR (NEW)
    z = (z + (z**2 - 1) * skew / 6 + (z**3 - 3 * z) * (kurtosis - 3) / 24 - (2 * z**3 - 5 * z) * (skew**2) / 36)
    var_modified_cornish_fisher = -(average_return + z * data_frame[cols].std(ddof=0)) # Cornish-Fisher VaR (NEW)


    # ### --- Performance Statistics (Winners vs. Losers) --- ###
    pos_average_return = data_frame[data_frame[cols] > 0].mean()
    pos_median_return = data_frame[data_frame[cols] > 0].median()
    pos_max_return = data_frame[data_frame[cols] > 0].max()
    pos_min_return = data_frame[data_frame[cols] > 0].min()
    pos_st_dev = data_frame[data_frame[cols] > 0].std()

    neg_average_return = data_frame[data_frame[cols] < 0].mean()
    neg_median_return = data_frame[data_frame[cols] < 0].median()
    neg_max_return = data_frame[data_frame[cols] < 0].max()
    neg_min_return = data_frame[data_frame[cols] < 0].min()
    neg_st_dev = data_frame[data_frame[cols] < 0].std()

    num_winning_periods = data_frame[data_frame[cols] > 0].count()
    num_losing_periods = data_frame[data_frame[cols] < 0].count()
    zero_count = data_frame[data_frame[cols] == 0].count()
    total_count = num_winning_periods + num_losing_periods + zero_count

    num_winning_periods_percentage = num_winning_periods / total_count
    num_losing_periods_percentage = num_losing_periods / total_count
    win_loss_ratio = num_winning_periods / num_losing_periods
    expectancy = (pos_median_return * num_winning_periods) + (neg_median_return * num_losing_periods)
    expectancy_ratio = (pos_median_return * num_winning_periods) / abs((neg_median_return * num_losing_periods))
    markowitz_return_function = average_return / st_dev
    # sharpe_ratio_skew

    # ### --- Convert to DataFrames --- ##
    df_average_return = pd.DataFrame([average_return], index=['Average Return'])
    df_median_return = pd.DataFrame([median_return], index=['Median Return'])
    df_max_return = pd.DataFrame([max_return], index=['Maximum Return'])
    df_min_return = pd.DataFrame([min_return], index=['Minimum Return'])
    df_st_dev = pd.DataFrame([st_dev], index=['Standard Deviation'])

    # df_max_drawdown = pd.DataFrame([max_drawdown], index=['Max Drawdown'])



    df_average_return_over_st_dev = pd.DataFrame([average_return_over_st_dev], index=['Avg. Return / Std. Dev.'])
    df_gain_to_pain = pd.DataFrame([gain_to_pain], index=['Gain to Pain Ratio'])
    # df_information_ratio
    df_skew = pd.DataFrame([skew], index=['Skew'])
    df_kurtosis = pd.DataFrame([kurtosis], index=['Kurtosis'])
    df_excess_kurtosis = pd.DataFrame([excess_kurtosis], index=['Excess Kurtosis'])
    df_kurtosis_times_skew = pd.DataFrame([kurtosis_times_skew], index=['Kurtosis * Skew'])
    df_excess_kurtosis_times_skew = pd.DataFrame([excess_kurtosis_times_skew], index=['Excess Kurtosis * Skew'])
    df_var_gauss = pd.DataFrame([var_gauss], index=['Parametric/Gaussian VaR'])
    df_var_modified_cornish_fisher = pd.DataFrame([var_modified_cornish_fisher], index=['Modified Cornish Fisher VaR'])

    df_pos_average_return = pd.DataFrame([pos_average_return], index=['Average Return (winning periods)'])
    df_pos_median_return = pd.DataFrame([pos_median_return], index=['Median Return (winning periods)'])
    df_pos_max_return = pd.DataFrame([pos_max_return], index=['Max Return (winning periods)'])
    df_pos_min_return = pd.DataFrame([pos_min_return], index=['Min Return (winning periods)'])
    df_pos_st_dev = pd.DataFrame([pos_st_dev], index=['Standard Deviation (winning periods)'])

    df_neg_average_return = pd.DataFrame([neg_average_return], index=['Average Return (losing periods)'])
    df_neg_median_return = pd.DataFrame([neg_median_return], index=['Median Return (losing periods)'])
    df_neg_max_return = pd.DataFrame([neg_max_return], index=['Max Return (losing periods)'])
    df_neg_min_return = pd.DataFrame([neg_min_return], index=['Min Return (losing periods)'])
    df_neg_st_dev = pd.DataFrame([neg_st_dev], index=['Standard Deviation (losing periods)'])

    df_num_winning_periods = pd.DataFrame([num_winning_periods], index=['# of Winning Periods'])
    df_num_losing_periods = pd.DataFrame([num_losing_periods], index=['# of Winning Periods'])
    df_zero_count = pd.DataFrame([zero_count], index=['# of Flat Periods'])
    df_total_count = pd.DataFrame([total_count], index=['Total # of Periods'])

    df_num_winning_periods_percentage = pd.DataFrame([num_winning_periods_percentage], index=['"%"of Winning Periods'])
    df_num_losing_periods_percentage = pd.DataFrame([num_losing_periods_percentage], index=['"%"of Losing Periods'])
    df_win_loss_ratio = pd.DataFrame([win_loss_ratio], index=['Win / Loss Ratio'])
    df_expectancy = pd.DataFrame([expectancy], index=['Expectancy'])
    df_expectancy_ratio = pd.DataFrame([expectancy_ratio], index=['Expectancy %'])
    df_markowitz_return_function = pd.DataFrame([markowitz_return_function], index=['Markowitz Return Function'])

    extend_perf_stats = []
    extend_perf_stats.extend(
        [
            df_average_return,
            df_median_return,
            df_max_return,
            df_min_return,
            df_st_dev,
            # df_max_drawdown,
            df_average_return_over_st_dev,
            df_gain_to_pain,
            # df_information_ratio,
            df_skew, df_kurtosis,
            df_excess_kurtosis,
            df_kurtosis_times_skew,
            df_excess_kurtosis_times_skew,
            df_var_gauss,
            df_var_modified_cornish_fisher,
            df_pos_average_return,
            df_pos_median_return, 
            df_pos_max_return,
            df_pos_min_return,
            df_pos_st_dev, 
            df_neg_average_return,
            df_neg_median_return,
            df_neg_max_return,
            df_neg_min_return, df_neg_st_dev,
            df_num_winning_periods,
            df_num_losing_periods,
            df_zero_count,
            df_total_count,
            df_num_winning_periods_percentage,
            df_num_losing_periods_percentage,
            df_win_loss_ratio,
            df_expectancy,
            df_expectancy_ratio,
            df_markowitz_return_function,
        ]
    )
    performance_stats = pd.concat(extend_perf_stats)
    print(f"performance_stats:\n{performance_stats}")
    # interesting plots - https://medium.com/swlh/downside-risk-measures-9a013d03800d
    print(f"--------- END ---------")



# plots(df_monthly)
performance_statistics(df_monthly)