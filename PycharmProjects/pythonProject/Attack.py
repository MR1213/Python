import random

health = 100


def attack():
    r = random.random()
    x = (41 * r) + 20
    a = int(x)
    return a


life1 = health - attack()
print("After the first attack you have", life1, "health left.")
life2 = life1 - attack()
print("After the second attack you have", life2, "health left.")

if life2 <= 0:
    print("You are dead!")
    exit(0)
else:
    print("You have survived!")

life3 = life2 - attack()
print("After the third attack you have", life3, "health left.")

if life3 <= 0:
    print("You are dead!")
else:
    print("You have survived!")
    print("You are one of few that remain alive!")