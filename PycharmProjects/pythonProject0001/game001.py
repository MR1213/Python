import random
x = 1
name = str(input("What is your characters name? "))
print("Adding character... \nSuccessfully added: " + name)
difficulty = str(input("What difficulty would you like to play on?\nEasy \nMedium \nHard \n"))
if difficulty.lower() == "easy":
    ouch = random.randint(5,10)
    creatures = 10
    print("In Easy difficulty there are " + str(creatures) + " creatures and they do " + str(ouch) + " Damage")
elif difficulty.lower() == "medium":
    ouch = random.randint(10,15)
    creatures = 10
    print("In Medium difficulty there are " + str(creatures) + " creatures and they do " + str(ouch) + " Damage")
elif difficulty.lower() == "hard":
    ouch = random.randint(15,25)
    creatures = 10
    print("In Hard difficulty there are " + str(creatures) + " creatures. ")
else:
    print("That's not a difficulty \n")

ask1 = str(input("Are you sure you want to play on difficulty " + str(difficulty) + "? "))



def round(x, health):
    healingPotion = random.randint(10,20)
    hardcreatures = random.randint(1,5)
    healing = 10
    potionamount = 5
    for y in range(0, hardcreatures):
        health = health - (hardcreatures * ouch) + healing
        if health <= 50:
            potion = str(input("You are talking massive damage, would you like to splash a potion of Health? \n"))
            print("You have only " + str(health) + " health left!")
            if potion.lower() == "yes":
                health = health + healingPotion
                potionamount = potionamount - 1
                print(health)
                print("You have only " + str(health) + " health left!")
        if health <= 0:
            print("Your Died on level " + x + "...")




    print(health)
    return health


health = 100

while health > 0:
    if x == 1:
        answer1 = str(input("Round 1 is easy, Are you ready? \n"))
    else:
        answer1 = str(input("Round " + str(x) + " will be harder, Are you ready? \n"))
    if answer1.lower() == "yes":
        health = round(x, health)
        x = x + 1
    else:
        break
print("Your Died on level " + str(x) + "...")