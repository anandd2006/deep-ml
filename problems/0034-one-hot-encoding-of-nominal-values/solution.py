
import numpy as np

def to_categorical(x, n_col=None):

    mx = np.max(x)

    if n_col is None:
        n_col = mx + 1

    if n_col <= mx:
        raise ValueError("n_col is too small")

    z = np.zeros((len(x), n_col))

    for i in range(len(x)):
        z[i][x[i]] = 1

    return z