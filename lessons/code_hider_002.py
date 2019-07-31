word = input("Give me a phrase to decrypt:")
dic = {
    "z": "a",
    "q": "b",
    "e": "c",
    "g": "d",
    "i": "e",
    "b": "f",
    "m": "g",
    "p": "h",
    "n": "i",
    "w": "j",
    "f": "k",
    "c": "l",
    "u": "m",
    "y": "n",
    "h": "o",
    "t": "p",
    "l": "q",
    "x": "r",
    "k": "s",
    "d": "t",
    "v": "u",
    "r": "v",
    "j": "w",
    "s": "x",
    "o": "y",
    "a": "z",
    "Z": "A",
    "Q": "B",
    "E": "C",
    "G": "D",
    "I": "E",
    "B": "F",
    "M": "G",
    "P": "H",
    "N": "I",
    "W": "J",
    "F": "K",
    "C": "L",
    "U": "M",
    "Y": "N",
    "H": "O",
    "T": "P",
    "L": "Q",
    "X": "R",
    "K": "S",
    "D": "T",
    "V": "U",
    "R": "V",
    "J": "W",
    "S": "X",
    "O": "Y",
    "A": "Z"}
encrypted_word = ""
for ch in word:
    if ch in dic:
        encrypted_word = encrypted_word + dic[ch]
    else:
        encrypted_word = encrypted_word + ch

print(encrypted_word)