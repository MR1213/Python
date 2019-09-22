import random

def dice():
    res = []
    for f in range(3):
        res.append(random.randint(1, 6))
    return res

def roll(round_number):
    res = []

    while True:
        tem_res = dice()
        print("Current roll {0}".format(tem_res))
        res.extend(tem_res)
        if round_number not in tem_res:
            break
    return res


#round_number = int(input("Enter the round number: "))
round_number = 3

for i in range(10):
    res = roll(round_number)
    print("Final result for current player {0}".format(res))
