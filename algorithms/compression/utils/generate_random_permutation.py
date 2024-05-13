import random


if __name__ == "__main__":
    permutation = list(range(2**24))

    with open("permutation.bin", "wb") as f:
        random.shuffle(permutation)
        
        for value in permutation:
            f.write(value.to_bytes(length=3, byteorder='little'))
