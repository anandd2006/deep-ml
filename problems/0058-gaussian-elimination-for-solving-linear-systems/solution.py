import numpy as np

def gaussian_elimination(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    # Combine A and b into an augmented matrix
    Ab = np.column_stack((A, b))

    # Forward elimination
    for i in range(n):

        # Find the pivot row
        pivot = i + np.argmax(np.abs(Ab[i:, i]))

        if abs(Ab[pivot, i]) < 1e-12:
            raise ValueError("Matrix is singular")

        # Swap rows
        Ab[[i, pivot]] = Ab[[pivot, i]]

        # Eliminate elements below the pivot
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]

            for k in range(i, n + 1):
                Ab[j, k] -= factor * Ab[i, k]

    # Back substitution
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        total = np.dot(Ab[i, i + 1:n], x[i + 1:n])
        x[i] = (Ab[i, n] - total) / Ab[i, i]

    return x