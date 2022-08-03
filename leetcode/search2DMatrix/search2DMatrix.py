def searchMatrix(matrix, target):
    matrix = [i for sublist in matrix for i in sublist]

    left, right = 0, len(matrix)-1

    while left <= right:
        mid = (left+right)//2
        if matrix[mid] == target:
            return True
        elif matrix[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return False


print(searchMatrix(matrix=[[1, 3, 5, 7], [
      10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(searchMatrix(matrix=[[1, 3, 5, 7], [
      10, 11, 16, 20], [23, 30, 34, 60]], target=13))
