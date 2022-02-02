import re
import urllib.request
import requests
def convert(lst):
    return ' '.join(lst).split()

link = "https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"
f = requests.get(link)
lst = f.read()

#lst = open("C:\\Users\\maxsu\\OneDrive\\Documents\\PythonReadertest001.txt", "r")


words = convert(lst)

procesed_words = set()
for x in words:
    x = re.sub(r'[^\w]', '', x)
    x = x.lower()
    #x = ''.join(sorted(x))
    print(x)
    procesed_words.update(x)

count = len(procesed_words)
print(count)
print(convert(lst))



link = ""
f = urllib.urlopen(link)
myfile = f.read()
