import numpy as np
import pandas as pd
import re
from functools import reduce
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
        df_KurtSkew = pd.DataFrame()
        df_ExcessKurtosis = pd.DataFrame()
        df_ExcessKurtosisSkew = pd.DataFrame()
        df_CompoundedReturn = pd.DataFrame()
        df_CAGR = pd.DataFrame()
        df_MaxDD = pd.DataFrame()
        df_MarkowitzReturnFunction = pd.DataFrame()
        df_MarkowitzReturnFunctionCAGR = pd.DataFrame()
        df_AvgReturnStDev = pd.DataFrame()
        df_MedianReturnStDev = pd.DataFrame()
        df_CAGRStDev = pd.DataFrame()
        df_AvgReturnMaxDD = pd.DataFrame()
        df_MedianReturnMaxDD = pd.DataFrame()
        df_CAGRMaxDD = pd.DataFrame()
        df_TreynorRatio = pd.DataFrame()
        df_TreynorRatioAnnualized = pd.DataFrame()
        df_SharpeRatio = pd.DataFrame()
        df_SharpeRatioAnnualized = pd.DataFrame()
        df_SortinoRatio = pd.DataFrame()
        df_SortinoRatioAnnualized = pd.DataFrame()
        df_CalmarRatio = pd.DataFrame()
        df_CalmarRatioAnnualized = pd.DataFrame()
        df_GaussianVaR = pd.DataFrame()
        df_CornishFisherVaR = pd.DataFrame()
        df_TotalNumOfPeriods = pd.DataFrame()
        df_WinningAvgReturn = pd.DataFrame()
        df_WinningMedianReturn = pd.DataFrame()
        df_WinningMaxReturn = pd.DataFrame()
        df_WinningMinReturn = pd.DataFrame()
        df_WinningStDev = pd.DataFrame()
        df_WinningVariance = pd.DataFrame()
        df_WinningNumOfPeriods = pd.DataFrame()
        df_WinningPerc = pd.DataFrame()
        df_LosingAvgReturn = pd.DataFrame()
        df_LosingMedianReturn = pd.DataFrame()
        df_LosingMaxReturn = pd.DataFrame()
        df_LosingMinReturn = pd.DataFrame()
        df_LosingStDev = pd.DataFrame()
        df_LosingVariance = pd.DataFrame()
        df_LosingNumOfPeriods = pd.DataFrame()
        df_LosingPerc = pd.DataFrame()
        df_WinLossRatio = pd.DataFrame()
        df_Expectancy = pd.DataFrame()
        df_ExepectancyRatio = pd.DataFrame()
        df_SumOfReturns = pd.DataFrame()
        df_SumOfLosses = pd.DataFrame()
        df_GainToPainRatio = pd.DataFrame()
        df_SharpeRatioSkew = pd.DataFrame()

        for fund_stat in fund_stats:
            features = fund_stat.columns[1:]
            fund_name = fund_stat.columns[0]

            for feature in features:
                if feature == 'AvgReturn':
                    df_AvgReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MedianReturn':
                    df_MedianReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MaxReturn':
                    df_MaxReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MinReturn':
                    df_MinReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'StDev':
                #     df_StDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'Variance':
                #     df_Variance[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Beta':
                    df_Beta[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'DownsideDev':
                    df_DownsideDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Skew':
                    df_Skew[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Kurtosis':
                    df_Kurtosis[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'KurtTimesSkew':
                    df_KurtSkew[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExcessKurtosis':
                    df_ExcessKurtosis[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExcessKurtosisTimesSkew':
                    df_ExcessKurtosisSkew[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CompoundedReturn':
                    df_CompoundedReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CAGR':
                    df_CAGR[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MaxDD':
                    df_MaxDD[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MarkowitzReturnFunction':
                    df_MarkowitzReturnFunction[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MarkowitzReturnFunctionCAGR':
                    df_MarkowitzReturnFunctionCAGR[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'AvgReturnStDev':
                    df_AvgReturnStDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MedianReturnStDev':
                    df_MedianReturnStDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CAGRStDev':
                    df_CAGRStDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'AvgReturnMaxDD':
                    df_AvgReturnMaxDD[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'MedianReturnMaxDD':
                    df_MedianReturnMaxDD[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CAGRMaxDD':
                    df_CAGRMaxDD[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'TreynorRatio':
                    df_TreynorRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'TreynorRatioAnnualized':
                    df_TreynorRatioAnnualized[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SharpeRatio':
                    df_SharpeRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SharpeRatioAnnualized':
                    df_SharpeRatioAnnualized[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SortinoRatio':
                    df_SortinoRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SortinoRatioAnnualized':
                    df_SortinoRatioAnnualized[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CalmarRatio':
                    df_CalmarRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CalmarRatioAnnualized':
                    df_CalmarRatioAnnualized[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'GaussianVaR':
                    df_GaussianVaR[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'CornishFisherVaR':
                    df_CornishFisherVaR[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'Total_NumOfPeriods':
                #     df_Total_NumOfPeriods[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinningAvgReturn':
                    df_WinningAvgReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinningMedianReturn':
                    df_WinningMedianReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinningMaxReturn':
                    df_WinningMaxReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinningMinReturn':
                    df_WinningMinReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'Winning_StDev':
                #     df_Winning_StDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'Winning_Variance':
                #     df_Winning_Variance[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'Winning_NumOfPeriods':
                #     df_Winning_NumOfPeriods[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinningPerc':
                    df_WinningPerc[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'LosingAvgReturn':
                    df_LosingAvgReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'LosingMedianReturn':
                    df_LosingMedianReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'LosingMaxReturn':
                    df_LosingMaxReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'LosingMinReturn':
                    df_LosingMinReturn[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'LosingStDev':
                #     df_LosingStDev[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'LosingVariance':
                #     df_LosingVariance[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                # if feature == 'LosingNumOfPeriods':
                #     df_LosingNumOfPeriods[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'LosingPerc':
                    df_LosingPerc[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'WinLossRatio':
                    df_WinLossRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'Expectancy':
                    df_Expectancy[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'ExepectancyRatio':
                    df_ExepectancyRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SumOfReturns':
                    df_SumOfReturns[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SumOfLosses':
                    df_SumOfLosses[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'GainToPainRatio':
                    df_GainToPainRatio[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
                if feature == 'SharpeRatioSkew':
                    df_SharpeRatioSkew[f'{feature}#{fund_name}'] = fund_stat[f'{feature}']
        
        return df_AvgReturn, df_MedianReturn, df_MaxReturn, df_MinReturn, df_Beta, df_DownsideDev, df_Skew, df_Kurtosis, df_KurtSkew, df_ExcessKurtosis, df_ExcessKurtosisSkew, df_CompoundedReturn, df_CAGR, df_MaxDD, df_MarkowitzReturnFunction, df_MarkowitzReturnFunctionCAGR, df_AvgReturnStDev, df_MedianReturnStDev, df_CAGRStDev, df_AvgReturnMaxDD, df_MedianReturnMaxDD, df_CAGRMaxDD, df_TreynorRatio, df_TreynorRatioAnnualized, df_SharpeRatio, df_SharpeRatioAnnualized, df_SortinoRatio, df_SortinoRatioAnnualized, df_CalmarRatio, df_CalmarRatioAnnualized, df_GaussianVaR, df_CornishFisherVaR, df_WinningAvgReturn, df_WinningMedianReturn, df_WinningMaxReturn, df_WinningMinReturn, df_WinningPerc, df_LosingAvgReturn, df_LosingMedianReturn, df_LosingMaxReturn, df_LosingMinReturn, df_LosingPerc, df_WinLossRatio, df_Expectancy, df_ExepectancyRatio, df_SumOfReturns, df_SumOfLosses, df_GainToPainRatio, df_SharpeRatioSkew

    def percentile_dataframes(self, q=10):
        metrics_dataframes = RankingModel().metrics_dataframes()
        percentile_dataframes = []
        
        for metrics_df in metrics_dataframes:
            percentiles = metrics_df.apply(lambda rank: pd.qcut(rank, q=q, labels=False, duplicates='drop'), axis=1).add_prefix('Rank^')
            percentile_dataframes.append(percentiles)
        return percentile_dataframes

    def percentiles(self, q=10):
        '''
        For Deciles:
            - 0 is the lowest quantile, meaning the lower numbers
            - 9 is the highest quantile, meaning the higher numbers

            9 will be scored as 9 if a higher decile is desired
            9 will be scored as -9 if a lower decile is desired
        '''
        percentile_dataframes = self.percentile_dataframes(q=q)
        percentiles = []

        for percentile_df in percentile_dataframes:
            cols = percentile_df.columns
            for col in cols:
                stat = re.split('\^|#', col)[1]
                if stat == 'Beta' or stat == 'MaxDD' or stat == 'LosingPerc' or stat == 'SumOfLosses':
                    percentile_df = -percentile_df
            percentiles.append(percentile_df)
        return percentiles

    def ranking_model(self):
        percentiles = self.percentiles()

        # percentiles.to_csv("percentiles.csv")
        files = MonthlyStatistics().files()
        df_ranking = pd.DataFrame()
        dict_test = {}
        rank = []
        objs = [
            'dunn-capital-management--wma-program',
            'eckhardt-trading-company--evolution-strategy',
            'mak-capital--one-fund',
            'tim--trend-2',
            'winton-capital--futures-program',
        ]

        for percentile in percentiles:
            cols = percentile.columns
            for col in cols:
                strategy_names = re.split('\^|#', col)[2]
                df_ranking[f'{col}'] = percentile[col]
                # df_ranking[f'sum-{strategy_names}'] = df_ranking.groupby(f'{strategy_names}').sum()
        
        for (col, file) in zip(df_ranking.columns, files):
            strategy_names = re.split('\^|#', col)[2]
            # print(f'col: {col} -> strategy_names: {strategy_names}')
            # df_ranking[f'sum-{strategy_names}'] = df_ranking.groupby([f'{strategy_names}']).sum()
            df_ranking = df_ranking.groupby(by=f'{strategy_names}', axis=1).sum()
        print(df_ranking)
        print('-----')
        # print(df_ranking[''])
        # print('-----')



        # #####################################################
        # print(df_ranking)
        # print(df_ranking.columns)

            # for (col, file) in zip(cols, files):
                # strategy_names = re.split('\^|#', col)[2]
                # if strategy_names == file:
                # if strategy_names == objs[0]:
                #     df_ranking[f'{col}'] = percentile[col]
                # if strategy_names == objs[1]:
                #     df_ranking[f'{col}'] = percentile[col]
                # if strategy_names == objs[2]:
                #     df_ranking[f'{col}'] = percentile[col]
                # if strategy_names == objs[3]:
                    # df_ranking[f'{col}'] = percentile[col]
                # if strategy_names == objs[4]:
                #     df_ranking[f'{col}'] = percentile[col]

        # df_ranking['sum'] = df_ranking.sum(axis=1)
        # strategy_names = re.split('\^|#', col)[2]
        # test = sum(i for i in percentile[col] if strategy_names == objs[4])
        # df_ranking[f'sum-{strategy_names}'] = test

        # ranking_df.to_csv("ranking_df.csv")
