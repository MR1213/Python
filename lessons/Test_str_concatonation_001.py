word = input("Give me a phrase to encrypt:")
dic = {
    "a": "z",
    "b": "q",
    "c": "e",
    "d": "g",
    "e": "i",
    "f": "b",
    "g": "m",
    "h": "p",
    "i": "n",
    "j": "w",
    "k": "f",
    "l": "c",
    "m": "u",
    "n": "y",
    "o": "h",
    "p": "t",
    "q": "l",
    "r": "x",
    "s": "k",
    "t": "d",
    "u": "v",
    "v": "r",
    "w": "j",
    "x": "s",
    "y": "o",
    "z": "a",}
encrypted_word = ""
for ch in word:
    if ch in dic:
        encrypted_word = encrypted_word + dic[ch]
    else:
        encrypted_word = encrypted_word + ch

print(encrypted_word)
