    from random import randint


    def wins(guess, total_finger):
        if guess == total_finger:
            print(f"{name} wins!!!")
        else:
            print("You didn't guess the amount of fingers correctly... ")
            if guess > total_finger:
                off = guess - total_finger
            else:
                off = total_finger - guess
            print("You were off by ", off, ". ")


    game_rules = """
        Welcome to Morra! In this game, you'll decide how many fingers
        to hold up (from one hand) and then the computer will randomly
        do the same. You'll need to guess the total number of fingers
        to win the round, before seeing how many fingers the computer
        has decided to hold up!
    """
    print(game_rules)
    player_wins = 0
    computer_wins = 0
    name = str(input("What is your name? "))
    valid_choices = [1, 2, 3, 4, 5]
    rounds = int(input("How many rounds do you want to play? "))
    for valid_choice in valid_choices:
        print(valid_choice)
    for x in range(1, rounds + 1):
        player_finger = int(input("How many fingers do you want to hold up? "))
        if player_finger in valid_choices:
            computer_finger = randint(1, 5)
            total_finger = player_finger + computer_finger
            guess = int(input("How many fingers are held up total? "))
            wins(guess, total_finger)
        else:
            print("Thats an invalid choice...")
            print("You dont have ", player_finger, " fingers. ")
