def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        val = target - num
        if val in dic:
            return [dic[val], i]
        dic[num] = i


print(twoSum(nums=[2, 7, 11, 15], target=9))
