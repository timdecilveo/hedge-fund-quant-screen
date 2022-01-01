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

            i['MonthlyReturn'] = i[file_name]
            i['AvgReturn'] = i['MonthlyReturn'].expanding().mean()
            i['MedianReturn'] = i['MonthlyReturn'].expanding().median()
            i['MaxReturn'] =  i['MonthlyReturn'].expanding().max()
            i['MinReturn'] = i['MonthlyReturn'].expanding().min()
            i['StDev'] =  i['MonthlyReturn'].expanding().std()
            i['Variance'] = i['MonthlyReturn'].expanding().var()

            # # downside deviation of monthly percentage returns
            downside_deviation = i['MonthlyReturn'][i['MonthlyReturn'] < 0].expanding().std()
            i['DownsideDev'] = downside_deviation
            i['DownsideDev'].fillna(method="ffill", inplace=True)

            i['Skew'] = i['MonthlyReturn'].expanding().skew(axis=0)
            i['Kurtosis'] = i['MonthlyReturn'].expanding().kurt(axis=0)
            i['Kurt*Skew'] = i['Kurtosis'] * i['Skew']
            i['ExcessKurtosis'] = i['Kurtosis'] - 3
            i['ExcessKurtosis*Skew'] = i['ExcessKurtosis'] * i['Skew']

            time_delta_days = (end_date - start_date).days
            years = time_delta_days / 365
            i['CompoundedReturn'] = (i['MonthlyReturn'] + 1).cumprod()
            i['CAGR'] = ((i['CompoundedReturn']) ** (1 / years)) - 1

            peak = i['CompoundedReturn'].expanding(min_periods=1).max()
            drawdown = (i['CompoundedReturn'] / peak) - 1
            i['MaxDD'] = drawdown.min()
            # # max_dd beginning date
            # # max_dd ending date
            # # max_dd in months
            # # max_dd in years
            # # max_dd duration

            i['MarkowitzReturnFunction'] = i['AvgReturn'] / i['Variance']
            i['MarkowitzReturnFunction (CAGR)'] = i['CAGR'] / i['Variance']

            i['AvgReturn/StDev'] = i['AvgReturn'] / i['StDev']
            i['MedianReturn/StDev'] = i['MedianReturn'] / i['StDev']
            i['CAGR/StDev'] = i['CAGR'] / i['StDev']

            i['AvgReturn/MaxDD'] = i['AvgReturn'] / abs(i['MaxDD'])
            i['MedianReturn/MaxDD'] = i['MedianReturn'] / abs(i['MaxDD'])
            i['CAGR/MaxDD'] = i['CAGR'] / abs(i['MaxDD'])

            # # ####################################
            # # gain to pain ratio
            # # information_ratio
            # # tail_ratio
            # # treynor_ratio

            i['SharpeRatio'] = (i['AvgReturn'] - self.rf) / i['StDev']
            i['SharpeRatio-Annualized'] = i['SharpeRatio'] * np.sqrt(12)

            i['SortinoRatio'] = (i['AvgReturn'] - self.rf) / i['DownsideDev']
            i['SortinoRatio-Annualized'] = i['SortinoRatio'] * np.sqrt(12)

            i['CalmarRatio'] = (i['AvgReturn'] - self.rf) / abs(i['MaxDD'])
            i['CalmarRatio-Annualized'] = i['CalmarRatio'] * np.sqrt(12)

            # # Parametric/Gaussian VaR
            z = norm.ppf(0.05)
            i['Gaussian VaR'] = -(i['AvgReturn'] + z * i['MonthlyReturn'].std(ddof=0))

            # Modified Cornish Fisher VaR
            z = (z + (z**2 - 1) * i['Skew'] / 6 + (z**3 - 3 * z) * (i['Kurtosis'] - 3) / 24 - (2 * z**3 - 5 * z) * (i['Skew']**2) / 36)
            i['CornishFisher VaR'] = -(i['AvgReturn'] + z * i['MonthlyReturn'].std(ddof=0))

            # Total Months
            i['Total-NumOfPeriods'] = i['MonthlyReturn'].expanding().count()
            
            # Winning Months
            i['Winning-Return'] = i['MonthlyReturn'][i['MonthlyReturn'] > 0]
            i['Winning-AvgReturn'] = i['Winning-Return'].expanding().mean()
            i['Winning-MedianReturn'] = i['Winning-Return'].expanding().median()
            i['Winning-MaxReturn'] = i['Winning-Return'].expanding().max()
            i['Winning-MinReturn'] = i['Winning-Return'].expanding().min()
            i['Winning-StDev'] = i['Winning-Return'].expanding().std()
            i['Winning-Variance'] = i['Winning-Return'].expanding().var()
            i['Winning-NumOfPeriods'] = i['Winning-Return'].expanding().count()
            i['WinningPerc (%)'] = i['Winning-NumOfPeriods'] / i['Total-NumOfPeriods']

            # Losing Months
            i['Losing-Return'] = i['MonthlyReturn'][i['MonthlyReturn'] < 0]
            i['Losing-AvgReturn'] = i['Losing-Return'].expanding().mean()
            i['Losing-MedianReturn'] = i['Losing-Return'].expanding().median()
            i['Losing-MaxReturn'] = i['Losing-Return'].expanding().max()
            i['Losing-MinReturn'] = i['Losing-Return'].expanding().min()
            i['Losing-StDev'] = i['Losing-Return'].expanding().std()
            i['Losing-Variance'] = i['Losing-Return'].expanding().var()
            i['Losing-NumOfPeriods'] = i['Losing-Return'].expanding().count()
            i['LosingPerc (%)'] = i['Losing-NumOfPeriods'] / i['Total-NumOfPeriods']

            # Win-Loss Calcs
            i['Win-Loss Ratio'] = i['Winning-NumOfPeriods'] / i['Losing-NumOfPeriods']
            i['Expectancy (+)'] = (i['Winning-MedianReturn'] * i['Winning-NumOfPeriods']) + (i['Losing-MedianReturn'] * i['Losing-NumOfPeriods'])
            i['ExepectancyRatio (%)'] = (i['Winning-MedianReturn'] * i['Winning-NumOfPeriods']) / abs((i['Losing-MedianReturn'] * i['Losing-NumOfPeriods']))

            db.append(i)
        return db