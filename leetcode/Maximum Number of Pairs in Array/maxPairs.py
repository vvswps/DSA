# nums = [1, 3, 2, 1, 3, 2, 2]
nums = [5, 12, 53, 22, 7, 59, 41, 54, 71, 24, 91, 74, 62, 47, 20, 14, 73, 11, 82, 2, 15, 38,
        38, 20, 57, 70, 86, 93, 38, 75, 94, 19, 36, 40, 28, 6, 35, 86, 38, 94, 4, 90, 18, 87, 24, 22]
pairs = 0

if len(nums) > 1:
    for i in nums:
        # print(i, nums, nums.count(i))
        count = nums.count(i)
        if count is not 1:
            nums.remove(i)
            nums.remove(i)
            pairs += 1
    # print(nums)
    print([pairs, len(nums)])

else:
    print("[0,1]")
