from monthlyStatistics import MonthlyStatistics
from rankingModel import RankingModel

############################################################################
# fund_statistics, benchmark_statistics = MonthlyStatistics().statistics()
# print(fund_statistics)
# print(benchmark_statistics)
############################################################################
df_AvgReturn, df_MedianReturn, df_MaxReturn, df_MinReturn, df_StDev, df_Variance, df_Beta, df_DownsideDev, df_Skew, df_Kurtosis, df_Kurt_Skew, df_ExcessKurtosis, df_ExcessKurtosis_Skew, df_CompoundedReturn, df_CAGR, df_MaxDD, df_MarkowitzReturnFunction, df_MarkowitzReturnFunction_CAGR, df_AvgReturn_StDev, df_MedianReturn_StDev, df_CAGR_StDev, df_AvgReturn_MaxDD, df_MedianReturn_MaxDD, df_CAGR_MaxDD, df_TreynorRatio, df_TreynorRatio_Annualized, df_SharpeRatio, df_SharpeRatio_Annualized, df_SortinoRatio, df_SortinoRatio_Annualized, df_CalmarRatio, df_CalmarRatio_Annualized, df_Gaussian_VaR, df_CornishFisher_VaR, df_Total_NumOfPeriods, df_Winning_AvgReturn, df_Winning_MedianReturn, df_Winning_MaxReturn, df_Winning_MinReturn, df_Winning_StDev, df_Winning_Variance, df_Winning_NumOfPeriods, df_WinningPerc, df_Losing_AvgReturn, df_Losing_MedianReturn, df_Losing_MaxReturn, df_Losing_MinReturn, df_Losing_StDev, df_Losing_Variance, df_Losing_NumOfPeriods, df_LosingPerc, df_Win_Loss_Ratio, df_Expectancy, df_ExepectancyRatio, df_Sum_of_Returns, df_Sum_of_Losses, df_Gain_to_Pain_Ratio, df_Sharpe_Ratio_Skew = RankingModel().metrics_dataframes()
# RankingModel().ranking_model()
print(df_AvgReturn)
deciles = 10
# scoring = RankingModel().scoring(q=deciles)
# print(scoring)
RankingModel().scoring(q=deciles)