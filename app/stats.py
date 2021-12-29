import os
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from directories import Directory

class Stats:
    def __init__(self, beginning_date, end_date):
        # self.df = pd.DataFrame()
        self.directory = os.listdir(f"../data-files")
        self.file_list = Directory(self.directory).files()

        self.beginning_date = dt.datetime.strptime(beginning_date, '%Y-%m-%d')
        self.end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    def average_return(self):
        rows = []
        for i in self.file_list:
            column = i.columns[0]
            avg_return = i[column].expanding().mean()
            rows.append(avg_return)
        
        # print(f"rows:\n{rows}")
        df = pd.DataFrame(rows, columns=['AverageReturn'])
        print(f"df:\n{df}")
        # return df

    # def median_return(self):
    #     for i in self.file_list:
    #         column = i.columns[0]
    #         i['MedianReturn'] = i[column].expanding().median()
    #         self.df = self.df.append(i['MedianReturn'], ignore_index=True)
    #         # print(f"i:\n{i}")
    #     return self.df

    # def max_return(self):
    #     for i in self.file_list:
    #         column = i.columns[0]
    #         i['MaxReturn'] = i[column].expanding().max()
    #         self.df = self.df.append(i['MaxReturn'], ignore_index=True)
    #         # print(f"i:\n{i}")
    #     return self.df

    # def min_return(self):
    #     for i in self.file_list:
    #         column = i.columns[0]
    #         i['MinReturn'] = i[column].expanding().min()
    #         self.df = self.df.append(i['MinReturn'], ignore_index=True)
    #         # print(f"i:\n{i}")
    #     return self.df

    # def st_dev(self):
    #     for i in self.file_list:
    #         column = i.columns[0]
    #         i['StDev'] = i[column].expanding().std()
    #         self.df = self.df.append(i['StDev'], ignore_index=True)
    #         # print(f"i:\n{i}")
    #     return self.df