def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    
    result = []

    for i in range(len(a[0])):
        temp =[]
        for j in range(len(a)):
            temp.append(a[j][i])
        result.append(temp)

    return result 
