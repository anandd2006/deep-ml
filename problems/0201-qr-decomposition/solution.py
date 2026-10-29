import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
	A=np.array(A)
	m, n = A.shape
	Q=np.zeros((m,n))
	R=np.zeros((n,n))

	for k in range (n):
		v=np.zeros(m)
		for i in range (m):
			v[i]= A[i,k]
		for j in range(k):
			dot =0
			for i in range(m):
				dot+= Q[i,j]*A[i,k]
			R[j,k]=dot
			for i in range(m):
				v[i]-=dot*Q[i,j]
		norm=0
		for i in range(m):
			norm += v[i]*v[i]
		norm=np.sqrt(norm)
		if norm < 1e-10:
			raise ValueError("columns are Linearly dependent")
		R[k,k]=norm
		for i in range(m):
			Q[i,k]=v[i]/norm
	return Q, R