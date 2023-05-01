import os

word = input(str("What is the word? "))
word = word.lower()
used_letters = set()

# To clear screen
os.system('cls')

def printWord(word, used_letters, health):
    os.system('cls')
    print(health)
    tmp = ""
    for i in word:
        tmp += i
    print(tmp)
    print(f"Used letters: {used_letters}")

def check_win(word, guessed_letters):
    for i in range(len(word)):
        if word[i] != guessed_letters[i]:
            return False
    return True

guessed_letters = "_" * len(word)
guessed_letters = [*guessed_letters]

length = len(word)
print("The word is", + length, "characters long.")
player1 = 0
player2 = 0

health_0 ='''
      _______
     |/      |
     |
     |
     |
     |
     |
    _|___
'''

health_1 ='''
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___
'''

health_2 ='''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
    _|___
'''
health_3 ='''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |
     |
    _|___
'''
health_4 ='''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
    _|___
'''
health_5 ='''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
    _|___
'''
health_6 ='''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
'''

healths = [health_0, health_1, health_2, health_3, health_4, health_5, health_6]

number_incorrect_letters = 0

while True:
    printWord(guessed_letters, used_letters, healths[number_incorrect_letters])
    if check_win(guessed_letters, word):
        print("You guessed the word!!!")
        player2 = player2 + 1
        break

    print(" ")
    guess = input(str("What letter might be in this word? "))
    guess = guess.lower()
    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    if len(guess) > 1  and not guess.isalpha() or len(guess) < 1:
        print("Invalid guess")
    elif len(guess) == word:
        if guess == word:
            print("You guessed the word!!!")
            break
        else:
            print("That isn't the word.")
            number_incorrect_letters += 1
    elif len(guess) > 1:
        print("Invalid guess")
        number_incorrect_letters += 1
    else:
        used_letters.add(guess)
        if guess in word:
            for i, c in enumerate(word):
                if c == guess:
                    guessed_letters[i] = c
        else:
            print("That letter isn't in the word.")
            number_incorrect_letters += 1
            
            
print("The word was ", word )
