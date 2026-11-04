import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    A = np.array(A, dtype=float).copy()

    m, n = A.shape
    rank = 0

    for col in range(n):
        pivot = -1

        # Find pivot
        for row in range(rank, m):
            if abs(A[row][col]) > tol:
                if pivot == -1 or abs(A[row][col]) > abs(A[pivot][col]):
                    pivot = row

        if pivot == -1:
            continue

        # Swap rows
        for j in range(n):
            A[rank][j], A[pivot][j] = A[pivot][j], A[rank][j]

        # Eliminate rows below pivot
        for i in range(rank + 1, m):
            factor = A[i][col] / A[rank][col]

            for j in range(col, n):
                A[i][j] -= factor * A[rank][j]

        rank += 1

        if rank == m:
            break

    return rank