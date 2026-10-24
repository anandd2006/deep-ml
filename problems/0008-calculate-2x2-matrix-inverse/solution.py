def determinant(matrix: list[list[float]]):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    if determinant(matrix)==0:
        return None
    det=determinant(matrix)
    result = [
        [matrix[1][1] / det, -matrix[0][1] / det],
        [-matrix[1][0] / det, matrix[0][0] / det]
    ]

    return result