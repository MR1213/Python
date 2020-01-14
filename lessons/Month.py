word = input("What month do you want to see:")
if not word.isnumeric():
    print("Error")
    exit(-1)
w = int(word)

if w > 12:
    print("Error")
    exit(-1)
if w < 1:
    print("Error")
    exit(-1)
dic = {
    1: "January ",
    2: "February ",
    3: "March ",
    4: "April ",
    5: "May ",
    6: "June ",
    7: "July ",
    8: "August ",
    9: "September ",
    10: "October ",
    11: "November ",
    12: "December "}
print(dic[w])
