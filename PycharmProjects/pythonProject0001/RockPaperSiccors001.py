import random

for x in range(3):
    y = random.randint(1, 3)

    if y == 1:
        choice = "ROCK"
    if y == 2:
        choice = "PAPER"
    if y == 3:
        choice = "SCISSORS"

print("Choices: \n" + "1 ROCK\n" + "2 PAPER \n" + "3 SCISSORS" )
player = int(input("What is you choice?"))

if y == 1 and player == 2:
    print("Player WON!")

if y == 2 and player == 3:
    print("Player WON!")

if y == 3 and player == 1:
    print("Player WON!")

if y == 2 and player == 1:
    print("COMPUTER WON!")

if y == 3 and player == 2:
    print("COMPUTER WON!")

if y == 1 and player == 3:
    print("COMPUTER WON!")
