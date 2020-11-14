import random

print("Hello, welcome to Among us Random task picker")
imposter = int(input("How many imposters?"))
crewmate = int(input("How many crewmates?"))
tasks = int(input("How many tasks for each person (1,18):"))
# randomtasks =

thetask = random.randint(1, 12)
for x in range(tasks):
    thetask = random.randint(0, 12)
    if thetask == 1:
        print("Test Lights (1-4)")
    elif thetask == 2:
        print("Type Hello:")
    elif thetask == 3:
        print("Test Frequency")
    elif thetask == 4:
        print("Fix Wiring (1-3)")

if imposter:
    print("Kill everyone.")
    print("Fake Tasks:")
    # print(randomtasks)
