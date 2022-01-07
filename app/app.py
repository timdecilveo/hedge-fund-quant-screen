from monthlyStatistics import MonthlyStatistics
from rankingModel import RankingModel

############################################################################
# files = MonthlyStatistics().files()

############################################################################
fund_statistics, benchmark_statistics = MonthlyStatistics().statistics()
# print(fund_statistics)
# print(benchmark_statistics)
############################################################################

print(RankingModel().ranking_model())