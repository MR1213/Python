import random
from os import system, name
from time import sleep

print("Hello, welcome to Among us Random task picker:")
while 1:
    imposter = int(input("How many imposters? "))
    if imposter < 1 or imposter > 2:
        print("You need to enter either 1 or 2 imposters: ")
    else:
        break
while 1:
    crewmate = int(input("How many crewmates? "))
    if crewmate < 3 or crewmate > 10:
        print("You need to enter from 3 to 10 imposters: ")
    else:
        break
if imposter > crewmate or (imposter * 2) > crewmate:
    exit(-3)
list = []

while imposter > 0 or crewmate > 0:
    while 1:
        name = input("Enter you name for a Random Role: ")
        if len(name) != 0:
            break
        else:
            _ = system('cls')
    r = random.randint(0, 1)
    print(r)
    role = ""
    if imposter > 0 and crewmate > 0:
        if r == 0:
            role = "Imposter"
            imposter = imposter - 1
            # Write Tasks
        else:
            role = "Crewmate"
            crewmate = crewmate - 1
            # Write Tasks
    elif imposter > 0:
        role = "Imposter"
        imposter = imposter - 1
    else:
        role = "Crewmate"
        crewmate = crewmate - 1
    print("You are a(n): " + role)
    list += [(name, role)]
    input("PRESS Enter if you REMEMBER your role!")
    _ = system('cls')
print("All roles have been given out")
print("If you forgot your role you are a MORON")

MyFile = open('C:\\Users\\maxsu\\OneDrive\\Documents\\AmongUsRolesPlusName.txt', 'w')
for element in list:
    MyFile.write(str(element) + "\n")
MyFile.close()
