import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	v1_val=0
	v2_val=0
	for i in range(len(v1)):
		v1_val+=v1[i]**2
		v2_val+=v2[i]**2
	v1_val=np.sqrt(v1_val)
	v2_val=np.sqrt(v2_val)

	ans=(v1 @ v2)/(v1_val*v2_val)
	return ans