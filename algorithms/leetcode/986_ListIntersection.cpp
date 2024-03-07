#include <vector>
#include <iostream>

using std::vector;
using std::min;

class Solution {
public:
    bool intersect(
        const vector<int> segment1,
        const vector<int> segment2,
        vector<int> &intersection
    ) {
        if (segment1[0] > segment2[0]) {
            return intersect(segment2, segment1, intersection);
        }

        if (segment2[0] <= segment1[1]) {
            intersection[0] = segment2[0];
            intersection[1] = min(segment1[1], segment2[1]);
            return true;
        }

        return false;
    }

    vector<vector<int>> intervalIntersection(
        vector<vector<int>>& firstList,
        vector<vector<int>>& secondList
    ) {
        vector<vector<int>> intersections;
        vector<int> intersection(2);

        size_t ptr1 = 0;
        size_t ptr2 = 0;

        while (ptr1 < firstList.size() && ptr2 < secondList.size()) {
            if (intersect(firstList[ptr1], secondList[ptr2], intersection)) {
                intersections.push_back(intersection);
            }

            if (ptr1 < firstList.size() && ptr2 < secondList.size()) {
                if (firstList[ptr1][1] <= secondList[ptr2][1]) {
                    ptr1 += 1;
                } else {
                    ptr2 += 1;
                }
            }
        }

        return intersections;
    }
};

int main() {
    vector<vector<int>> firstList = {{0, 2}, {5, 10}, {13, 23}, {24, 25}};
    vector<vector<int>> secondList = {{1, 5}, {8, 12}, {15, 24}, {25, 26}};

    Solution sol = Solution();

    auto intersections = sol.intervalIntersection(firstList, secondList);

    for (const auto &segment : intersections) {
        std::cout << segment[0] << " " << segment[1] << std::endl;
    }

    return 0;
}
