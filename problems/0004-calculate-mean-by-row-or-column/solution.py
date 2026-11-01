import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	matrix=np.array(matrix)
	n , m = matrix.shape
	ans=[]
	if(mode=='column'):
		for i in range(m):
			x=0
			for j in range(n):
				x+=matrix[j][i]
			ans.append(x/n)
		return ans
	else:
		for i in range(n):
			x=0
			for j in range(m):
				x+=matrix[i][j]
			ans.append(x/m)
		return ans