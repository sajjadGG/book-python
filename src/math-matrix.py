def matrix_multiplication(A, B):
    """
    >>> A = [[1, 0], [0, 1]]
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]
    """
    C = [[0, 0], [0, 0]]

    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            for k in range(0, len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C
