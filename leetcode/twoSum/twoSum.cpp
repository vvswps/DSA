#include <bits/stdc++.h>

using namespace std;

// two sum function
vector<int> twoSum(vector<int> &nums, int target)
{
    vector<int> result;
    unordered_map<int, int> hash;
    for (int i = 0; i < nums.size(); i++)
    {
        if (hash.find(target - nums[i]) != hash.end())
        {
            result.push_back(hash[target - nums[i]]);
            result.push_back(i);
            return result;
        }
        hash[nums[i]] = i;
    }
    return result;
}

int main()
{
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> result = twoSum(nums, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}