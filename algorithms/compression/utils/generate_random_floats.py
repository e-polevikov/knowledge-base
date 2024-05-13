import numpy as np


if __name__ == "__main__":
    mu, sigma = 3, 4.0 # mean and standard deviation

    num_floats = 2**24
    print(num_floats)

    s = np.float32(np.random.normal(mu, sigma, num_floats))
    s = np.sort(s)

    with open("floats.bin", "wb") as f:
        f.write(s.tobytes())
