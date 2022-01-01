import os
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from directories import Directory
from functools import reduce

class Stats:
    def __init__(self):
        self.directory = os.listdir(f"../data-files")
        self.file_list = Directory(self.directory).files()
        self.rf = 0.02 / 12

    def statistics(self):
        db = []

        for i in self.file_list:
            file_name = i.columns[0]
            dates = i[file_name].index
            start_date = dates[0]
            end_date = dates[-1] #need to fix this so it's the rolling date

            monthly_return = i[file_name]
            average_return = monthly_return.expanding().mean()
            median_reutrn = monthly_return.expanding().median()
            maximum_return = monthly_return.expanding().max()
            minimum_return = monthly_return.expanding().min()
            standard_deviation = monthly_return.expanding().std()

            # downside deviation of monthly percentage returns
            downside_deviation = i[monthly_return < 0].expanding().std() # deviations of only the negative returns
            
            # pd.merge_ordered(i, downside_deviation, on='Date', suffixes=('_win', '_downside_dev'), fill_method='ffill')
            # print(type(downside_deviation))




            skew = monthly_return.expanding().skew(axis=0)
            kurtosis = monthly_return.expanding().kurt(axis=0)
            excess_kurtosis = kurtosis - 3
            kurtosis_times_skew_ = kurtosis * skew
            excess_kurtosis_times_skew_ = excess_kurtosis * skew

            time_delta_days = (end_date - start_date).days
            years = time_delta_days / 365
            compounded_return = (monthly_return + 1).cumprod()
            cagr = ((compounded_return) ** (1 / years)) - 1

            peak = compounded_return.expanding(min_periods=1).max()
            drawdown = (compounded_return / peak) - 1
            max_drawdown = drawdown.min()
            markowitz_return_function = average_return / standard_deviation

            # ####################################
            i['MonthlyReturn'] = monthly_return
            i['AvgReturn'] = average_return
            i['MedianReturn'] = median_reutrn
            i['MaxReturn'] = maximum_return
            i['MinReturn'] = minimum_return
            i['StDev'] = standard_deviation
            i['DownsideDev'] = downside_deviation
            i['DownsideDev'].fillna(method="ffill", inplace=True)
            i['Skew'] = skew
            i['Kurtosis'] = kurtosis
            i['ExcessKurtosis'] = excess_kurtosis
            i['Kurt*Skew'] = kurtosis_times_skew_
            i['ExcessKurtosis*Skew'] = excess_kurtosis_times_skew_
            i['CompoundedReturn'] = compounded_return
            i['CAGR'] = cagr
            i['MaxDD'] = max_drawdown
            i['MarkowitzReturnFunction'] = markowitz_return_function
            i['AvgReturn/StDev'] = i['AvgReturn'] / i['StDev']
            i['MedianReturn/StDev'] = i['MedianReturn'] / i['StDev']
            i['CAGR/StDev'] = i['CAGR'] / i['StDev']
            i['AvgReturn/MaxDD'] = i['AvgReturn'] / abs(i['MaxDD'])
            i['MedianReturn/MaxDD'] = i['MedianReturn'] / abs(i['MaxDD'])
            i['CAGR/MaxDD'] = i['CAGR'] / abs(i['MaxDD'])
            # ####################################

            '''
            Sharpe Ratio:
            sharpe ratio = (rp - rf) / standard deviation
                rp = average_return
                rf = self.rf
                standard deviation = standard_deviation
            '''
            sharpe = (i['AvgReturn'] - self.rf) / i['StDev']
            i['SharpeRatio'] = sharpe
            i['SharpeRatioAnnualized'] = sharpe * np.sqrt(12)

            '''
            Sortino Ratio:
            sortino ratio = (rp - rf) / downside deviation
                rp = average_return
                rf = self.rf
                downside deviation = downside_deviation
            '''
            sortino = (i['AvgReturn'] - self.rf) / i['DownsideDev']
            i['SortinoRatio'] = sortino
            i['SortinoRatioAnnualized'] = sortino * np.sqrt(12)

            '''
            Calmar Ratio:
            calmar ratio = (rp - rf) / maximum drawdown
                rp = average_return
                rf = self.rf
                maximum drawdown = max_drawdown
            '''
            calmar = (i['AvgReturn'] - self.rf) / abs(i['MaxDD'])
            i['CalmarRatio'] = calmar
            i['CalmarRatioAnnualized'] = calmar * np.sqrt(12)

            '''
            Parametric/Gaussian VaR
            gaussian var = 
            '''
            z = norm.ppf(0.05)
            gaussian_var = -(i['AvgReturn'] + z * i['MonthlyReturn'].std(ddof=0))
            i['Gaussian VaR'] = gaussian_var

            '''
            Modified Cornish Fisher VaR
            cornish fisher var = 
            '''
            z = (z + (z**2 - 1) * i['Skew'] / 6 + (z**3 - 3 * z) * (i['Kurtosis'] - 3) / 24 - (2 * z**3 - 5 * z) * (i['Skew']**2) / 36)
            modified_cornish_fisher_var = -(i['AvgReturn'] + z * i['MonthlyReturn'].std(ddof=0))
            i['CornishFisher VaR'] = modified_cornish_fisher_var

            '''
            Winning Months vs. Losing Months
            '''
            # Winning Months
            winning_return = i['MonthlyReturn'][i['MonthlyReturn'] > 0]
            i['Winning-Return'] = winning_return

            i['Winning-AvgReturn'] = i['Winning-Return'].expanding().mean()
            i['Winning-MedianReturn'] = i['Winning-Return'].expanding().median()
            i['Winning-MaxReturn'] = i['Winning-Return'].expanding().max()
            i['Winning-MinReturn'] = i['Winning-Return'].expanding().min()
            i['Winning-StDev'] = i['Winning-Return'].expanding().std()
            i['Winning-NumOfPeriods'] = i['Winning-Return'].expanding().count()

            # Losing Months
            losing_return = i['MonthlyReturn'][i['MonthlyReturn'] < 0]
            i['Losing-Return'] = losing_return

            i['Losing-AvgReturn'] = i['Losing-Return'].expanding().mean()
            i['Losing-MedianReturn'] = i['Losing-Return'].expanding().median()
            i['Losing-MaxReturn'] = i['Losing-Return'].expanding().max()
            i['Losing-MinReturn'] = i['Losing-Return'].expanding().min()
            i['Losing-StDev'] = i['Losing-Return'].expanding().std()
            i['Losing-NumOfPeriods'] = i['Losing-Return'].expanding().count()

            i['Total-NumOfPeriods'] = i['MonthlyReturn'].expanding().count()

            # i['WinningPerc (%)'] = winning_periods_percentage
            # i['LosingPerc (%)'] = losing_periods_percentage
            # i['Win-Loss Ratio'] = win_loss_ratio
            # i['Expectancy (+)'] = expectancy
            # i['ExepectancyRatio (%)'] = expectancy_ratio

            # winning_median_return = i[winning].expanding().median()
            # winning_median_return.name = 'winning_median_return'

            # winning_max_return = i[winning].expanding().max()
            # winning_max_return.name = 'winning_max_return'

            # winning_min_return = i[winning].expanding().min()
            # winning_min_return.name = 'winning_min_return'

            # winning_st_dev = i[winning].expanding().std()
            # winning_st_dev.name = 'winning_st_dev'

            # winning_num_periods = i[winning].expanding().count()
            # winning_num_periods.name = 'winning_num_periods'

            # # Losing Months
            # losing_average_return = i[losing].expanding().mean()
            # losing_average_return.name = 'losing_average_return'

            # losing_median_return = i[losing].expanding().median()
            # losing_median_return.name = 'losing_median_return'

            # losing_max_return = i[losing].expanding().max()
            # losing_max_return.name = 'losing_max_return'

            # losing_min_return = i[losing].expanding().min()
            # losing_min_return.name = 'losing_min_return'

            # losing_st_dev = i[losing].expanding().std()
            # losing_st_dev.name = 'losing_st_dev'

            # losing_num_periods = i[losing].expanding().count()
            # losing_num_periods.name = 'losing_num_periods'

            # # Total Months
            # total_num_periods = monthly_return.expanding().count()
            # total_num_periods.name = 'total_num_periods'

            # vars_ = [
                # downside_deviation,
                # sortino,
                # winning_average_return,
                # winning_median_return,
                # winning_max_return,
                # winning_min_return,
                # winning_st_dev,
                # winning_num_periods,
                # losing_average_return,
                # losing_median_return,
                # losing_max_return,
                # losing_min_return,
                # losing_st_dev,
                # losing_num_periods,
                # total_num_periods,
            # ]
            # column_names = ['Date',
            #     # 'downside_deviation',
            #     # 'sortino',
            #     'winning_average_return',
            #     'winning_median_return',
            #     'winning_max_return',
            #     'winning_min_return',
            #     'winning_st_dev',
            #     'winning_num_periods',
            #     'losing_average_return',
            #     'losing_median_return',
            #     'losing_max_return',
            #     'losing_min_return',
            #     'losing_st_dev',
            #     'losing_num_periods',
            #     'total_num_periods',
            # ]
            # df_merged = reduce(lambda  left,right: pd.merge_ordered(left, right, on=['Date'], how='outer', fill_method='ffill'), vars_)
            # for (i, column_name) in zip(df_merged, column_names):
            #     # print(f'i: {i}\tcolumn_name: {column_name}')
            #     # print('--')
            #     df_merged.rename(columns={i: column_name}, inplace=True)
            #     # df_merged.rename(columns={i: column_name})
            
            # index_date = df_merged.columns[0]
            # df_merged.set_index(index_date, inplace=True)
            # print(df_merged)

            # Winning vs. Losing Months Calculations
            # Winning Months Calcs
            # df_winning_periods_percentage = pd.merge_ordered(winning_num_periods, total_num_periods, on='Date', suffixes=('_win', '_total'), fill_method='ffill')
            # index = df_winning_periods_percentage.columns[0]
            # win_col = df_winning_periods_percentage.columns[1]
            # total_col = df_winning_periods_percentage.columns[2]
            # df_winning_periods_percentage.set_index(index, inplace=True)
            # df_winning_periods_percentage['WinningPerc (%)'] = df_winning_periods_percentage[win_col] / df_winning_periods_percentage[total_col]
            # winning_periods_percentage = df_winning_periods_percentage['WinningPerc (%)']

            # # Losing Months Calcs
            # df_losing_periods_percentage = pd.merge_ordered(losing_num_periods, total_num_periods, on='Date', suffixes=('_lose', '_total'), fill_method='ffill')
            # index = df_losing_periods_percentage.columns[0]
            # los_col = df_losing_periods_percentage.columns[1]
            # total_col = df_losing_periods_percentage.columns[2]
            # df_losing_periods_percentage.set_index(index, inplace=True)
            # df_losing_periods_percentage['LosingPerc (%)'] = df_losing_periods_percentage[los_col] / df_losing_periods_percentage[total_col]
            # losing_periods_percentage = df_losing_periods_percentage['LosingPerc (%)']

            # df_win_loss_ratio = pd.merge_ordered(winning_num_periods, losing_num_periods, on='Date', suffixes=('_win', '_loss'), fill_method='ffill')
            # index = df_win_loss_ratio.columns[0]
            # win_col = df_win_loss_ratio.columns[1]
            # lose_col = df_win_loss_ratio.columns[2]
            # df_win_loss_ratio.set_index(index, inplace=True)
            # df_win_loss_ratio['Win-Loss Ratio'] = df_win_loss_ratio[win_col] / df_win_loss_ratio[lose_col]
            # win_loss_ratio = df_win_loss_ratio['Win-Loss Ratio']

            # expectancy = (winning_median_return * winning_num_periods) + (losing_median_return * losing_num_periods)
            # expectancy_ratio = (winning_median_return * winning_num_periods) / abs((losing_median_return * losing_num_periods))

            # ####################################
            # gain to pain ratio
            # information_ratio


            # i['Winning-AvgReturn'] = winning_average_return
            # i['Winning-MedianReturn'] = winning_median_return
            # i['Winning-MaxReturn'] = winning_max_return
            # i['Winning-MinReturn'] = winning_min_return
            # i['Winning-StDev'] = winning_st_dev
            # i['Winning-NumOfPeriods'] = winning_num_periods
            # i['Losing-AvgReturn'] = losing_average_return
            # i['Losing-MedianReturn'] = losing_median_return
            # i['Losing-MaxReturn'] = losing_max_return
            # i['Losing-MinReturn'] = losing_min_return
            # i['Losing-StDev'] = losing_st_dev
            # i['Losing-NumOfPeriods'] = losing_num_periods
            # i['Total-NumOfPeriods'] = total_num_periods
            # i['WinningPerc (%)'] = winning_periods_percentage
            # i['LosingPerc (%)'] = losing_periods_percentage
            # i['Win-Loss Ratio'] = win_loss_ratio
            # i['Expectancy (+)'] = expectancy
            # i['ExepectancyRatio (%)'] = expectancy_ratio
            
            db.append(i)
        return db

    def downside_deviation(self):
        db = []

        for i in self.file_list:
            file_name = i.columns[0]
            downside_deviation_ = i[i[file_name] < 0].expanding().std() # deviations of only the negative returns
            i['DownsideDev'] = downside_deviation_
            db.append(i)
        return db