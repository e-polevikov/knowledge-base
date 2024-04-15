#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        vector<int> sums(nums.size(), 0);
        
        int maxSum = sums[0] = nums[0];
        for (size_t i = 1; i < nums.size(); i++) {
            sums[i] = sums[i - 1] + nums[i];
            maxSum = std::max(maxSum, sums[i]);
        }

        for (size_t i = 1; i < sums.size(); i++) {
            for (size_t j = 0; j < i; j++) {
                maxSum = std::max(maxSum, sums[i] - sums[j]);
            }
        }

        return maxSum;
    }
};

int main() {
    Solution s = Solution();

    vector<int> nums = {-1,-2};

    std::cout << s.maxSubArray(nums) << std::endl;

    return 0;
}
