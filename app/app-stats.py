from stats import Stats

average_return = Stats().average_return()
median_return = Stats().median_return()
nmaximum_return = Stats().nmaximum_return()
minimum_return = Stats().minimum_return()
standard_devation = Stats().standard_devation()
cagr = Stats().cagr()
max_drawdown = Stats().max_drawdown()

average_return_over_st_dev = Stats().average_return_over_st_dev()
median_return_over_st_dev = Stats().median_return_over_st_dev()
cagr_over_st_dev = Stats().cagr_over_st_dev()

average_return_over_max_dd = Stats().average_return_over_max_dd()
median_return_over_max_dd = Stats().median_return_over_max_dd()
cagr_over_max_dd = Stats().cagr_over_max_dd()

sharpe_ratio = Stats().sharpe_ratio()

print(sharpe_ratio)