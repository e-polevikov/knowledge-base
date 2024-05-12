import random


if __name__ == "__main__":
    permutation = list(range(2**10))

    with open("permutation.bin", "wb") as f:
        for _ in range(1000):
            random.shuffle(permutation)
            
            for value in permutation:
                f.write(value.to_bytes(length=2, byteorder='little'))
