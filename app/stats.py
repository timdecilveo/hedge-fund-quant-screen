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
            i['MedReturn'] = median_reutrn_
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
            i['MaxDD'] = max_drawdown
            db.append(i)
        return db
    
    def average_return_over_st_dev(self):
        db = []
        st_devs = self.standard_devation()
        avg_returns = self.average_return()
        for (avg_return, st_dev) in zip(avg_returns, st_devs):
            avg_ret = avg_return['AvgReturn']
            st_dev_ = st_dev['StDev']
            df = pd.merge_ordered(avg_ret, st_dev_, on='Date')
            df['AvgReturn / StDev'] = df['AvgReturn'] / df['StDev']
            db.append(df)
        return db

    def median_return_over_st_dev(self):
        db = []
        st_devs = self.standard_devation()
        median_returns = self.median_return()
        for (median_return, st_dev) in zip(median_returns, st_devs):
            median_ret = median_return['MedReturn']
            st_dev_ = st_dev['StDev']
            df = pd.merge_ordered(median_ret, st_dev_, on='Date')
            df['MedReturn / StDev'] = df['MedReturn'] / df['StDev']
            db.append(df)
        return db

    def cagr_over_st_dev(self):
        db = []
        st_devs = self.standard_devation()
        cagrs = self.cagr()
        for (cagr, st_dev) in zip(cagrs, st_devs):
            cagr_ = cagr['CAGR']
            st_dev_ = st_dev['StDev']
            df = pd.merge_ordered(cagr_, st_dev_, on='Date')
            df['CAGR / StDev'] = df['CAGR'] / df['StDev']
            db.append(df)
        return db

    def average_return_over_max_dd(self):
        db = []
        max_dds = self.max_drawdown()
        avg_returns = self.average_return()
        for (avg_return, max_dd) in zip(avg_returns, max_dds):
            avg_ret = avg_return['AvgReturn']
            dd = max_dd['MaxDD']
            df = pd.merge_ordered(avg_ret, dd, on='Date')
            df['AvgReturn / MaxDD'] = df['AvgReturn'] / abs(df['MaxDD'])
            db.append(df)
        return db

    def median_return_over_max_dd(self):
        db = []
        max_dds = self.max_drawdown()
        median_returns = self.median_return()
        for (median_return, max_dd) in zip(median_returns, max_dds):
            median_ret = median_return['MedReturn']
            dd = max_dd['MaxDD']
            df = pd.merge_ordered(median_ret, dd, on='Date')
            df['MedReturn / MaxDD'] = df['MedReturn'] / abs(df['MaxDD'])
            db.append(df)
        return db

    def cagr_over_max_dd(self):
        db = []
        max_dds = self.max_drawdown()
        cagrs = self.cagr()
        for (cagr, max_dd) in zip(cagrs, max_dds):
            cagr_ = cagr['CAGR']
            dd = max_dd['MaxDD']
            df = pd.merge_ordered(cagr_, dd, on='Date')
            df['CAGR / MaxDD'] = df['CAGR'] / abs(df['MaxDD'])
            db.append(df)
        return db

# gain to pain ratio - line 50
