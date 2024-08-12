import sys


if __name__ == "__main__":
    input_bytes = None

    with open(sys.argv[1], "rb") as f:
        input_bytes = f.read()

    num_groups = 4
    with open("grouped_bytes.bin", "wb") as f:
        for i in range(num_groups):
            for j in range(i, len(input_bytes), num_groups):
                f.write(input_bytes[j].to_bytes(length=1, byteorder='little'))
