import random

# define a list of words to choose from
words = ["python", "programming", "computer", "code", "algorithm", "variable", "function", "debugging", "loop", "string"]

# choose a random word from the list
word = random.choice(words)

# create a list to keep track of the user's guesses
guesses = []

# set the number of turns
turns = 6

# play the game
while turns > 0:
    # display the current state of the word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

    # check if the game is over
    if "_" not in display_word:
        print("You win!")
        break

    # get a letter guess from the user
    guess = input("Guess a letter: ")

    # check if the guess is correct
    if guess in word:
        print("Correct!")
        guesses.append(guess)
    else:
        print("Incorrect.")
        turns -= 1

    # check if the game is over
    if turns == 0:
        print("You lose. The word was", word)
    elif "_" not in display_word:
        print("You win!")
        break

    # display the remaining turns
    print("You have", turns, "turns left.")
