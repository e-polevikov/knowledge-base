#include "array.hpp"

int main() {
    {
        array<int> int_array;
    }

    {
        array<int> array1(10, 42);

        array1[5] = 13;

        for (size_t i = 0; i < array1.size(); i++) {
            std::cout << array1[i] << " ";
        }

        std::cout << std::endl;

        array<int> array2(array1);
        array<int> array3;

        array3 = array2;
        array3 = array1;
        array3 = array3 = array1;
        
        for (size_t i = 0; i < array3.size(); i++) {
            std::cout << array3[i] << " ";
        }

        array<int> array4(array<int>(10, 42));

        std::cout << array4.size() << std::endl;
    }

    {
        array<int> array1(array<int>(10, 42));
        array<int> array2 = std::move(array1);
    }

    return 0;
}
