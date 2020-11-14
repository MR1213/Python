import random
class player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def get_name(self):
        return self.name

    def __str__(self):
        st = "Player {0} got {1} points!".format(self.name, self.points)
        return st

    def get_point(self):
        return self.points

    def add_points(self, points):
        self.points = points + self.points

class table:
    def __init__(self, order_number):
        self.order_number = order_number
        self.players = []
    def get_order_number(self):
        print(self.order_number)
    def add_player(self, player):
        self.players.append(player)
    def get_players(self):
        return self.players
    def __str__(self):
        st = "Table {0}".format(self.order_number)
        for k in self.players:
            st = st + "\n     Player {0}".format(str(k))
        return st
r = random.randint
def dice():
    res = []
    for f in range(3):
        res.append(random.randint(1, 6))
    return res
print("Welcome to Bunco!")
tables_count = int(input("Enter number of tables: "))
tables = []
players = tables_count * 4
#______________________________________________________
if tables_count <2:
    print("ERROR, NOT ENOUGH TABLES!")
    exit(-1)
else:
    print("There are {0} players".format(players))
#______________________________________________________
for i in range(tables_count):
    print("\nFiling up Table {0}".format(i + 1))
    table_i = table(i + 1)
    tables.append(table_i)
    for j in range(4):
        name = input("Enter name of player {0}: ".format(j + 1))
        player_j = player(name)
        table_i.add_player(player_j)
for q in tables:
    print(str(q))
print(r, player)
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

for round_number in range(1, 7):
    # round_number = int(input("Enter the round number: "))
    # round_number = 3
    print("Round {0}".format(round_number))
    for table in tables:
        players=table.get_players()
        for player in players:
            player_name=player.get_name()
            #print(player_name)
            res = roll(round_number)
            print("Final result for {0}: {1}".format(player_name, res))

            points = calculate_point_full_roll(round_number, res)
            player.add_points(points)
            points = player.get_point()
            print("Total points {0}: {1}".format(player_name, points))


for table in tables:
    print("{0}".format(table))
#winner = max(players, key=players.get)
#print("Winner {0}".format(winner))


