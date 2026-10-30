import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	value = x
	derivative=float(1)
	for func in reversed(functions):
		if(func=='sin'):
			derivative*=np.cos(value)
			value=np.sin(value)
		elif(func=='square'):
			derivative*=value*2
			value = value**2
		elif(func=='log'):
			derivative*=1/value
			value = np.log(value)
		elif(func=='exp'):
			derivative*=np.exp(value)
			value = np.exp(value)
	return derivative

