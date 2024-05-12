import numpy as np


if __name__ == "__main__":
    mu, sigma = 3, 4.0 # mean and standard deviation
    s = np.float32(np.random.normal(mu, sigma, 2 * 10**6))
    s = np.sort(s)

    with open("floats.bin", "wb") as f:
        f.write(s.tobytes())
