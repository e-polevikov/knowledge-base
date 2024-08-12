import random


if __name__ == "__main__":
    #permutation = list(range(10**2))
    #n = len(permutation)
    #random.shuffle(permutation)

    permutation = []

    for _ in range(10**6):
        permutation.append(random.randint(0, 10**2))

    with open("random_permutation.bin", "wb") as f:
        for value in permutation:
            f.write(value.to_bytes(length=2, byteorder='little'))
