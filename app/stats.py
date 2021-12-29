import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

class Stats:
    def __init__(self, df, beginning_date, ending_date):
        self.df = df
        self.cols = df.columns
        self.dates = df.index
        self.beginning_date = dt.datetime.strptime(beginning_date, '%Y-%m-%d')
        self.ending_date = dt.datetime.strptime(ending_date, '%Y-%m-%d')

    def average_return(self):
        average_return = self.df[self.cols].mean()
        avg_return = self.df[self.cols]
        return average_return

    def compounded_annual_growth_rate(self):
        compounded_return = (self.df[self.cols] + 1).cumprod()
        time_delta = (self.ending_date - self.beginning_date).days
        years = time_delta / 365
        cagr = ((compounded_return) ** (1 / years)) - 1

        return cagr
    