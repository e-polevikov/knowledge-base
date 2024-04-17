import sys


def encode(text):
    phrases = dict()
    curr_phrase = ""

    for i in range(len(text)):
        curr_phrase += text[i]

        phrase_id = phrases.get(curr_phrase, None)

        if phrase_id is None:
            phrases[curr_phrase] = len(phrases)
            curr_phrase = ""
    
    phrases = {(phrase_id, phrase) for phrase, phrase_id in phrases.items()}

    if len(curr_phrase) > 0:
        phrases.add((len(phrases), curr_phrase))
    
    id_to_phrase = [""] * len(phrases)

    for phrase_id, phrase in phrases:
        id_to_phrase[phrase_id] = phrase
    
    encoded_phrases = [id_to_phrase[0]]

    for i in range(1, len(id_to_phrase)):
        phrase_prefix = id_to_phrase[i][:-1]
        phrase_last_ch = id_to_phrase[i][-1]

        try:
            phrase_prefix_id = id_to_phrase.index(phrase_prefix)
        except ValueError:
            phrase_prefix_id = ''

        encoded_phrases.append(f"{phrase_prefix_id}{phrase_last_ch}")
    
    return encoded_phrases


def decode(encoded_phrases):
    decoded_phrases = [encoded_phrases[0]]

    for i in range(1, len(encoded_phrases)):
        if len(encoded_phrases[i]) == 1:
            phrase_prefix = ""
        else:
            phrase_id = int(encoded_phrases[i][:-1])
            phrase_prefix = decoded_phrases[phrase_id]

        phrase_last_ch = encoded_phrases[i][-1]

        decoded_phrase = f"{phrase_prefix}{phrase_last_ch}"
        decoded_phrases.append(decoded_phrase)

    decoded_text = "".join(decoded_phrases)

    return decoded_text


if __name__ == "__main__":
    text = ""

    with open(sys.argv[1], "r") as f:
        text = f.read()
    
    encoded_phrases = encode(text)

    print(len(text))
    print(len(encoded_phrases))

    decoded_text = decode(encoded_phrases)

    print(text == decoded_text)
