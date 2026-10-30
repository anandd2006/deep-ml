import math
import numpy as np

PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
	days = np.arange(1 , 11)
	fluctuation = 10 * np.sin(2*PI*days/10)
	detrended = consumption_data - fluctuation
	x=np.column_stack((np.ones(10),days))
	w = np.linalg.solve(x.T @ x, x.T @ detrended)
	lis = np.array([1, 15])
	base15 = lis @ w
	result = math.ceil(base15*1.05)
	return result



