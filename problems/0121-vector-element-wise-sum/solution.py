def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	n=len(a)
	m=len(b)
	if n!=m:
		return -1
	result=[]
	for i in range (n):
		result.append(a[i]+b[i])

	return result