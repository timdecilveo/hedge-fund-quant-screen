import os
import numpy as np
import pandas as pd
from scipy.stats import norm
from directories import Directory

class MonthlyStatistics:
    def __init__(self):
        self.directory = os.listdir(f"../data-files")
        self.fund_list = Directory(self.directory).files()
        self.benchmarks = os.listdir(f"../benchmarks")
        self.benchmark_list = Directory(self.benchmarks).benchmark()
        self.rf = 0.02 / 12

    def statistics(self):
        benchmark_stats = []
        fund_stats = []

        for benchmark in self.benchmark_list:
            benchmark_stats.append(benchmark)

        for fund in self.fund_list:
            file_name = fund.columns[0]
            dates = fund[file_name].index
            start_date = dates[0]
            end_date = dates[-1] #need to fix this so it's the rolling date

            # Basic Monthly Statistics
            fund['MonthlyReturn'] = fund[file_name]
            fund['AvgReturn'] = fund['MonthlyReturn'].expanding().mean()
            fund['MedianReturn'] = fund['MonthlyReturn'].expanding().median()
            fund['MaxReturn'] =  fund['MonthlyReturn'].expanding().max()
            fund['MinReturn'] = fund['MonthlyReturn'].expanding().min()
            fund['StDev'] =  fund['MonthlyReturn'].expanding().std()
            fund['Variance'] = fund['MonthlyReturn'].expanding().var()

            # Beta
            fund['Benchmark-Return'] = benchmark_stats[0]['SPY']
            fund['Benchmark-StDev'] = fund['Benchmark-Return'].expanding().std()
            fund['Benchmark-Correlation'] = fund['Benchmark-Return'].expanding().corr(fund['MonthlyReturn'])
            fund['Beta'] = fund['Benchmark-Correlation'] * (fund['StDev'] / fund['Benchmark-StDev'])

            # Downside Deviation of monthly percentage returns
            downside_deviation = fund['MonthlyReturn'][fund['MonthlyReturn'] < 0].expanding().std()
            fund['DownsideDev'] = downside_deviation
            fund['DownsideDev'].fillna(method="ffill", inplace=True)

            fund['Skew'] = fund['MonthlyReturn'].expanding().skew(axis=0)
            fund['Kurtosis'] = fund['MonthlyReturn'].expanding().kurt(axis=0)
            fund['Kurt*Skew'] = fund['Kurtosis'] * fund['Skew']
            fund['ExcessKurtosis'] = fund['Kurtosis'] - 3
            fund['ExcessKurtosis*Skew'] = fund['ExcessKurtosis'] * fund['Skew']

            # Compounded Monthly Return
            time_delta_days = (end_date - start_date).days
            years = time_delta_days / 365
            fund['CompoundedReturn'] = (fund['MonthlyReturn'] + 1).cumprod()
            # Compounded Annual Growth Rate
            fund['CAGR'] = ((fund['CompoundedReturn']) ** (1 / years)) - 1

            # Maximum Drawdown
            peak = fund['CompoundedReturn'].expanding(min_periods=1).max()
            drawdown = (fund['CompoundedReturn'] / peak) - 1
            fund['MaxDD'] = drawdown.min()
            # fund['MaxDD-BeginningDate'] = 
            # fund['MaxDD-EndingDate'] = 
            # fund['MaxDD-Duration-Months'] = 
            # fund['MaxDD-Duration-Years'] = 

            # Markowitz Return Function
            fund['MarkowitzReturnFunction'] = fund['AvgReturn'] / fund['Variance']
            fund['MarkowitzReturnFunction_CAGR'] = fund['CAGR'] / fund['Variance']

            fund['AvgReturn_StDev'] = fund['AvgReturn'] / fund['StDev']
            fund['MedianReturn_StDev'] = fund['MedianReturn'] / fund['StDev']
            fund['CAGR_StDev'] = fund['CAGR'] / fund['StDev']

            fund['AvgReturn_MaxDD'] = fund['AvgReturn'] / abs(fund['MaxDD'])
            fund['MedianReturn_MaxDD'] = fund['MedianReturn'] / abs(fund['MaxDD'])
            fund['CAGR_MaxDD'] = fund['CAGR'] / abs(fund['MaxDD'])

            # # ####################################
            # # information_ratio - - need benchmark data to calculate
            # # tail_ratio - - need to figure out how to calculate this

            # Treynor Ratio
            fund['TreynorRatio'] = (fund['AvgReturn'] - self.rf) / fund['Beta']
            fund['TreynorRatio_Annualized'] = fund['TreynorRatio'] * np.sqrt(12)

            # Sharpe Ratio
            fund['SharpeRatio'] = (fund['AvgReturn'] - self.rf) / fund['StDev']
            fund['SharpeRatio_Annualized'] = fund['SharpeRatio'] * np.sqrt(12)

            # Sortino Ratio
            fund['SortinoRatio'] = (fund['AvgReturn'] - self.rf) / fund['DownsideDev']
            fund['SortinoRatio_Annualized'] = fund['SortinoRatio'] * np.sqrt(12)

            # Calmar Ratio
            fund['CalmarRatio'] = (fund['AvgReturn'] - self.rf) / abs(fund['MaxDD'])
            fund['CalmarRatio_Annualized'] = fund['CalmarRatio'] * np.sqrt(12)

            # # Parametric/Gaussian VaR
            z = norm.ppf(0.05)
            fund['Gaussian_VaR'] = -(fund['AvgReturn'] + z * fund['MonthlyReturn'].std(ddof=0))

            # Modified Cornish Fisher VaR
            z = (z + (z**2 - 1) * fund['Skew'] / 6 + (z**3 - 3 * z) * (fund['Kurtosis'] - 3) / 24 - (2 * z**3 - 5 * z) * (fund['Skew']**2) / 36)
            fund['CornishFisher_VaR'] = -(fund['AvgReturn'] + z * fund['MonthlyReturn'].std(ddof=0))

            # Total Months
            fund['Total_NumOfPeriods'] = fund['MonthlyReturn'].expanding().count()
            
            # Winning Months
            fund['Winning_Return'] = fund['MonthlyReturn'][fund['MonthlyReturn'] > 0]
            fund['Winning_AvgReturn'] = fund['Winning_Return'].expanding().mean()
            fund['Winning_MedianReturn'] = fund['Winning_Return'].expanding().median()
            fund['Winning_MaxReturn'] = fund['Winning_Return'].expanding().max()
            fund['Winning_MinReturn'] = fund['Winning_Return'].expanding().min()
            fund['Winning_StDev'] = fund['Winning_Return'].expanding().std()
            fund['Winning_Variance'] = fund['Winning_Return'].expanding().var()
            fund['Winning_NumOfPeriods'] = fund['Winning_Return'].expanding().count()
            fund['WinningPerc'] = fund['Winning_NumOfPeriods'] / fund['Total_NumOfPeriods']

            # Losing Months
            fund['Losing_Return'] = fund['MonthlyReturn'][fund['MonthlyReturn'] < 0]
            fund['Losing_AvgReturn'] = fund['Losing_Return'].expanding().mean()
            fund['Losing_MedianReturn'] = fund['Losing_Return'].expanding().median()
            fund['Losing_MaxReturn'] = fund['Losing_Return'].expanding().max()
            fund['Losing_MinReturn'] = fund['Losing_Return'].expanding().min()
            fund['Losing_StDev'] = fund['Losing_Return'].expanding().std()
            fund['Losing_Variance'] = fund['Losing_Return'].expanding().var()
            fund['Losing_NumOfPeriods'] = fund['Losing_Return'].expanding().count()
            fund['LosingPerc'] = fund['Losing_NumOfPeriods'] / fund['Total_NumOfPeriods']

            # Win-Loss Calcs
            fund['Win_Loss_Ratio'] = fund['Winning_NumOfPeriods'] / fund['Losing_NumOfPeriods']
            fund['Expectancy'] = (fund['Winning_MedianReturn'] * fund['Winning_NumOfPeriods']) + (fund['Losing_MedianReturn'] * fund['Losing_NumOfPeriods'])
            fund['ExepectancyRatio'] = (fund['Winning_MedianReturn'] * fund['Winning_NumOfPeriods']) / abs((fund['Losing_MedianReturn'] * fund['Losing_NumOfPeriods']))
            
            # Gain to Pain Ratio
            fund['Sum_of_Returns'] = fund['MonthlyReturn'].expanding().sum()
            fund['Sum_of_Losses'] = fund['MonthlyReturn'][fund['MonthlyReturn'] < 0].expanding().sum()
            fund['Sum_of_Losses'].fillna(method='ffill', inplace=True)
            fund['Gain_to_Pain_Ratio'] = fund['Sum_of_Returns'] / abs(fund['Sum_of_Losses'])

            # Sharpe Ratio / Skew - average return - rf / skew
            fund['Sharpe_Ratio_Skew'] = (fund['AvgReturn'] - self.rf) / abs(fund['Skew'])

            fund_stats.append(fund)
        return fund_stats, benchmark_stats