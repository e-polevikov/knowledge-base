#include <iostream>

template<int N>
struct Fib {
    static int const value = Fib<N - 1>::value + Fib<N - 2>::value;
};

template<>
struct Fib<1> {
    static int const value = 1;
};

template<>
struct Fib<0> {
    static int const value = 0;
};

int main() {
    const int f10 = Fib<10>::value;

    std::cout << f10 << std::endl;
    return 0;
}