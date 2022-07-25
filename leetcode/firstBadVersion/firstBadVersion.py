def firstBadVersion(n):
    left, right = 0, n

    while left < right:
        mid = (left+right)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid+1

    if left == right and isBadVersion(left):
        return left


def isBadVersion(n):
    return n >= 5


print(firstBadVersion(5))
