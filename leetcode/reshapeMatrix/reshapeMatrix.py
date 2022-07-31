def matrixReshape(mat, r, c):
    m = len(mat[0])
    n = len(mat)
    if (n == r and m == c) or r*c != m*n:
        return mat

    flat = [i for sublist in mat for i in sublist]
    count = 0
    res = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            res[i][j] = flat[count]
            count += 1
    return res


print(matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4))
print(matrixReshape(mat=[[1, 2], [3, 4]], r=2, c=4))
