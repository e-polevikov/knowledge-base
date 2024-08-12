from itertools import permutations
import numpy as np


def same_order(values1, values2):
    for i in range(len(values1) - 1):
        order1 = [0, 1][bool(values1[i] > values1[i + 1])]
        order2 = [0, 1][bool(values2[i] > values2[i + 1])]

        if order1 != order2:
            return False
    
    return True


def same_signs(values1, values2):
    for i in range(len(values1)):
        sign1 = [0, 1][bool(values1[i]) > 0]
        sign2 = [0, 1][bool(values2[i]) > 0]

        if sign1 != sign2:
            return False
    
    return True


def get_deltas(values):
    deltas = []
    
    for i in range(len(values) - 1):
        deltas.append(values[i + 1] - values[i])
    
    return np.array(deltas, dtype=np.float64)


def values_equal(values1, values2, idxs):
    for idx in idxs:
        if values1[idx] != values2[idx]:
            return False
    
    return True


def main():
    N = 10

    values = np.random.normal(0, 0.01, N).astype(np.float32)
    deltas_var = get_deltas(values).var()
    values_copy = np.copy(values)

    np.random.shuffle(values_copy)

    num_same_order_permutations = 0
    num_equal_deltas_var_permutations = 0
    for values_permutation in permutations(values_copy):
        values_permutation = np.array(values_permutation, dtype=np.float32)

        if not values_equal(values, values_permutation, [0, 2, 4, 6, 8]):
            continue

        if same_order(values, values_permutation):
            num_same_order_permutations += 1

            if deltas_var == get_deltas(values_permutation).var():
                num_equal_deltas_var_permutations += 1

                print(np.array_equal(values, values_permutation))


    print(num_same_order_permutations)
    print(num_equal_deltas_var_permutations)


if __name__ == "__main__":
    main()
