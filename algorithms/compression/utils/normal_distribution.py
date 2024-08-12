import numpy as np
from matplotlib import pyplot as plt

def f(x, mean, sigma):
    f = (1 / sigma * np.sqrt(2 * np.pi)) * np.e**(-(1/2) * ((x - mean / sigma)**2))
    f = np.floor(f * 2**10)
    return f


def invf(y, mean, sigma, sign):
    return mean + sign * np.sqrt(4 * np.log(2 * np.pi * y))


def main():
    m, s = 0, 1.0

    floats = np.float32(np.random.normal(m, s, 10**5))
    rounded_floats = np.int32(np.floor((floats * 2**5)))
    initial_floats = np.float32(rounded_floats / 2**5)
    errors = np.int32(np.float32(floats - initial_floats) * 2 ** 23)

    print(floats)
    print(initial_floats + errors / 2**23)

    floats.tofile("floats.bin")
    rounded_floats.tofile("rounded_floats.bin")
    errors.tofile("errors.bin")


    plt.hist(errors, bins=10)
    plt.show()

main()
