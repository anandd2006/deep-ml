import numpy as np

def calculate_correlation_matrix(X, Y=None):
    X = np.array(X, dtype=float).T

    if Y is None:
        Y = X
    else:
        Y = np.array(Y, dtype=float).T

    fea = len(X)
    fea2 = len(Y)
    obv = len(X[0])

    mean_x = []
    mean_y = []
    std_x = []
    std_y = []

    for i in range(fea):
        x = 0
        for j in range(obv):
            x += X[i][j]
        mean_x.append(x / obv)

    for i in range(fea2):
        x = 0
        for j in range(obv):
            x += Y[i][j]
        mean_y.append(x / obv)

    for i in range(fea):
        std_x.append(np.std(X[i], ddof=1))

    for i in range(fea2):
        std_y.append(np.std(Y[i], ddof=1))

    mat = np.empty((fea, fea2))

    for i in range(fea):
        for j in range(fea2):
            total = 0

            for k in range(obv):
                total += (X[i][k] - mean_x[i]) * (Y[j][k] - mean_y[j])

            if std_x[i] == 0 or std_y[j] == 0:
                mat[i][j] = 0
            else:
                cov = total / (obv - 1)
                mat[i][j] = cov / (std_x[i] * std_y[j])

    return mat