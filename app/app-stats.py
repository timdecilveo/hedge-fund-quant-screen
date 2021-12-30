import os
import numpy as np
import pandas as pd
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns
from directories import Directory
from stats import Stats

beginning_date = '1993-02-28'
ending_date = '2019-02-28'
end_date = '2019-02-28'

directory = os.listdir(f"../data-files")
file_list = Directory(directory).files()

average_return = Stats().average_return()
median_return = Stats().median_return()
nmaximum_return = Stats().nmaximum_return()
minimum_return = Stats().minimum_return()
standard_devation = Stats().standard_devation()
cagr = Stats().cagr()
max_drawdown = Stats().max_drawdown()
