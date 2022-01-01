import numpy as np
import pandas as pd
from monthlyStatistics import MonthlyStatistics

class RankingModel:
    def __init__(self):
        self.monthlyStats = MonthlyStatistics()
    
    def ranking_model(self):
        fund_stats, benchmark_stats = self.monthlyStats.statistics()

        for fund_stat in fund_stats:
            print(fund_stat)
            print('----')


