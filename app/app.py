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
# df_all_stats, df_ranking_sum = RankingModel().ranking_model()
# print(df_all_stats)
# print(df_ranking_sum)
############################################################################
d = '2019-02-28'
# df_ranking = RankingModel().ranking_as_of(date=d)
df_ranking = RankingModel().ranking_as_of()
print(df_ranking)
