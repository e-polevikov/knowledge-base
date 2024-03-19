#include "pow.hpp"

int pow(int value, int p) {
    if (p == 0) {
        return 1;
    }

    if (value <= 1) {
        return value;
    }

    int result = 1;
    while (p > 0) {
        result *= value;
        p -= 1;
    }

    return result;
}
