import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	m=np.mean(data,axis=0)
	s=np.std(data,axis=0)

	z=(data-m)/s

	mn=np.min(data,axis=0)
	mx=np.max(data,axis=0)

	x=(data-mn)/(mx-mn)

	return (z,x)