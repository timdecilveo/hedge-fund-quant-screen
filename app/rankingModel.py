import numpy as np
import pandas as pd
from datetime import datetime
from monthlyStatistics import MonthlyStatistics

class RankingModel:
    def __init__(self):
        self.monthlyStats = MonthlyStatistics()
    
    def metrics_dataframes(self):
        fund_stats, benchmark_stats = self.monthlyStats.statistics()

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
                if feature == 'Kurt_times_Skew':
                    df_Kurt_Skew[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExcessKurtosis':
                    df_ExcessKurtosis[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExcessKurtosis_times_Skew':
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

    def percentile_dataframes(self, q):
        metrics_dataframes = RankingModel().metrics_dataframes()
        db = []
        
        for metrics_df in metrics_dataframes:
            features = metrics_df.columns
            features[0]
            percentiles = metrics_df.apply(lambda rank: pd.qcut(rank, q=q, labels=False, duplicates='drop'), axis=1).add_prefix('Rank_')
            db.append(percentiles)
        return db

    def scoring(self, q):
        '''
        For Deciles:
            - 0 is the lowest quantile, meaning the lower numbers
            - 9 is the highest quantile, meaning the higher numbers
            9 will be scored as 9 if a higher decile is desired
            9 will be scored as -9 if a lower decile is desired
        '''
        percentile_dataframes = self.percentile_dataframes(q=q)

        for percentile_df in percentile_dataframes:
            '''
            AvgReturn: (+) higher decile is desired
            '''

            '''            
            MedianReturn: (+) higher decile is desired
            '''

            '''
            MaxReturn: (+) higher decile is desired
            '''

            '''
            MinReturn: (+) higher decile is desired
            '''

            '''
            StDev: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Variance: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Beta: (-) lower decile is desired
            '''

            '''
            DownsideDev
            '''

            '''
            Skew: (+) higher decile is desired
            '''

            '''
            Kurtosis: (+) higher decile is desired
            '''

            '''
            Kurt_Skew: (+) higher decile is desired
            '''

            '''
            ExcessKurtosis: (+) higher decile is desired
            '''

            '''
            ExcessKurtosis_Skew: (+) higher decile is desired
            '''

            '''
            CompoundedReturn: (+) higher decile is desired
            '''

            '''
            CAGR: (+) higher decile is desired
            '''

            '''
            MaxDD: (-) lower decile is desired
            '''

            '''
            MarkowitzReturnFunction: (+) higher decile is desired
            '''

            '''
            MarkowitzReturnFunction_CAGR: (+) higher decile is desired
            '''

            '''
            AvgReturn_StDev: (+) higher decile is desired
            '''

            '''
            MedianReturn_StDev: (+) higher decile is desired
            '''

            '''
            CAGR_StDev: (+) higher decile is desired
            '''

            '''
            AvgReturn_MaxDD: (+) higher decile is desired
            '''

            '''
            MedianReturn_MaxDD: (+) higher decile is desired
            '''

            '''
            CAGR_MaxDD: (+) higher decile is desired
            '''

            '''
            TreynorRatio: (+) higher decile is desired
            '''

            '''
            TreynorRatio_Annualized: (+) higher decile is desired
            '''

            '''
            SharpeRatio: (+) higher decile is desired
            '''

            '''
            SharpeRatio_Annualized: (+) higher decile is desired
            '''

            '''
            SortinoRatio: (+) higher decile is desired
            '''

            '''
            SortinoRatio_Annualized: (+) higher decile is desired
            '''

            '''
            CalmarRatio: (+) higher decile is desired
            '''

            '''
            CalmarRatio_Annualized: (+) higher decile is desired
            '''

            '''
            Gaussian_VaR
            '''

            '''
            CornishFisher_VaR
            '''

            '''
            Total_NumOfPeriods: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Winning_AvgReturn: (+) higher decile is desired
            '''

            '''
            Winning_MedianReturn: (+) higher decile is desired
            '''

            '''
            Winning_MaxReturn: (+) higher decile is desired
            '''

            '''
            Winning_MinReturn: (+) higher decile is desired
            '''

            '''
            Winning_StDev: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Winning_Variance: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Winning_NumOfPeriods: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            WinningPerc: (+) higher decile is desired
            '''

            '''
            Losing_AvgReturn: (+) higher decile is desired
            '''

            '''
            Losing_MedianReturn: (+) higher decile is desired
            '''

            '''
            Losing_MaxReturn: (+) higher decile is desired
            '''

            '''
            Losing_MinReturn: (+) higher decile is desired
            '''

            '''
            Losing_StDev: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Losing_Variance: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            Losing_NumOfPeriods: (N/A) in previous model, ranking wasn't calculated
            '''

            '''
            LosingPerc: (-) lower decile is desired
            '''

            '''
            Win_Loss_Ratio: (+) higher decile is desired
            '''

            '''
            Expectancy: (+) higher decile is desired
            '''

            '''
            ExepectancyRatio: (+) higher decile is desired
            '''

            '''
            Sum_of_Returns: (+) higher decile is desired
            '''

            '''
            Sum_of_Losses: (-) lower decile is desired
            '''

            '''
            Gain_to_Pain_Ratio: (+) higher decile is desired
            '''

            '''
            Sharpe_Ratio_Skew
            '''
            print(percentile_df)

