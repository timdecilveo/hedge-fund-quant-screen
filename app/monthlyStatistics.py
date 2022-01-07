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
    
    def files(self):
        files = []
        for fund in self.fund_list:
            file_name = fund.columns[0]
            files.append(file_name)
        return files

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
            fund['BenchmarkReturn'] = benchmark_stats[0]['SPY']
            fund['BenchmarkStDev'] = fund['BenchmarkReturn'].expanding().std()
            fund['BenchmarkCorrelation'] = fund['BenchmarkReturn'].expanding().corr(fund['MonthlyReturn'])
            fund['Beta'] = fund['BenchmarkCorrelation'] * (fund['StDev'] / fund['BenchmarkStDev'])

            # Downside Deviation of monthly percentage returns
            downside_deviation = fund['MonthlyReturn'][fund['MonthlyReturn'] < 0].expanding().std()
            fund['DownsideDev'] = downside_deviation
            fund['DownsideDev'].fillna(method="ffill", inplace=True)

            fund['Skew'] = fund['MonthlyReturn'].expanding().skew(axis=0)
            fund['Kurtosis'] = fund['MonthlyReturn'].expanding().kurt(axis=0)
            fund['KurtTimesSkew'] = fund['Kurtosis'] * fund['Skew']
            fund['ExcessKurtosis'] = fund['Kurtosis'] - 3
            fund['ExcessKurtosisRimesSkew'] = fund['ExcessKurtosis'] * fund['Skew']

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
            fund['MarkowitzReturnFunctionCAGR'] = fund['CAGR'] / fund['Variance']

            fund['AvgReturnStDev'] = fund['AvgReturn'] / fund['StDev']
            fund['MedianReturnStDev'] = fund['MedianReturn'] / fund['StDev']
            fund['CAGRStDev'] = fund['CAGR'] / fund['StDev']

            fund['AvgReturnMaxDD'] = fund['AvgReturn'] / abs(fund['MaxDD'])
            fund['MedianReturnMaxDD'] = fund['MedianReturn'] / abs(fund['MaxDD'])
            fund['CAGRMaxDD'] = fund['CAGR'] / abs(fund['MaxDD'])

            # # ####################################
            # # information_ratio - - need benchmark data to calculate
            # # tail_ratio - - need to figure out how to calculate this

            # Treynor Ratio
            fund['TreynorRatio'] = (fund['AvgReturn'] - self.rf) / fund['Beta']
            fund['TreynorRatioAnnualized'] = fund['TreynorRatio'] * np.sqrt(12)

            # Sharpe Ratio
            fund['SharpeRatio'] = (fund['AvgReturn'] - self.rf) / fund['StDev']
            fund['SharpeRatioAnnualized'] = fund['SharpeRatio'] * np.sqrt(12)

            # Sortino Ratio
            fund['SortinoRatio'] = (fund['AvgReturn'] - self.rf) / fund['DownsideDev']
            fund['SortinoRatioAnnualized'] = fund['SortinoRatio'] * np.sqrt(12)

            # Calmar Ratio
            fund['CalmarRatio'] = (fund['AvgReturn'] - self.rf) / abs(fund['MaxDD'])
            fund['CalmarRatioAnnualized'] = fund['CalmarRatio'] * np.sqrt(12)

            # # Parametric/Gaussian VaR
            z = norm.ppf(0.05)
            fund['GaussianVaR'] = -(fund['AvgReturn'] + z * fund['MonthlyReturn'].std(ddof=0))

            # Modified Cornish Fisher VaR
            z = (z + (z**2 - 1) * fund['Skew'] / 6 + (z**3 - 3 * z) * (fund['Kurtosis'] - 3) / 24 - (2 * z**3 - 5 * z) * (fund['Skew']**2) / 36)
            fund['CornishFisherVaR'] = -(fund['AvgReturn'] + z * fund['MonthlyReturn'].std(ddof=0))

            # Total Months
            fund['TotalNumOfPeriods'] = fund['MonthlyReturn'].expanding().count()
            
            # Winning Months
            fund['WinningReturn'] = fund['MonthlyReturn'][fund['MonthlyReturn'] > 0]
            fund['WinningAvgReturn'] = fund['WinningReturn'].expanding().mean()
            fund['WinningMedianReturn'] = fund['WinningReturn'].expanding().median()
            fund['WinningMaxReturn'] = fund['WinningReturn'].expanding().max()
            fund['WinningMinReturn'] = fund['WinningReturn'].expanding().min()
            fund['WinningStDev'] = fund['WinningReturn'].expanding().std()
            fund['WinningVariance'] = fund['WinningReturn'].expanding().var()
            fund['WinningNumOfPeriods'] = fund['WinningReturn'].expanding().count()
            fund['WinningPerc'] = fund['WinningNumOfPeriods'] / fund['TotalNumOfPeriods']

            # Losing Months
            fund['LosingReturn'] = fund['MonthlyReturn'][fund['MonthlyReturn'] < 0]
            fund['LosingAvgReturn'] = fund['LosingReturn'].expanding().mean()
            fund['LosingMedianReturn'] = fund['LosingReturn'].expanding().median()
            fund['LosingMaxReturn'] = fund['LosingReturn'].expanding().max()
            fund['LosingMinReturn'] = fund['LosingReturn'].expanding().min()
            fund['LosingStDev'] = fund['LosingReturn'].expanding().std()
            fund['LosingVariance'] = fund['LosingReturn'].expanding().var()
            fund['LosingNumOfPeriods'] = fund['LosingReturn'].expanding().count()
            fund['LosingPerc'] = fund['LosingNumOfPeriods'] / fund['TotalNumOfPeriods']

            # Win-Loss Calcs
            fund['WinLossRatio'] = fund['WinningNumOfPeriods'] / fund['LosingNumOfPeriods']
            fund['Expectancy'] = (fund['WinningMedianReturn'] * fund['WinningNumOfPeriods']) + (fund['LosingMedianReturn'] * fund['LosingNumOfPeriods'])
            fund['ExepectancyRatio'] = (fund['WinningMedianReturn'] * fund['WinningNumOfPeriods']) / abs((fund['LosingMedianReturn'] * fund['LosingNumOfPeriods']))
            
            # Gain to Pain Ratio
            fund['SumOfReturns'] = fund['MonthlyReturn'].expanding().sum()
            fund['SumOfLosses'] = fund['MonthlyReturn'][fund['MonthlyReturn'] < 0].expanding().sum()
            fund['SumOfLosses'].fillna(method='ffill', inplace=True)
            fund['GainToPainRatio'] = fund['SumOfReturns'] / abs(fund['SumOfLosses'])

            # Sharpe Ratio / Skew - average return - rf / skew
            fund['SharpeRatioSkew'] = (fund['AvgReturn'] - self.rf) / abs(fund['Skew'])

            fund_stats.append(fund)
        return fund_stats, benchmark_stats