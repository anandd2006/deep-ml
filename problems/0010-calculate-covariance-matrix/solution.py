import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	v=np.array(vectors)
	fea=len(v)
	obv=len(v[0])
	mean=[]
	for i in range(fea):
		x=0
		for j in range(obv):
			x+=v[i][j]
		x=x/obv
		mean.append(x)

	mat=np.empty((fea,fea))

	for i in range(fea):
		for j in range(fea):
			total =0
			for k in range(obv):
				total+=(v[i][k]-mean[i])*(v[j][k]-mean[j])
			mat[i][j]=total/(obv-1)

	return mat