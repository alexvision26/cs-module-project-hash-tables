# suppose you have a bunch of data and you want to transform it
# you know what it should transorm to

# substituting one letter for another

encode_table = {
    "A": "M",
    "B": "N",
    "C": "B",
    "D": "V",
    "E": "C",
    "F": "X",
    "G": "Z",
    "H": "L",
    "I": "K",
    "J": "J",
    "K": "H",
    "L": "G",
    "M": "F",
    "N": "D",
    "O": "S",
    "P": "A",
    "Q": "P",
    "R": "O",
    "S": "I",
    "T": "U",
    "U": "Y",
    "V": "T",
    "W": "R",
    "X": "E",
    "Y": "W",
    "Z": "Q"
}

decode_table = {}

def build_decode(encoding_table):
    for key, value in encode_table.items():
        decode_table(value) = key

def decode(s):
    decoded_string = ""
    for character in s:
        if character not in decode_table:
            decoded_string += character
        else:
            unscrambled_character = decode_table[character]
            decoded_string

def encode(s):
    encoded_string = ""

    s = s.upper()
    for character in s:
        if character