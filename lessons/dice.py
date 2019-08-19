import random


def dice():
    res=[]

    for f in range(3):
        res.append(random.randint(1, 6))

    return res

print(dice())