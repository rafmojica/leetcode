// O(n^2) approach:
// - nested for loop
// - compare each number to next

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (i == j)
                    j += 1;
                if ((nums[i] + nums[j]) == target)
                    return vector<int>{i, j};
            }
        }
        return {};
    }
};