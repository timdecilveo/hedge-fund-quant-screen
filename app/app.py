from monthlyStatistics import MonthlyStatistics
from rankingModel import RankingModel

############################################################################
# files = MonthlyStatistics().files()
# print(files)
############################################################################
# fund_statistics, benchmark_statistics = MonthlyStatistics().statistics()
# print(fund_statistics)
# print(benchmark_statistics)
############################################################################
# df_all_stats, df_ranking = RankingModel().ranking_model()
# print(df_all_stats)
# print(df_ranking)
############################################################################
d = '2019-02-28'
df_ranking = RankingModel().ranking_as_of()
# df_ranking = RankingModel().ranking_as_of(date=d)
print(df_ranking)
############################################################################