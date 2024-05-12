import sys


def to_binary_string(b):
    return f'{b:08b}'


def to_byte(bits):
    return int(bits, 2).to_bytes(length=1, byteorder=sys.byteorder)


if __name__ == "__main__":
    input_bytes = None

    with open(sys.argv[1], "rb") as f:
        input_bytes = f.read()

    with open("exp8.bin", "wb") as f1, open("sign1_mantissa23.bin", "wb") as f2:
        for i in range(0, len(input_bytes), 4):
            float32 = input_bytes[i:i + 4]
            float32_str = reversed(list(map(to_binary_string, float32)))
            float32_str = "".join(list(float32_str))
            exp = float32_str[1:9]
            sign_mantissa = float32_str[0] + float32_str[9:]

            f1.write(to_byte(exp))
            f2.write(to_byte(sign_mantissa[:8]))
            f2.write(to_byte(sign_mantissa[8:16]))
            f2.write(to_byte(sign_mantissa[16:]))
