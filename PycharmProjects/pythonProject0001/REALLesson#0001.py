health = 100
name = str(input("What is your characters name? "))
print("Adding character... \nSuccessfully added: " + name)
difficulty = str(input("What difficulty would you like to play on?\nEasy \nMedium \nHard \n"))
if difficulty == "Easy" or "easy":
    ouch = 10
    creatures = 10
    healing = 10
    healingPotion = 20
    print("In Easy difficulty there are " + str(creatures) + " creatures and they do " + str(ouch) + " Damage")
elif difficulty == "Medium" or "medium":
    ouch = 15
    creatures = 10
    healing = 5
    healingPotion = 15
    print("In Medium difficulty there are " + str(creatures) + " creatures and they do " + str(ouch) + " Damage")
elif difficulty == "Hard" or "hard":
    ouch = 20
    creatures = 10
    healing = 5
    healingPotion = 10
    print("In Hard difficulty there are " + str(creatures) + " creatures and they do " + str(ouch) + " Damage")
else:
    print("That's not a difficulty \n")

ask1 = str(input("Are you sure you want to play on difficulty " + str(difficulty) + "? "))

if ask1 == "No":
    exit(-2)
if ask1 == "no":
    exit(-2)
hardcreatures = 2 * creatures
for x in range(0, creatures):
    health = health - creatures + healing

print("After round one you have " + str(health) + " health...")
if health <= 0:
    print("Your Dead...")
else:
    print("Good job on surviving round 1!")
    print("You have " + str(health) + " left")

answer = str(input("Round 2 will be harder, Are you ready? \n"))
if answer == "Yes" or "yes":
    for x in range(0, hardcreatures):
        health = health - creatures + healing
        if health <= 50:
            potion = str(input("You are talking massive damage, would you like to splash a potion of Health? \n"))
            if potion == "Yes":
                health = health + healingPotion
            else:
                print("You have only " + health + "health left!")
                if health <= 0:
                    print("Your Died on level 2...")

answer1 = str(input("Round 3 will be harder, Are you ready? \n"))
if answer1 == "Yes" or "yes":
    for x in range(0, hardcreatures):
        health = health - hardcreatures + healing
        if health <= 50:
            potion = str(input("You are talking massive damage, would you like to splash a potion of Health? \n"))
            if potion == "Yes":
                health = health + healingPotion
            else:
                print("You have only " + health + "health left!")
                if health <= 0:
                    print("Your Died on level 3...")

print(health)
