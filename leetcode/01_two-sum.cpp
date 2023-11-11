#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> indices;

    for (int i = 0; i < nums.size() - 1; i++) {
      for (int j = i + 1; j < nums.size(); j++) {
        if (nums[i] + nums[j] == target) {
          indices.push_back(i);
          indices.push_back(j);
          return indices;
        }
      }
    }

    return indices;
  }
};

int main() {
  vector<int> nums = {3, 2, 4};
  int target = 6;

  Solution solution = Solution();
  vector<int> indices = solution.twoSum(nums, target);
  std::cout << indices[0] << ' ' << indices[1] << std::endl;

  return 0;
}
