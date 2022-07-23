def maxSubarray(nums):
    maxSum = curr_max = nums[0]
    for i in range(len(nums)):
        curr_max = max(nums[i], nums[i]+curr_max)
        if curr_max > maxSum:
            maxSum = curr_max
    return maxSum


print(maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
