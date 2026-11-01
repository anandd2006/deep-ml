def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	
	ex=(n+1)/2
	fx=((n+1)*(2*n+1))/6
	return [ex,fx-ex**2]