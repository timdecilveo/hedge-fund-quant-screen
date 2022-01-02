import numpy as np
import pandas as pd
from monthlyStatistics import MonthlyStatistics

class RankingModel:
    def __init__(self):
        self.monthlyStats = MonthlyStatistics()
    
    def ranking_model(self):
        fund_stats, benchmark_stats = self.monthlyStats.statistics()

        MonthlyReturn = []
        AvgReturn = []
        MedianReturn = []
        MaxReturn = []
        MinReturn = []
        StDev = []
        Variance = []
        Benchmark_Return = []
        Benchmark_StDev = []
        Benchmark_Correlation = []
        Beta = []
        DownsideDev = []
        Skew = []
        Kurtosis = []
        Kurt_times_Skew = []
        ExcessKurtosis = []
        ExcessKurtosis_Skew = []
        CompoundedReturn = []
        Cagr = []
        MaxDD = []
        MarkowitzReturnFunction = []
        MarkowitzReturnFunction_Cagr = []
        AvgReturn_StDev = []
        MedianReturn_StDev = []
        Cagr_StDev = []
        AvgReturn_MaxDD = []
        MedianReturn_MaxDD = []
        Cagr_MaxDD = []
        TreynorRatio = []
        TreynorRatio_Annualized = []
        SharpeRatio = []
        SharpeRatio_Annualized = []
        SortinoRatio = []
        SortinoRatio_Annualized = []
        CalmarRatio = []
        CalmarRatio_Annualized = []
        Gaussian_VaR = []
        CornishFisher_VaR = []
        Total_NumOfPeriods = []
        Winning_Return = []
        Winning_AvgReturn = []
        Winning_MedianReturn = []
        Winning_MaxReturn = []
        Winning_MinReturn = []
        Winning_StDev = []
        Winning_Variance = []
        Winning_NumOfPeriods = []
        WinningPerc = []
        Losing_Return = []
        Losing_AvgReturn = []
        Losing_MedianReturn = []
        Losing_MaxReturn = []
        Losing_MinReturn = []
        Losing_StDev = []
        Losing_Variance = []
        Losing_NumOfPeriods = []
        LosingPerc = []
        Win_Loss_Ratio = []
        Expectancy = []
        ExepectancyRatio = []
        Sum_of_Returns = []
        Sum_of_Losses = []
        Gain_to_Pain_Ratio = []
        Sharpe_Ratio_Skew = []

        for fund_stat in fund_stats:
            features = fund_stat.columns[1:]
            dates = fund_stat.index
            start_date = dates[0]
            end_date = dates[-1]
            fund_name = fund_stat.columns[0]
            names = ['FundName', 'Statistic']

            # Need to rank by highest and lowest value depending on feature
            df = pd.DataFrame(fund_stat)
            # print(df)
            # print('-----')
            df2 = pd.MultiIndex.from_frame(df)
            print(df2)
            print('--end new--')












            # rank_MonthlyReturn = pd.DataFrame()
            # rank_MonthlyReturn[f'MonthlyReturn-{fund_name}'] = fund_stat['MonthlyReturn']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_AvgReturn = pd.DataFrame()
            # rank_AvgReturn[f'AvgReturn-{fund_name}'] = fund_stat['AvgReturn']
            # AvgReturn.append(rank_AvgReturn)
            
            # rank_MedianReturn = pd.DataFrame()
            # rank_MedianReturn[f'MedianReturn-{fund_name}'] = fund_stat['MedianReturn']
            # MedianReturn.append(rank_MedianReturn)
            
            # rank_MaxReturn = pd.DataFrame()
            # rank_MaxReturn[f'MaxReturn-{fund_name}'] = fund_stat['MaxReturn']
            # MaxReturn.append(rank_MaxReturn)
            
            # rank_MinReturn = pd.DataFrame()
            # rank_MinReturn[f'MinReturn-{fund_name}'] = fund_stat['MinReturn']
            # MinReturn.append(rank_MinReturn)
            
            # rank_StDev = pd.DataFrame()
            # rank_StDev[f'StDev-{fund_name}'] = fund_stat['StDev']
            # StDev.append(rank_StDev)
            
            # rank_Variance = pd.DataFrame()
            # rank_Variance[f'Variance-{fund_name}'] = fund_stat['Variance']
            # Variance.append(rank_Variance)
            
            # rank_Benchmark_Return = pd.DataFrame()
            # rank_Benchmark_Return[f'Benchmark-Return-{fund_name}'] = fund_stat['Benchmark-Return']
            # Benchmark_Return.append(rank_Benchmark_Return)
            
            # rank_Benchmark_StDev = pd.DataFrame()
            # rank_Benchmark_StDev[f'Benchmark-StDev-{fund_name}'] = fund_stat['Benchmark-StDev']
            # Benchmark_StDev.append(rank_Benchmark_StDev)
            
            # rank_Benchmark_Correlation = pd.DataFrame()
            # rank_Benchmark_Correlation[f'Benchmark-Correlation-{fund_name}'] = fund_stat['Benchmark-Correlation']
            # Benchmark_Correlation.append(rank_Benchmark_Correlation)
            
            # rank_Beta = pd.DataFrame()
            # rank_Beta[f'Beta-{fund_name}'] = fund_stat['Beta']
            # Beta.append(rank_Beta)
            
            # rank_DownsideDev = pd.DataFrame()
            # rank_DownsideDev[f'DownsideDev-{fund_name}'] = fund_stat['DownsideDev']
            # DownsideDev.append(rank_DownsideDev)
            
            # rank_Skew = pd.DataFrame()
            # rank_Skew[f'Skew-{fund_name}'] = fund_stat['Skew']
            # Skew.append(rank_Skew)
    
            # rank_Kurtosis = pd.DataFrame()
            # rank_Kurtosis[f'Kurtosis-{fund_name}'] = fund_stat['Kurtosis']
            # Kurtosis.append(rank_Kurtosis)
            
            # rank_Kurt_times_Skew = pd.DataFrame()
            # rank_Kurt_times_Skew[f'Kurt*Skew-{fund_name}'] = fund_stat['Kurt*Skew']
            # Kurt_times_Skew.append(rank_Kurt_times_Skew)

        # ExcessKurtosis = []
        # ExcessKurtosis_Skew = []
        # CompoundedReturn = []
        # Cagr = []
        # MaxDD = []
        # MarkowitzReturnFunction = []
        # MarkowitzReturnFunction_Cagr = []
        # AvgReturn_StDev = []
        # MedianReturn_StDev = []
        # Cagr_StDev = []
        # AvgReturn_MaxDD = []
        # MedianReturn_MaxDD = []
        # Cagr_MaxDD = []
        # TreynorRatio = []
        # TreynorRatio_Annualized = []
        # SharpeRatio = []
        # SharpeRatio_Annualized = []
        # SortinoRatio = []
        # SortinoRatio_Annualized = []
        # CalmarRatio = []
        # CalmarRatio_Annualized = []
        # Gaussian_VaR = []
        # CornishFisher_VaR = []
        # Total_NumOfPeriods = []
        # Winning_Return = []
        # Winning_AvgReturn = []
        # Winning_MedianReturn = []
        # Winning_MaxReturn = []
        # Winning_MinReturn = []
        # Winning_StDev = []
        # Winning_Variance = []
        # Winning_NumOfPeriods = []
        # WinningPerc = []
        # Losing_Return = []
        # Losing_AvgReturn = []
        # Losing_MedianReturn = []
        # Losing_MaxReturn = []
        # Losing_MinReturn = []
        # Losing_StDev = []
        # Losing_Variance = []
        # Losing_NumOfPeriods = []
        # LosingPerc = []
        # Win_Loss_Ratio = []
        # Expectancy = []
        # ExepectancyRatio = []
        # Sum_of_Returns = []
        # Sum_of_Losses = []
        # Gain_to_Pain_Ratio = []
        # Sharpe_Ratio_Skew = []
            










            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'ExcessKurtosis-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'ExcessKurtosis*Skew-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CompoundedReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CAGR-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'MaxDD-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'MarkowitzReturnFunction-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'MarkowitzReturnFunction (CAGR)-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'AvgReturn/StDev-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'MedianReturn/StDev-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CAGR/StDev-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'AvgReturn/MaxDD-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'MedianReturn/MaxDD-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CAGR/MaxDD-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'TreynorRatio-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'TreynorRatio-Annualized-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'SharpeRatio-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'SharpeRatio-Annualized-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'SortinoRatio-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'SortinoRatio-Annualized-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CalmarRatio-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CalmarRatio-Annualized-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Gaussian VaR-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'CornishFisher VaR-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Total-NumOfPeriods-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-Return-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
    
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-AvgReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-MedianReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-MaxReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-MinReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-StDev-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-Variance-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Winning-NumOfPeriods-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'WinningPerc-(%)-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-Return-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-AvgReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-MedianReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-MaxReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-MinReturn-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-StDev-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-Variance-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Losing-NumOfPeriods-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'LosingPerc-(%)-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Win-Loss-Ratio-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Expectancy-(+)-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'ExepectancyRatio-(%)-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Sum-of-Returns-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Sum-of-Losses-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Gain-to-Pain-Ratio-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)

            # rank_MonthlyReturn = pd.DataFrame()
            # # rank_[f'Sharpe-Ratio / Skew-{fund_name}'] = fund_stat['']
            # MonthlyReturn.append(rank_MonthlyReturn)
            
        # final_MonthlyReturn = pd.concat(MonthlyReturn)
        # final_AvgReturn = pd.concat(AvgReturn)
        # final_MedianReturn = pd.concat(MedianReturn)
        # final_MaxReturn = pd.concat(MaxReturn)
        # final_MinReturn = pd.concat(MinReturn)
        # final_StDev = pd.concat(StDev)
        # final_Variance = pd.concat(Variance)
        # final_Benchmark_Return = pd.concat(Benchmark_Return)
        # final_Benchmark_StDev = pd.concat(Benchmark_StDev)
        # final_Benchmark_Correlation = pd.concat(Benchmark_Correlation)
        # final_Beta = pd.concat(Beta)
        # final_DownsideDev = pd.concat(DownsideDev)
        # final_Skew = pd.concat(Skew)
        # final_Kurtosis = pd.concat(Kurtosis)
        # final_Kurt_times_Skew = pd.concat(Kurt_times_Skew)
        # final_ = pd.concat(ExcessKurtosis)
        # final_ = pd.concat(ExcessKurtosis_Skew)
        # final_ = pd.concat(CompoundedReturn)
        # final_ = pd.concat(Cagr)
        # final_ = pd.concat(MaxDD)
        # final_ = pd.concat(MarkowitzReturnFunction)
        # final_ = pd.concat(MarkowitzReturnFunction_Cagr)
        # final_ = pd.concat(AvgReturn_StDev)
        # final_ = pd.concat(MedianReturn_StDev)
        # final_ = pd.concat(Cagr_StDev)
        # final_ = pd.concat(AvgReturn_MaxDD)
        # final_ = pd.concat(MedianReturn_MaxDD)
        # final_ = pd.concat(Cagr_MaxDD)
        # final_ = pd.concat(TreynorRatio)
        # final_ = pd.concat(TreynorRatio_Annualized)
        # final_ = pd.concat(SharpeRatio)
        # final_ = pd.concat(SharpeRatio_Annualized)
        # final_ = pd.concat(SortinoRatio)
        # final_ = pd.concat(SortinoRatio_Annualized)
        # final_ = pd.concat(CalmarRatio)
        # final_ = pd.concat(CalmarRatio_Annualized)
        # final_ = pd.concat(Gaussian_VaR)
        # final_ = pd.concat(CornishFisher_VaR)
        # final_ = pd.concat(Total_NumOfPeriods)
        # final_ = pd.concat(Winning_Return)
        # final_ = pd.concat(Winning_AvgReturn)
        # final_ = pd.concat(Winning_MedianReturn)
        # final_ = pd.concat(Winning_MaxReturn)
        # final_ = pd.concat(Winning_MinReturn)
        # final_ = pd.concat(Winning_StDev)
        # final_ = pd.concat(Winning_Variance)
        # final_ = pd.concat(Winning_NumOfPeriods)
        # final_ = pd.concat(WinningPerc)
        # final_ = pd.concat(Losing_Return)
        # final_ = pd.concat(Losing_AvgReturn)
        # final_ = pd.concat(Losing_MedianReturn)
        # final_ = pd.concat(Losing_MaxReturn)
        # final_ = pd.concat(Losing_MinReturn)
        # final_ = pd.concat(Losing_StDev)
        # final_ = pd.concat(Losing_Variance)
        # final_ = pd.concat(Losing_NumOfPeriods)
        # final_ = pd.concat(LosingPerc)
        # final_ = pd.concat(Win_Loss_Ratio)
        # final_ = pd.concat(Expectancy)
        # final_ = pd.concat(ExepectancyRatio)
        # final_ = pd.concat(Sum_of_Returns)
        # final_ = pd.concat(Sum_of_Losses)
        # final_ = pd.concat(Gain_to_Pain_Ratio)
        # final_ = pd.concat(Sharpe_Ratio_Skew)

        # print(f"final_MonthlyReturn:\n{final_MonthlyReturn}")
        # print(f"final_AvgReturn:\n{final_AvgReturn}")
        # print(f"final_MedianReturn:\n{final_MedianReturn}")
        # print(f"final_MaxReturn:\n{final_MaxReturn}")
        # print(f"final_MinReturn:\n{final_MinReturn}")
        # print(f"final_StDev:\n{final_StDev}")
        # print(f"final_Variance:\n{final_Variance}")
        # print(f"final_Benchmark_Return:\n{final_Benchmark_Return}")
        # print(f"final_Benchmark_StDev:\n{final_Benchmark_StDev}")
        # print(f"final_Benchmark_Correlation:\n{final_Benchmark_Correlation}")
        # print(f"final_Beta:\n{final_Beta}")
        # print(f"final_DownsideDev:\n{final_DownsideDev}")
        # print(f"final_Skew:\n{final_Skew}")
        # print(f"final_Kurtosis:\n{final_Kurtosis}")
        # print(f"final_Kurt_times_Skew:\n{final_Kurt_times_Skew}")
