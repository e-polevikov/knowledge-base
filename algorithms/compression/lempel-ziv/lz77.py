import sys


def find_longest_match(text, dict_start, buffer_start, buffer_size):
    longest_match_start, longest_match_length = None, 0

    for i in range(dict_start, buffer_start):
        match_length = 0

        while match_length < buffer_size - 1 and \
            text[i + match_length] == text[buffer_start + match_length]:
            match_length += 1

        if match_length > longest_match_length:
            longest_match_start, longest_match_length = i, match_length
    
    return longest_match_start, longest_match_length


def encode(text, dict_size, buffer_size):
    encoded_text = []
    dict_start, buffer_start = -dict_size, 0

    while buffer_start < len(text):
        longest_match_start, longest_match_length = find_longest_match(
            text=text,
            dict_start=max(dict_start, 0),
            buffer_start=buffer_start,
            buffer_size=min(buffer_size, len(text) - buffer_start)
        )

        if longest_match_length > 0:
            encoded_text.append((
                longest_match_start - dict_start,
                longest_match_length,
                text[buffer_start + longest_match_length]
            ))

            dict_start += longest_match_length
            buffer_start += longest_match_length
        else:
            encoded_text.append((0, 0, text[buffer_start]))

        dict_start += 1
        buffer_start += 1
    
    return encoded_text


def decode(encoded_text, dict_size):
    text = ""

    for match_start, match_length, character in encoded_text:
        if match_length > 0:
            substr_start = len(text) - dict_size + match_start
            substr_end = substr_start + match_length

            if substr_end <= len(text):
                text += text[substr_start : substr_end]
            else:
                substr = text[substr_start:]

                while len(substr) < match_length:
                    substr += substr
                
                text += substr[:match_length]

        text += character

    return text


def read_text(filename):
    text = ""

    with open(filename, "r") as f:
        text = f.read()
    
    return text


if __name__ == "__main__":
    DICT_SIZE = 8
    BUFFER_SIZE = 4

    text = read_text(sys.argv[1])

    encoded_text = encode(text, dict_size=DICT_SIZE, buffer_size=BUFFER_SIZE)

    print("Encoded text:")

    for record in encoded_text:
        print(*record)
    
    decoded_text = decode(encoded_text, dict_size=DICT_SIZE)

    print("Decoded text:")
    print(decoded_text)

    print(len(encoded_text))
    print(text == decoded_text)
