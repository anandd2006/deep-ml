import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	x=np.array(X)
	y=np.array(y)

	xt=x.T
	xtx_inv=np.linalg.inv(xt.dot(x))
	xty=xt.dot(y)
	w=xtx_inv.dot(xty)
	return w