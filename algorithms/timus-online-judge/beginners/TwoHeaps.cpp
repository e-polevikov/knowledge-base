#include <iostream>

int main() {
  int n;
  int weights[20];
  int minDiff = 0;

  std::cin >> n;
  for (int i = 0; i < n; i++) {
    std::cin >> weights[i];
    minDiff += weights[i];
  }

  for (int N = 1; N <= (1 << n) - 2; N++) {
    int s1 = 0;
    int s2 = 0;

    for (int i = 0; i < n; i++) {
      ((N >> i) & 1) ? s1 += weights[i] : s2 += weights[i];
    }

    minDiff = std::min(minDiff, std::abs(s1 - s2));
  }

  std::cout << minDiff;

  return 0;
}
