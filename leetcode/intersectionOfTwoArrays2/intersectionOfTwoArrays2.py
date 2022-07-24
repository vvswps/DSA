from collections import Counter


def intersect(nums1, nums2):
    nums2 = Counter(nums2)
    nums1 = Counter(nums1)
    res = []

    for i in nums1:
        if i in nums2:
            for _ in range(min(nums1[i], nums2[i])):
                res.append(i)
    return res


print(intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
print(intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
