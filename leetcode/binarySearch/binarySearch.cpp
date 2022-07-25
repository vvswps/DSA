#include <iostream>

int binarySearch(int *nums, int numsSize, int target)
{
    int left = 0;
    int right = numsSize - 1;
    while (left <= right)
    {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target)
        {
            return mid;
        }
        else if (nums[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    return -1;
}

int main()
{
    int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target = 5;
    int result = binarySearch(nums, 10, target);
    std::cout << result << std::endl;
    return 0;
}