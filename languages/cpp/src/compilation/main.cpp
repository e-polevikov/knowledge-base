#include <iostream>
#include "pow.hpp"

int main() {
    int value, p;

    std::cin >> value >> p;
    std::cout << pow(value, p) << std::endl;

    return 0;
}
