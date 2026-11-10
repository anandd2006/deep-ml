
import numpy as np

def dummy_regressor(y_train, n_test, strategy='mean', constant=None, quantile=None):

    ans = []

    if strategy == 'mean':
        value = np.mean(y_train)

    elif strategy == 'median':
        value = np.median(y_train)

    elif strategy == 'quantile':
        if quantile is None or quantile < 0 or quantile > 1:
            raise ValueError("Invalid quantile")
        value = np.quantile(y_train, quantile)

    elif strategy == 'constant':
        if constant is None:
            raise ValueError("Constant not provided")
        value = constant

    else:
        raise ValueError("Invalid strategy")

    for i in range(n_test):
        ans.append(float(value))

    return ans
