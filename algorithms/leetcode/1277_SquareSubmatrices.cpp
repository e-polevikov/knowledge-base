#include <vector>
#include <iostream>

using std::vector; 

class Solution {
public:
    int countSquares(vector<vector<int>> &matrix) {
        size_t nRows = matrix.size();
        size_t nCols = matrix[0].size();

        for (size_t i = 1; i < nRows; i++) {
            matrix[i][0] += matrix[i - 1][0];
        }

        for (size_t j = 1; j < nCols; j++) {
            matrix[0][j] += matrix[0][j - 1];
        }

        for (size_t i = 1; i < nRows; i++) {
            for (size_t j = 1; j < nCols; j++) {
                matrix[i][j] += matrix[i - 1][j]
                    + matrix[i][j - 1]
                    - matrix[i - 1][j - 1];
            }
        }

        int numSquareMatrices = matrix[nRows - 1][nCols - 1];

        for (size_t matrixSize = 2; matrixSize <= std::min(nRows, nCols); matrixSize++) {
            for (size_t i = matrixSize - 1; i < nRows; i++) {
                for (size_t j = matrixSize - 1; j < nCols; j++) {
                    int numOnes = matrix[i][j];

                    if (i >= matrixSize) {
                        numOnes -= matrix[i - matrixSize][j];
                    }

                    if (j >= matrixSize) {
                        numOnes -= matrix[i][j - matrixSize];
                    }

                    if (i >= matrixSize && j >= matrixSize) {
                        numOnes += matrix[i - matrixSize][j - matrixSize];
                    }

                    if (numOnes == matrixSize * matrixSize) {
                        numSquareMatrices += 1;
                    }
                }
            }
        }

        return numSquareMatrices;
    }
};

int main() {
    vector<vector<int>> matrix = {
        {0, 1, 1, 1},
        {1, 1, 1, 1},
        {0, 1, 1, 1}
    };

    Solution sol = Solution();
    std::cout << sol.countSquares(matrix) << std::endl;
}
