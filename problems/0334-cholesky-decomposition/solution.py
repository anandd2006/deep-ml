import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here

    n = len(A)
    lower=[[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            sum=0
            if j==i:
                for k in range(j):
                    sum+=lower[j][k]**2
                if ((A[j][j]-sum)<0): 
                    return -1
                lower[j][j]=(A[j][j]-sum)**0.5
                
            else:
                for k in range(j):
                    sum+=lower[i][k]*lower[j][k]
                lower[i][j]=(A[i][j]-sum)//lower[j][j]

    return lower