#include <vector>
#include <iostream>

using std::vector; 

class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> bits(n + 1, 0);
        int pow2 = 1;

        while (pow2 <= n) {
            for (int i = 0; i < pow2 && pow2 + i < n + 1; i++) {
                bits[pow2 + i] = bits[i] + 1;
            }

            pow2 <<= 1;
        }

        return bits;
    }
};

int main() {
    Solution sol = Solution();

    std::vector<int> bits = sol.countBits(33);

    for (size_t i = 0; i < bits.size(); i++) {
        std::cout << bits[i] << " ";
    }

    std::cout << std::endl;

    return 0;
}
