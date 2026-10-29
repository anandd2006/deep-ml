
import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
    size = len(b)

    if x0 is None:
        x = np.zeros(size)
    else:
        x = x0.copy()

    r = np.zeros(size)

    for i in range(size):
        total = 0
        for j in range(size):
            total += A[i, j] * x[j]
        r[i] = b[i] - total

    p = np.zeros(size)
    for i in range(size):
        p[i] = r[i]

    rs_old = 0
    for i in range(size):
        rs_old += r[i] * r[i]

    for iteration in range(n):
        Ap = np.zeros(size)

        for i in range(size):
            for j in range(size):
                Ap[i] += A[i, j] * p[j]

        denominator = 0
        for i in range(size):
            denominator += p[i] * Ap[i]

        if abs(denominator) < 1e-15:
            break

        alpha = rs_old / denominator

        for i in range(size):
            x[i] += alpha * p[i]

        for i in range(size):
            r[i] -= alpha * Ap[i]

        rs_new = 0
        for i in range(size):
            rs_new += r[i] * r[i]

        if np.sqrt(rs_new) < tol:
            return x

        beta = rs_new / rs_old

        for i in range(size):
            p[i] = r[i] + beta * p[i]

        rs_old = rs_new

    return x
