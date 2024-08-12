import numpy as np
import random
from matplotlib import pyplot as plt


if __name__ == "__main__":
    mu, sigma = 0, 0.01 # mean and standard deviation

    num_floats = 10**5
    print(num_floats)

    floats = np.float16(np.random.normal(mu, sigma, num_floats))
    floats.sort()

    plt.hist(floats)
    plt.show()

    with open("floats.bin", "wb") as f:
        f.write(floats.tobytes())
