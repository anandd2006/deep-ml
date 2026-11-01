import numpy as np
from scipy import stats

def descriptive_statistics(a: list | np.ndarray) -> dict:
    d = {}

    d['mean'] = np.mean(a)
    d['median'] = np.median(a)
    d['mode'] = stats.mode(a, keepdims=False).mode
    d['variance'] = np.var(a)
    d['standard_deviation'] = np.std(a)

    q1 = np.percentile(a, 25)
    q2 = np.percentile(a, 50)
    q3 = np.percentile(a, 75)

    d['25th_percentile'] = q1
    d['50th_percentile'] = q2
    d['75th_percentile'] = q3
    d['interquartile_range'] = q3 - q1

    return d