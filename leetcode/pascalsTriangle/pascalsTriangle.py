def generate(numRows):
    # res = [[1], [1, 1]]
    # if numRows == 1:
    #     return [[1]]
    # elif numRows == 2:
    #     return res
    # for i in range(numRows-2):
    #     i, j = 0, 1
    #     temp = [1, 1]
    #     for _ in range(len(res[-1])-1):
    #         temp.insert(-1, res[-1][i]+res[-1][j])
    #         i += 1
    #         j += 1
    #     res.append(temp)

    # return res.

    res = [[1]]

    for i in range(numRows-1):
        temp = [0]+res[-1]+[0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res


print(generate(5))
print(generate(1))
