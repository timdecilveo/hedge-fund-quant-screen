import numpy as np
import pandas as pd
from monthlyStatistics import MonthlyStatistics

class RankingModel:
    def __init__(self):
        self.monthlyStats = MonthlyStatistics()
    
    def metrics_dataframes(self):
        fund_stats, benchmark_stats = self.monthlyStats.statistics()
        q_deciles = 10
        q_quartiles = 4
        label_quartiles = ['1stQ', '2ndQ', '3rdQ', '4thQ']

        df_AvgReturn = pd.DataFrame()
        df_MedianReturn = pd.DataFrame()
        df_MaxReturn = pd.DataFrame()
        df_MinReturn = pd.DataFrame()
        df_StDev = pd.DataFrame()
        df_Variance = pd.DataFrame()
        df_Beta = pd.DataFrame()
        df_DownsideDev = pd.DataFrame()
        df_Skew = pd.DataFrame()
        df_Kurtosis = pd.DataFrame()
        df_Kurt_Skew = pd.DataFrame()
        df_ExcessKurtosis = pd.DataFrame()
        df_ExcessKurtosis_Skew = pd.DataFrame()
        df_CompoundedReturn = pd.DataFrame()
        df_CAGR = pd.DataFrame()
        df_MaxDD = pd.DataFrame()
        df_MarkowitzReturnFunction = pd.DataFrame()
        df_MarkowitzReturnFunction_CAGR = pd.DataFrame()
        df_AvgReturn_StDev = pd.DataFrame()
        df_MedianReturn_StDev = pd.DataFrame()
        df_CAGR_StDev = pd.DataFrame()
        df_AvgReturn_MaxDD = pd.DataFrame()
        df_MedianReturn_MaxDD = pd.DataFrame()
        df_CAGR_MaxDD = pd.DataFrame()
        df_TreynorRatio = pd.DataFrame()
        df_TreynorRatio_Annualized = pd.DataFrame()
        df_SharpeRatio = pd.DataFrame()
        df_SharpeRatio_Annualized = pd.DataFrame()
        df_SortinoRatio = pd.DataFrame()
        df_SortinoRatio_Annualized = pd.DataFrame()
        df_CalmarRatio = pd.DataFrame()
        df_CalmarRatio_Annualized = pd.DataFrame()
        df_Gaussian_VaR = pd.DataFrame()
        df_CornishFisher_VaR = pd.DataFrame()
        df_Total_NumOfPeriods = pd.DataFrame()
        df_Winning_AvgReturn = pd.DataFrame()
        df_Winning_MedianReturn = pd.DataFrame()
        df_Winning_MaxReturn = pd.DataFrame()
        df_Winning_MinReturn = pd.DataFrame()
        df_Winning_StDev = pd.DataFrame()
        df_Winning_Variance = pd.DataFrame()
        df_Winning_NumOfPeriods = pd.DataFrame()
        df_WinningPerc = pd.DataFrame()
        df_Losing_AvgReturn = pd.DataFrame()
        df_Losing_MedianReturn = pd.DataFrame()
        df_Losing_MaxReturn = pd.DataFrame()
        df_Losing_MinReturn = pd.DataFrame()
        df_Losing_StDev = pd.DataFrame()
        df_Losing_Variance = pd.DataFrame()
        df_Losing_NumOfPeriods = pd.DataFrame()
        df_LosingPerc = pd.DataFrame()
        df_Win_Loss_Ratio = pd.DataFrame()
        df_Expectancy = pd.DataFrame()
        df_ExepectancyRatio = pd.DataFrame()
        df_Sum_of_Returns = pd.DataFrame()
        df_Sum_of_Losses = pd.DataFrame()
        df_Gain_to_Pain_Ratio = pd.DataFrame()
        df_Sharpe_Ratio_Skew = pd.DataFrame()

        for fund_stat in fund_stats:
            features = fund_stat.columns[1:]
            fund_name = fund_stat.columns[0]
            # dates = fund_stat[fund_name].index

            for feature in features:
                if feature == 'AvgReturn':
                    df_AvgReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MedianReturn':
                    df_MedianReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MaxReturn':
                    df_MaxReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MinReturn':
                    df_MinReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'StDev':
                    df_StDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Variance':
                    df_Variance[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Beta':
                    df_Beta[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'DownsideDev':
                    df_DownsideDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Skew':
                    df_Skew[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Kurtosis':
                    df_Kurtosis[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Kurt*Skew':
                    df_Kurt_Skew[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExcessKurtosis':
                    df_ExcessKurtosis[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExcessKurtosis*Skew':
                    df_ExcessKurtosis_Skew[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CompoundedReturn':
                    df_CompoundedReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CAGR':
                    df_CAGR[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MaxDD':
                    df_MaxDD[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MarkowitzReturnFunction':
                    df_MarkowitzReturnFunction[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MarkowitzReturnFunction_CAGR':
                    df_MarkowitzReturnFunction_CAGR[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'AvgReturn_StDev':
                    df_AvgReturn_StDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MedianReturn_StDev':
                    df_MedianReturn_StDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CAGR_StDev':
                    df_CAGR_StDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'AvgReturn_MaxDD':
                    df_AvgReturn_MaxDD[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MedianReturn_MaxDD':
                    df_MedianReturn_MaxDD[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CAGR_MaxDD':
                    df_CAGR_MaxDD[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'TreynorRatio':
                    df_TreynorRatio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'TreynorRatio_Annualized':
                    df_TreynorRatio_Annualized[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SharpeRatio':
                    df_SharpeRatio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SharpeRatio_Annualized':
                    df_SharpeRatio_Annualized[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SortinoRatio':
                    df_SortinoRatio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SortinoRatio_Annualized':
                    df_SortinoRatio_Annualized[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CalmarRatio':
                    df_CalmarRatio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CalmarRatio_Annualized':
                    df_CalmarRatio_Annualized[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Gaussian_VaR':
                    df_Gaussian_VaR[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CornishFisher_VaR':
                    df_CornishFisher_VaR[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Total_NumOfPeriods':
                    df_Total_NumOfPeriods[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_AvgReturn':
                    df_Winning_AvgReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_MedianReturn':
                    df_Winning_MedianReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_MaxReturn':
                    df_Winning_MaxReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_MinReturn':
                    df_Winning_MinReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_StDev':
                    df_Winning_StDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_Variance':
                    df_Winning_Variance[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Winning_NumOfPeriods':
                    df_Winning_NumOfPeriods[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinningPerc':
                    df_WinningPerc[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_AvgReturn':
                    df_Losing_AvgReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_MedianReturn':
                    df_Losing_MedianReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_MaxReturn':
                    df_Losing_MaxReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_MinReturn':
                    df_Losing_MinReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_StDev':
                    df_Losing_StDev[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_Variance':
                    df_Losing_Variance[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Losing_NumOfPeriods':
                    df_Losing_NumOfPeriods[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'LosingPerc':
                    df_LosingPerc[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Win_Loss_Ratio':
                    df_Win_Loss_Ratio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Expectancy':
                    df_Expectancy[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExepectancyRatio':
                    df_ExepectancyRatio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Sum_of_Returns':
                    df_Sum_of_Returns[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Sum_of_Losses':
                    df_Sum_of_Losses[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Gain_to_Pain_Ratio':
                    df_Gain_to_Pain_Ratio[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Sharpe_Ratio_Skew':
                    df_Sharpe_Ratio_Skew[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
        
        return df_AvgReturn, df_MedianReturn, df_MaxReturn, df_MinReturn, df_StDev, df_Variance, df_Beta, df_DownsideDev, df_Skew, df_Kurtosis, df_Kurt_Skew, df_ExcessKurtosis, df_ExcessKurtosis_Skew, df_CompoundedReturn, df_CAGR, df_MaxDD, df_MarkowitzReturnFunction, df_MarkowitzReturnFunction_CAGR, df_AvgReturn_StDev, df_MedianReturn_StDev, df_CAGR_StDev, df_AvgReturn_MaxDD, df_MedianReturn_MaxDD, df_CAGR_MaxDD, df_TreynorRatio, df_TreynorRatio_Annualized, df_SharpeRatio, df_SharpeRatio_Annualized, df_SortinoRatio, df_SortinoRatio_Annualized, df_CalmarRatio, df_CalmarRatio_Annualized, df_Gaussian_VaR, df_CornishFisher_VaR, df_Total_NumOfPeriods, df_Winning_AvgReturn, df_Winning_MedianReturn, df_Winning_MaxReturn, df_Winning_MinReturn, df_Winning_StDev, df_Winning_Variance, df_Winning_NumOfPeriods, df_WinningPerc, df_Losing_AvgReturn, df_Losing_MedianReturn, df_Losing_MaxReturn, df_Losing_MinReturn, df_Losing_StDev, df_Losing_Variance, df_Losing_NumOfPeriods, df_LosingPerc, df_Win_Loss_Ratio, df_Expectancy, df_ExepectancyRatio, df_Sum_of_Returns, df_Sum_of_Losses, df_Gain_to_Pain_Ratio, df_Sharpe_Ratio_Skew

    def metrics_transposed(self):
        df_AvgReturn, df_MedianReturn, df_MaxReturn, df_MinReturn, df_StDev, df_Variance, df_Beta, df_DownsideDev, df_Skew, df_Kurtosis, df_Kurt_Skew, df_ExcessKurtosis, df_ExcessKurtosis_Skew, df_CompoundedReturn, df_CAGR, df_MaxDD, df_MarkowitzReturnFunction, df_MarkowitzReturnFunction_CAGR, df_AvgReturn_StDev, df_MedianReturn_StDev, df_CAGR_StDev, df_AvgReturn_MaxDD, df_MedianReturn_MaxDD, df_CAGR_MaxDD, df_TreynorRatio, df_TreynorRatio_Annualized, df_SharpeRatio, df_SharpeRatio_Annualized, df_SortinoRatio, df_SortinoRatio_Annualized, df_CalmarRatio, df_CalmarRatio_Annualized, df_Gaussian_VaR, df_CornishFisher_VaR, df_Total_NumOfPeriods, df_Winning_AvgReturn, df_Winning_MedianReturn, df_Winning_MaxReturn, df_Winning_MinReturn, df_Winning_StDev, df_Winning_Variance, df_Winning_NumOfPeriods, df_WinningPerc, df_Losing_AvgReturn, df_Losing_MedianReturn, df_Losing_MaxReturn, df_Losing_MinReturn, df_Losing_StDev, df_Losing_Variance, df_Losing_NumOfPeriods, df_LosingPerc, df_Win_Loss_Ratio, df_Expectancy, df_ExepectancyRatio, df_Sum_of_Returns, df_Sum_of_Losses, df_Gain_to_Pain_Ratio, df_Sharpe_Ratio_Skew = self.metrics_dataframes()

        t_AvgReturn = df_AvgReturn.T
        t_MedianReturn = df_MedianReturn.T
        t_MaxReturn = df_MaxReturn.T
        t_MinReturn = df_MinReturn.T
        t_StDev = df_StDev.T
        t_Variance = df_Variance.T
        t_Beta = df_Beta.T
        t_DownsideDev = df_DownsideDev.T
        t_Skew = df_Skew.T
        t_Kurtosis = df_Kurtosis.T
        t_Kurt_Skew = df_Kurt_Skew.T
        t_ExcessKurtosis = df_ExcessKurtosis.T
        t_ExcessKurtosis_Skew = df_ExcessKurtosis_Skew.T
        t_CompoundedReturn = df_CompoundedReturn.T
        t_CAGR = df_CAGR.T
        t_MaxDD = df_MaxDD.T
        t_MarkowitzReturnFunction = df_MarkowitzReturnFunction.T
        t_MarkowitzReturnFunction_CAGR = df_MarkowitzReturnFunction_CAGR.T
        t_AvgReturn_StDev = df_AvgReturn_StDev.T
        t_MedianReturn_StDev = df_MedianReturn_StDev.T
        t_CAGR_StDev = df_CAGR_StDev.T
        t_AvgReturn_MaxDD = df_AvgReturn_MaxDD.T
        t_MedianReturn_MaxDD = df_MedianReturn_MaxDD.T
        t_CAGR_MaxDD = df_CAGR_MaxDD.T
        t_TreynorRatio = df_TreynorRatio.T
        t_TreynorRatio_Annualized = df_TreynorRatio_Annualized.T
        t_SharpeRatio = df_SharpeRatio.T
        t_SharpeRatio_Annualized = df_SharpeRatio_Annualized.T
        t_SortinoRatio = df_SortinoRatio.T
        t_SortinoRatio_Annualized = df_SortinoRatio_Annualized.T
        t_CalmarRatio = df_CalmarRatio.T
        t_CalmarRatio_Annualized = df_CalmarRatio_Annualized.T
        t_Gaussian_VaR = df_Gaussian_VaR.T
        t_CornishFisher_VaR = df_CornishFisher_VaR.T
        t_Total_NumOfPeriods = df_Total_NumOfPeriods.T
        t_Winning_AvgReturn = df_Winning_AvgReturn.T
        t_Winning_MedianReturn = df_Winning_MedianReturn.T
        t_Winning_MaxReturn = df_Winning_MaxReturn.T
        t_Winning_MinReturn = df_Winning_MinReturn.T
        t_Winning_StDev = df_Winning_StDev.T
        t_Winning_Variance = df_Winning_Variance.T
        t_Winning_NumOfPeriods = df_Winning_NumOfPeriods.T
        t_WinningPerc = df_WinningPerc.T
        t_Losing_AvgReturn = df_Losing_AvgReturn.T
        t_Losing_MedianReturn = df_Losing_MedianReturn.T
        t_Losing_MaxReturn = df_Losing_MaxReturn.T
        t_Losing_MinReturn = df_Losing_MinReturn.T
        t_Losing_StDev = df_Losing_StDev.T
        t_Losing_Variance = df_Losing_Variance.T
        t_Losing_NumOfPeriods = df_Losing_NumOfPeriods.T
        t_LosingPerc = df_LosingPerc.T
        t_Win_Loss_Ratio = df_Win_Loss_Ratio.T
        t_Expectancy = df_Expectancy.T
        t_ExepectancyRatio = df_ExepectancyRatio.T
        t_Sum_of_Returns = df_Sum_of_Returns.T
        t_Sum_of_Losses = df_Sum_of_Losses.T
        t_Gain_to_Pain_Ratio = df_Gain_to_Pain_Ratio.T
        t_Sharpe_Ratio_Skew = df_Sharpe_Ratio_Skew

        return t_AvgReturn, t_MedianReturn, t_MaxReturn, t_MinReturn, t_StDev, t_Variance, t_Beta, t_DownsideDev, t_Skew, t_Kurtosis, t_Kurt_Skew, t_ExcessKurtosis, t_ExcessKurtosis_Skew, t_CompoundedReturn, t_CAGR, t_MaxDD, t_MarkowitzReturnFunction, t_MarkowitzReturnFunction_CAGR, t_AvgReturn_StDev, t_MedianReturn_StDev, t_CAGR_StDev, t_AvgReturn_MaxDD, t_MedianReturn_MaxDD, t_CAGR_MaxDD, t_TreynorRatio, t_TreynorRatio_Annualized, t_SharpeRatio, t_SharpeRatio_Annualized, t_SortinoRatio, t_SortinoRatio_Annualized, t_CalmarRatio, t_CalmarRatio_Annualized, t_Gaussian_VaR, t_CornishFisher_VaR, t_Total_NumOfPeriods, t_Winning_AvgReturn, t_Winning_MedianReturn, t_Winning_MaxReturn, t_Winning_MinReturn, t_Winning_StDev, t_Winning_Variance, t_Winning_NumOfPeriods, t_WinningPerc, t_Losing_AvgReturn, t_Losing_MedianReturn, t_Losing_MaxReturn, t_Losing_MinReturn, t_Losing_StDev, t_Losing_Variance, t_Losing_NumOfPeriods, t_LosingPerc, t_Win_Loss_Ratio, t_Expectancy, t_ExepectancyRatio, t_Sum_of_Returns, t_Sum_of_Losses, t_Gain_to_Pain_Ratio, t_Sharpe_Ratio_Skew

    def ranking_model(self):
        
# df_MedianReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MedianReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MaxReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MaxReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MinReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MinReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_StDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_StDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Variance[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Variance[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Beta[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Beta[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_DownsideDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_DownsideDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Skew[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Skew[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Kurtosis[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Kurtosis[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Kurt_Skew[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Kurt_Skew[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_ExcessKurtosis[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_ExcessKurtosis[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_ExcessKurtosis_Skew[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_ExcessKurtosis_Skew[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CompoundedReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CompoundedReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CAGR[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CAGR[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MaxDD[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MaxDD[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MarkowitzReturnFunction[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MarkowitzReturnFunction[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MarkowitzReturnFunction_CAGR[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MarkowitzReturnFunction_CAGR[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_AvgReturn_StDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_AvgReturn_StDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MedianReturn_StDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MedianReturn_StDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CAGR_StDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CAGR_StDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_AvgReturn_MaxDD[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_AvgReturn_MaxDD[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_MedianReturn_MaxDD[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_MedianReturn_MaxDD[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CAGR_MaxDD[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CAGR_MaxDD[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_TreynorRatio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_TreynorRatio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_TreynorRatio_Annualized[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_TreynorRatio_Annualized[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_SharpeRatio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_SharpeRatio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_SharpeRatio_Annualized[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_SharpeRatio_Annualized[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_SortinoRatio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_SortinoRatio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_SortinoRatio_Annualized[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_SortinoRatio_Annualized[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CalmarRatio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CalmarRatio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CalmarRatio_Annualized[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CalmarRatio_Annualized[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Gaussian_VaR[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Gaussian_VaR[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_CornishFisher_VaR[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_CornishFisher_VaR[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Total_NumOfPeriods[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Total_NumOfPeriods[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_AvgReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_AvgReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_MedianReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_MedianReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_MaxReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_MaxReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_MinReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_MinReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_StDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_StDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_Variance[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_Variance[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Winning_NumOfPeriods[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Winning_NumOfPeriods[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_WinningPerc[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_WinningPerc[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_AvgReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_AvgReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_MedianReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_MedianReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_MaxReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_MaxReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_MinReturn[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_MinReturn[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_StDev[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_StDev[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_Variance[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_Variance[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Losing_NumOfPeriods[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Losing_NumOfPeriods[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_LosingPerc[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_LosingPerc[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Win_Loss_Ratio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Win_Loss_Ratio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Expectancy[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Expectancy[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_ExepectancyRatio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_ExepectancyRatio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Sum_of_Returns[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Sum_of_Returns[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Sum_of_Losses[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Sum_of_Losses[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Gain_to_Pain_Ratio[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Gain_to_Pain_Ratio[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')
# df_Sharpe_Ratio_Skew[f'Rank-{feature}-{fund_name}'] = pd.qcut(df_Sharpe_Ratio_Skew[f'{feature}-{fund_name}'], q=deciles, labels=False, duplicates='drop')













        # for fund_stat in fund_stats:
        #     features = fund_stat.columns[1:]
        #     fund_name = fund_stat.columns[0]
        #     dates = fund_stat[fund_name].index
        #     for date in dates:

        #         print(date)
        
        print(df_AvgReturn)
        print('-------')
        transposed = df_AvgReturn.T
        print(transposed)
        print('-------')
        # df_AvgReturn.to_csv(f"rank1.csv")

    #     df_AvgReturn[f'RankLabel-{i}'] = pd.qcut(df_AvgReturn[f'{i}'], q=q_quartiles, labels=label_quartiles, duplicates='drop')
    #     df_AvgReturn[f'Rank-{i}'] = pd.qcut(df_AvgReturn[f'{i}'], q=q_quartiles, labels=False, duplicates='drop')
    #     df_AvgReturn[f'RankN-{i}'] = pd.qcut(df_AvgReturn[f'{i}'], q=q_quartiles, duplicates='drop')


        # print('-------')
        # df_AvgReturn.to_csv(f"rank2.csv")
        # print('-------')
        # print(df_AvgReturn)
        # print('-------')
        # print(df_MedianReturn)
        # print('-------')
        # print(df_MaxReturn)
        # print('-------')
        # print(df_MinReturn)
        # print('-------')
        # print(df_StDev)
        # print('-------')
        # print(df_Variance)
        # print('-------')
        # print(df_Beta)
        # print('-------')
        # print(df_DownsideDev)
        # print('-------')
        # print(df_Skew)
        # print('-------')
        # print(df_Kurtosis)
        # print('-------')
        # print(df_Kurt_Skew)
        # print('-------')
        # print(df_ExcessKurtosis)
        # print('-------')
        # print(df_ExcessKurtosis_Skew)
        # print('-------')
        # print(df_CompoundedReturn)
        # print('-------')
        # print(df_CAGR)
        # print('-------')
        # print(df_MaxDD)
        # print('-------')
        # print(df_MarkowitzReturnFunction)
        # print('-------')
        # print(df_MarkowitzReturnFunction_CAGR)
        # print('-------')
        # print(df_AvgReturn_StDev)
        # print('-------')
        # print(df_MedianReturn_StDev)
        # print('-------')
        # print(df_CAGR_StDev)
        # print('-------')
        # print(df_AvgReturn_MaxDD)
        # print('-------')
        # print(df_MedianReturn_MaxDD)
        # print('-------')
        # print(df_CAGR_MaxDD)
        # print('-------')
        # print(df_TreynorRatio)
        # print('-------')
        # print(df_TreynorRatio_Annualized)
        # print('-------')
        # print(df_SharpeRatio)
        # print('-------')
        # print(df_SharpeRatio_Annualized)
        # print('-------')
        # print(df_SortinoRatio)
        # print('-------')
        # print(df_SortinoRatio_Annualized)
        # print('-------')
        # print(df_CalmarRatio)
        # print('-------')
        # print(df_CalmarRatio_Annualized)
        # print('-------')
        # print(df_Gaussian_VaR)
        # print('-------')
        # print(df_CornishFisher_VaR)
        # print('-------')
        # print(df_Total_NumOfPeriods)
        # print('-------')
        # print(df_Winning_AvgReturn)
        # print('-------')
        # print(df_Winning_MedianReturn)
        # print('-------')
        # print(df_Winning_MaxReturn)
        # print('-------')
        # print(df_Winning_MinReturn)
        # print('-------')
        # print(df_Winning_StDev)
        # print('-------')
        # print(df_Winning_Variance)
        # print('-------')
        # print(df_Winning_NumOfPeriods)
        # print('-------')
        # print(df_WinningPerc)
        # print('-------')
        # print(df_Losing_AvgReturn)
        # print('-------')
        # print(df_Losing_MedianReturn)
        # print('-------')
        # print(df_Losing_MaxReturn)
        # print('-------')
        # print(df_Losing_MinReturn)
        # print('-------')
        # print(df_Losing_StDev)
        # print('-------')
        # print(df_Losing_Variance)
        # print('-------')
        # print(df_Losing_NumOfPeriods)
        # print('-------')
        # print(df_LosingPerc)
        # print('-------')
        # print(df_Win_Loss_Ratio)
        # print('-------')
        # print(df_Expectancy)
        # print('-------')
        # print(df_ExepectancyRatio)
        # print('-------')
        # print(df_Sum_of_Returns)
        # print('-------')
        # print(df_Sum_of_Losses)
        # print('-------')
        # print(df_Gain_to_Pain_Ratio)
        # print('-------')
        # print(df_Sharpe_Ratio_Skew)