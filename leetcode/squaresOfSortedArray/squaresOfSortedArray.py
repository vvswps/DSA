def sortedSquares(nums):
    # left, right = 0, len(nums)-1
    # res = []
    # count = -1
    # while left <= right:
    #     if abs(nums[left]) > abs(nums[right]):
    #         res.insert(count,  nums[left]**2)
    #         left += 1
    #     else:
    #         res.insert(count,  nums[right]**2)
    #         right -= 1
    #     count -= 1
    # return res

    # left, right = 0, len(nums)-1
    # res = []
    # while left <= right:
    #     if nums[left]**2 > nums[right]**2:
    #         res.append(nums[left]**2)
    #         left += 1
    #     else:
    #         res.append(nums[right]**2)
    #         right -= 1
    # return res[::-1]

    return sorted(map(lambda x: x**2, nums))
    # fastest


print(sortedSquares([-4, -1, 0, 3, 10]))
