text = "I encrypted this text and I say hello to everyone who could read it and you are great"
dictionary = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! '
secret_text = ""


# ENCODE Text
def encode_text(input_text):
    global secret_text
    shift_left, shift_right = 28, 12

    for char in range(len(input_text)):
        index = dictionary.index(input_text[char])
        if char % 2 == 0:
            new_pos = (index - shift_right + len(dictionary)) % len(dictionary)
        else:
            new_pos = (index + shift_left + len(dictionary)) % len(dictionary)
        secret_text += dictionary[new_pos]

    return secret_text

encode_text(text)
print(secret_text)


# DECODE Text
def decode_text(encoded_text):
    global secret_text
    shift_left, shift_right = 28, 12

    for char in range(len(encoded_text)):
        index = dictionary.index(encoded_text[char])
        if char % 2 == 0:
            new_pos = (index + shift_right + len(dictionary)) % len(dictionary)
        else:
            new_pos = (index - shift_left + len(dictionary)) % len(dictionary)
        secret_text += dictionary[new_pos]

    return secret_text

decode_text(secret_text)
print(f"А этот текст мы расшифровали:\n {secret_text}")
