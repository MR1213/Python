import random
import operator

def dice():
    res = []
    for f in range(3):
        res.append(random.randint(1, 6))
    return res

def roll(round_number):
    res = []

    while True:
        tem_res = dice()
        # print("Current roll {0}".format(tem_res))
        res.extend(tem_res)
        if round_number not in tem_res:
            break
    return res


def divide_chunks(list, n=3):
    # looping till length l
    for i in range(0, len(list), n):
        yield list[i:i + n]

def calculate_point_for_dice(round_number, list):
    n = list.count(round_number)
    points = 0
    if n == 0:
        if list.count(list[0]) == 3:
            points += 5
    elif n < 3:
        points += n
    else:
        points += 21
    return points

def calculate_point_full_roll(round_number, roll_list):
    points = 0

    for i in range(0, len(roll_list), 3):
        chunk = roll_list[i:i + 3]
        points += calculate_point_for_dice(round_number, chunk)
        # print("Point on each roll {0}".format(points))
    return  points




players = {"Maksym": 0, "Tom": 0, "Valeria": 0}

for round_number in range(1, 7):
    # round_number = int(input("Enter the round number: "))
    # round_number = 3

    print("Round {0}".format(round_number))

    for player_name in players:

        res = roll(round_number)
        print("Final result for {0}: {1}".format(player_name, res))

        points = players[player_name]
        points += calculate_point_full_roll(round_number, res)
        print("Total points {0}: {1}".format(player_name, points))

        players[player_name] = points


print("Results {0}".format(players))
winner = max(players, key=players.get)
print("Winner {0}".format(winner))