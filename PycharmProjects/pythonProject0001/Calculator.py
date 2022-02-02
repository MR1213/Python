import re

print("Welcome to Python Calculator: ")
old = 0
go = True


def doMath():
    global go
    global old
    equation = ""
    if old == 0:
        equation = input("What do you want me to calculate? ")
    else:
        equation = input(str(old))
    if equation == 'quit':
        exit(-1)
    elif equation == 'Quit':
        exit(-2)
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        old = eval(equation)

while go:
    doMath()
    print("The answer is: " + str(old))