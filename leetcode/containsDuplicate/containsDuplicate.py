from collections import Counter


def containsDuplicate(nums):
    # return False if len(nums) == len(set(nums)) else True

    # dict = {}
    # for i in nums:
    #     if i in dict:
    #         return True
    #     else:
    #         dict[i] = 1
    # return False

    # count = sorted(Counter(nums))
    # for i in count:
    #     if count[i]>1:
    #         return True
    # return False

    # count = sorted(Counter(nums).values())
    # return True if count[-1] > 1 else False

    # duplicate check
    return len(nums) != len(set(nums))


print(containsDuplicate([0, 4, 5, 0, 3, 6]))
print(containsDuplicate([1, 2, 3, 4]))
