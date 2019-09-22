import random


class player:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def __str__(self):
        return str(self.name)


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
if players<1:
    print("ERROR, NOT ENOUGH PLAYERS!")
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
