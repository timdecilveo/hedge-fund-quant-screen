import os
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from directories import Directory

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

            '''
            Sharpe Ratio:
            sharpe ratio = (rp - rf) / standard deviation
                rp = average_return
                rf = self.rf
                standard deviation = standard_deviation
            '''
            sharpe = (average_return - self.rf) / standard_deviation

            '''
            Sortino Ratio:
            sortino ratio = (rp - rf) / downside deviation
                rp = average_return
                rf = self.rf
                downside deviation = downside_deviation
            '''
            sortino = (average_return - self.rf) / downside_deviation

            '''
            Calmar Ratio:
            calmar ratio = (rp - rf) / maximum drawdown
                rp = average_return
                rf = self.rf
                maximum drawdown = max_drawdown
            '''
            calmar = (average_return - self.rf) / abs(max_drawdown)

            '''
            Parametric/Gaussian VaR
            gaussian var = 
            '''
            z = norm.ppf(0.05)
            gaussian_var = -(average_return + z * monthly_return.std(ddof=0))

            '''
            Modified Cornish Fisher VaR
            cornish fisher var = 
            '''
            z = (z + (z**2 - 1) * skew / 6 + (z**3 - 3 * z) * (kurtosis - 3) / 24 - (2 * z**3 - 5 * z) * (skew**2) / 36)
            modified_cornish_fisher_var = -(average_return + z * monthly_return.std(ddof=0))

            '''
            Winning Months vs. Losing Months
            '''
            winning = monthly_return.gt(0)
            losing = monthly_return.lt(0)
            flat = monthly_return.eq(0)

            # Winning Months
            winning_average_return = i[winning].expanding().mean()
            winning_median_return = i[winning].expanding().median()
            winning_max_return = i[winning].expanding().max()
            winning_min_return = i[winning].expanding().min()
            winning_st_dev = i[winning].expanding().std()
            winning_num_periods = i[winning].expanding().count()

            # Losing Months
            losing_average_return = i[losing].expanding().mean()
            losing_median_return = i[losing].expanding().median()
            losing_max_return = i[losing].expanding().max()
            losing_min_return = i[losing].expanding().min()
            losing_st_dev = i[losing].expanding().std()
            losing_num_periods = i[losing].expanding().count()

            # Total Months
            total_num_periods = monthly_return.expanding().count()

            # Winning vs. Losing Months Calculations
            # Winning Months Calcs
            df_winning_periods_percentage = pd.merge_ordered(winning_num_periods, total_num_periods, on='Date', suffixes=('_win', '_total'), fill_method='ffill')
            index = df_winning_periods_percentage.columns[0]
            win_col = df_winning_periods_percentage.columns[1]
            total_col = df_winning_periods_percentage.columns[2]
            df_winning_periods_percentage.set_index(index, inplace=True)
            df_winning_periods_percentage['WinningPerc (%)'] = df_winning_periods_percentage[win_col] / df_winning_periods_percentage[total_col]
            winning_periods_percentage = df_winning_periods_percentage['WinningPerc (%)']

            # Losing Months Calcs
            df_losing_periods_percentage = pd.merge_ordered(losing_num_periods, total_num_periods, on='Date', suffixes=('_lose', '_total'), fill_method='ffill')
            index = df_losing_periods_percentage.columns[0]
            los_col = df_losing_periods_percentage.columns[1]
            total_col = df_losing_periods_percentage.columns[2]
            df_losing_periods_percentage.set_index(index, inplace=True)
            df_losing_periods_percentage['LosingPerc (%)'] = df_losing_periods_percentage[los_col] / df_losing_periods_percentage[total_col]
            losing_periods_percentage = df_losing_periods_percentage['LosingPerc (%)']


            win_loss_ratio = winning_num_periods / losing_num_periods
            expectancy = (winning_median_return * winning_num_periods) + (losing_median_return * losing_num_periods)
            expectancy_ratio = (winning_median_return * winning_num_periods) / abs((losing_median_return * losing_num_periods))

            # ####################################
            i['MonthlyReturn'] = monthly_return
            i['AvgReturn'] = average_return
            i['MedianReturn'] = median_reutrn
            i['MaxReturn'] = maximum_return
            i['MinReturn'] = minimum_return
            i['StDev'] = standard_deviation
            i['DownsideDev'] = downside_deviation
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
            # gain to pain ratio
            # information_ratio
            i['SharpeRatio'] = sharpe
            i['SharpeRatioAnnualized'] = sharpe * np.sqrt(12)
            # i['SortinoRatio'] = sortino
            # i['SortinoRatioAnnualized'] = sortino * np.sqrt(12)
            i['CalmarRatio'] = calmar
            i['CalmarRatioAnnualized'] = calmar * np.sqrt(12)
            i['Gaussian VaR'] = gaussian_var
            i['CornishFisher VaR'] = modified_cornish_fisher_var
            i['Winning-AvgReturn'] = winning_average_return
            i['Winning-MedianReturn'] = winning_median_return
            i['Winning-MaxReturn'] = winning_max_return
            i['Winning-MinReturn'] = winning_min_return
            i['Winning-StDev'] = winning_st_dev
            i['Winning-NumOfPeriods'] = winning_num_periods
            i['Losing-AvgReturn'] = losing_average_return
            i['Losing-MedianReturn'] = losing_median_return
            i['Losing-MaxReturn'] = losing_max_return
            i['Losing-MinReturn'] = losing_min_return
            i['Losing-StDev'] = losing_st_dev
            i['Losing-NumOfPeriods'] = losing_num_periods
            i['Total-NumOfPeriods'] = total_num_periods
            i['WinningPerc (%)'] = winning_periods_percentage
            i['LosingPerc (%)'] = losing_periods_percentage
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