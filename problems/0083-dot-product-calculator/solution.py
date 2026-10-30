import numpy as np

def calculate_dot_product(vec1, vec2):
	ans = 0;
	for i in range(len(vec1)):
		ans+=vec1[i]*vec2[i]

	return ans