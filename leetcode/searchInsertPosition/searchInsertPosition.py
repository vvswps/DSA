def searchInsert(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return left


print(searchInsert(nums=[1, 3, 5, 6], target=5))
print(searchInsert(nums=[1, 3, 5, 6], target=2))
print(searchInsert(nums=[1, 3, 5, 6], target=7))
print(searchInsert(nums=[1, 3, 5, 6], target=0))
