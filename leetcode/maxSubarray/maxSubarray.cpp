#include <vector>;
#include <iostream>;

int maxSubArray(std::vector<int> &nums)
{
    int max = nums[0], curr_max = nums[0];
    for (int i = 1; i < nums.size(); i++)
    {
        curr_max = std::max(nums[i], curr_max + nums[i]);
        if (curr_max > max)
        {
            max = curr_max;
        }
    }
    return max;
}

int main()
{
    std::vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    std::cout << maxSubArray(nums) << std::endl;
    return 0;
}