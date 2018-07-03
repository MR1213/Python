


def mystr(word):
    print(word.strip()[-1])
    print(word.strip()[0])
    res = (word.strip()[-1]) == (word.strip()[0])
    if (word.strip()[-1]) == (word.strip()[0]):
        print("The Same!")
    else:
        print("Different!")

    print("length: " + str(len(word)))


mystr("123451")