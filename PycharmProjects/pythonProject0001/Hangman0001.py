word = input(str("What is the word? "))
word.lower()
for q in range(1, 25):
    print("\n")
# for characters in [*word]:
# Add error for numbers in word or guess
single_letters = [*word]
length = len(word)
print("The word is", + length, "characters long.")
player1 = 0
player2 = 0
while True:
    space = "_" * len(word)
    print(space)
    options = int(input("Do you want to guess the (1) whole word or just a (2) single letter? "))
    if options == 1:
        guess = input(str("What do you think the word is? "))
        guess.lower()
        if guess == word:
            print("You guessed the word!!!")
            player2 = player2 + 1
            break
    elif options == 2:
        guess = input(str("What letter might be in this word? "))
        if len(guess) > 1 or len(guess) < 1:
            print("Invalid guess")
        else:
            repetition = single_letters.count(guess)
            if repetition > 0:
                print("The letter", str(guess), "was in the word", int(repetition), "times!!!")
                place = single_letters.index(guess)
                print(place + 1)
            else:
                print("That letter isn't in the word.")
