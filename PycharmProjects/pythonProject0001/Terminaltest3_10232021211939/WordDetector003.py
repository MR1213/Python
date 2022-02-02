import itertools
dic = {}

def foo(l):
     yield from itertools.product(*([l] * 3))



words = open("C:\\Users\\maxsu\\OneDrive\\Documents\\PythonReadertest001.txt", "r")


for w in words:
    w = w.lower()
    key = "".join(sorted(w))

    if key in dic:
        sameWords = dic[key]

        print(sameWords[-1])

    else:
        sameWords = set()
        dic[key] = sameWords

    sameWords.add(w)

while 1:
    checkWord = str(input("Enter a Word: "))
    checkWord = checkWord.lower()
    inputKey = "".join(sorted(checkWord))

    if inputKey in dic:
        print(dic[inputKey])
    else:
        print("This word is not in our dictionary")
    if checkWord == "exit":
        break
