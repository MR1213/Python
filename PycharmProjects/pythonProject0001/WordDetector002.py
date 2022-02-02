import re


def convert(lst):
    return ' '.join(lst).split()

lst = open("C:\\Users\\maxsu\\OneDrive\\Documents\\PythonReadertest001.txt", "r")
words = convert(lst)

procesed_words = set()
for x in words:
    x = re.sub(r'[^\w]', '', x)
    x = x.lower()
    sorted_characters = sorted(x)
    x = "".join(sorted_characters)
    #print(x)
    procesed_words.update(x)





count = len(procesed_words)
print(count)


