import numpy as np
import pandas as pd
from monthlyStatistics import MonthlyStatistics

class RankingModel:
    def __init__(self):
        self.monthlyStats = MonthlyStatistics()
    
    def ranking_model(self):
        fund_stats, benchmark_stats = self.monthlyStats.statistics()
        deciles = 10
        quartiles = 4

        df_MonthlyReturn = pd.DataFrame()
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

        for fund_stat in fund_stats:
            features = fund_stat.columns[1:]
            fund_name = fund_stat.columns[0]

            for feature in features:
                if feature == 'MonthlyReturn':
                    df_MonthlyReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
                    # df_MonthlyReturn['Rank'] = pd.qcut(fund_stat

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
            
        # df_MonthlyReturn = pd.DataFrame()
        #         if feature == 'MonthlyReturn':
        #             df_MonthlyReturn[f'{feature}-{fund_name}'] = fund_stat[f'{feature}']
        

        # df_MonthlyReturn = df_MonthlyReturn.T
        print(df_MonthlyReturn)
        print('-------')
        df_MonthlyReturn['test'] = pd.qcut(df_MonthlyReturn['MonthlyReturn-dunn-capital-management--wma-program'], 10, labels = False)
        print(df_MonthlyReturn)
        print('-------')
        # for column in df_MonthlyReturn.columns:
        #     df_MonthlyReturn[f'DecileRank-{column}'] = pd.qcut(df_MonthlyReturn[f'{column}'], q=deciles, labels=False, duplicates='drop')
        # print(df_MonthlyReturn)
        # print(df_MonthlyReturn.columns)
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