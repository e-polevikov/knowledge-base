import numpy as np
from matplotlib import pyplot as plt


def linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    m = np.round(m)
    c = np.round(c)

    print(m, c)

    #plt.plot(x, y, 'o', label='Original data', markersize=10)
    #plt.plot(x, m*x + c, 'r', label='Fitted line')
    #plt.legend()
    #plt.show()
    # plt.clear()

    return m, c

def main():
    N = 10**5
    factoradic = []

    for i in range(N):
        factoradic.append(np.random.randint(0, i + 1))
    
    counts = [0] * N

    for value in factoradic:
        counts[value] += 1
    
    freqs = [counts[value] for value in factoradic]

    #print(factoradic)
    #print(counts)
    #print(freqs)

    x = np.array(freqs)
    y = np.array(factoradic)

    z = np.polyfit(x, y, 3)
    p = np.poly1d(z)

    for i in range(20):
        print(x[i], p(x[i]))

    #m, c = linear_regression(x, y)



    #print(m, c)
    #print(np.round(y))
    #predicted = np.round(m*x + c)
    #errors = np.int32(np.round(y) - predicted)

    #errors.tofile("errors.bin")
    
    #plt.hist(factoradic, bins=1000)
    #plt.show()

main()
