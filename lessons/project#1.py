gameboard = [(['.'] * 3) for i in range(3)]

row_col = [0]

turn = 1


def input_valid(values):
    if len(values) != 2:
        print
        "Input must be two numbers in format row,col e.g.  1,2 "

        return 0

    try:

        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):

            if gameboard[int(values[0]) - 1][int(values[1]) - 1] != '.':
                print
                "Position on board already taken."

                return 0

            return 1

        else:

            print
            "Input values must be numbers between 1 and 3 (inclusive)"

            return 0

    except ValueError:

        print
        "Input values must be numbers between 1 and 3 (inclusive)"

        return 0


def draw_board(values, player):
    gameboard[int(values[0]) - 1][int(values[1]) - 1] = player
    for row in gameboard:
        print
        row


def game_over():
    searcht = '.'

    for i in range(3):

        if len(set(gameboard[i])) == 1:

            if gameboard[i][1] == '.':

                continue

            elif gameboard[i][1] == 'X':

                print
                "Game over - Player 1 wins"



            else:

                print
                "Game over - Player 2 wins"

            return 1

    for i in range(3):

        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i]:

            if gameboard[0][i] == '.':

                continue

            elif gameboard[0][i] == 'X':

                print
                "Game over - Player 1 wins"

            else:

                print
                "Game over - Player 2 wins"

            return 1

    if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]) or (
            gameboard[0][2] == gameboard[1][1] == gameboard[2][0]):

        if gameboard[1][1] == 'X':

            print
            "Game over - Player 1 wins"

        elif gameboard[1][1] == 'O':

            print
            "Game over - Player 2 wins"

        else:

            return 0

        return 1

    # check board is full

    for sublist in gameboard:

        if searcht in sublist:
            return 0

    print
    "Game over - the board is filled"

    return 1


# main function that runs the game while board is not full

while not game_over():

    piece = '.'

    # Player input - checks for input correctness

    while not input_valid(row_col):

        player = turn % 2

        if player == 0:

            player = 2

            piece = 'O'

        else:

            piece = 'X'

        p1 = input('Player ' + str(player) + ' input: ')

        row_col = p1.split(",")

    draw_board(row_col, piece)

    row_col = [0]

    turn += 1
