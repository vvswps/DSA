from typing import List


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # for i in range(k):
    #     nums.insert(0, nums.pop())

    k %= len(nums)   # this is if k is greater than the length of nums

    def rotateArray(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    rotateArray(0, len(nums)-1)
    rotateArray(0, k-1)
    rotateArray(k, len(nums)-1)


nums = [1, 2, 3, 4, 5, 6, 7]

rotate(nums, k=3)
print(nums)
