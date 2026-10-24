def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0])!=len(b):
		return -1;
	
	result=[]

	for x in a:
		total =0;
		for y in range(len(b)):
			total+=x[y]*b[y]
		result.append(total)

	return result