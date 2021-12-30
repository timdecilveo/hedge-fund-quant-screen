import os
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from directories import Directory

class Stats:
    def __init__(self):
        self.directory = os.listdir(f"../data-files")
        self.file_list = Directory(self.directory).files()

    def average_return(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            average_return_ = i[file_name].expanding().mean()
            i['AvgReturn'] = average_return_
            db.append(i)
        return db

    def median_return(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            median_reutrn_ = i[file_name].expanding().median()
            i['MedianReturn'] = median_reutrn_
            db.append(i)
        return db

    def nmaximum_return(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            maximum_return_ = i[file_name].expanding().max()
            i['MaxReturn'] = maximum_return_
            db.append(i)
        return db

    def minimum_return(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            minimum_return_ = i[file_name].expanding().min()
            i['MinReturn'] = minimum_return_
            db.append(i)
        return db

    def standard_devation(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            standard_deviation_ = i[file_name].expanding().std()
            i['StDev'] = standard_deviation_
            db.append(i)
        return db
    
    def cagr(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            dates = i[file_name].index
            start_date = dates[0]
            end_date = dates[-1] #need to fix this so it's the rolling date
            time_delta_days = (end_date - start_date).days
            years = time_delta_days / 365

            compounded_return = (i[file_name] + 1).cumprod()
            cagr = ((compounded_return) ** (1 / years)) - 1
            i['CompoundedReturn'] = compounded_return
            i['CAGR'] = cagr
            db.append(i)
        return db

    def max_drawdown(self):
        db = []
        for i in self.file_list:
            file_name = i.columns[0]
            compounded_return = (i[file_name] + 1).cumprod()
            peak = compounded_return.expanding(min_periods=1).max()
            drawdown = (compounded_return / peak) - 1
            max_drawdown = drawdown.min()
            i['MaxDrawdown'] = max_drawdown
            db.append(i)
        return db
    
    # def st_dev_denominator(self):

