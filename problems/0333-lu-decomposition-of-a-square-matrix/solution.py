import numpy as np

def lu_decomposition(A: list) -> tuple:
	n = len(A)
	U = [[0 for _ in range(n)]for _ in range (n)]
	L = [[0 for _ in range(n)]for _ in range (n)]
	for i in range(n):
		for k in range(i,n):
			sum=0;
			for j in range(0,i):
				sum+=(L[i][j]*U[j][k])
			U[i][k]=A[i][k]-sum
		for k in range(i,n):
			if (i==k):
				L[i][i]=1
			else :
				sum=0
				for j in range(0,i):
					sum+=(L[k][j]*U[j][i])
				L[k][i]=((A[k][i]-sum)/U[i][i])
	return np.array(L), np.array(U)