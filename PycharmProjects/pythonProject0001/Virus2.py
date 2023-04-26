import random
import webbrowser
import time

chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
# Basicaly it WILL RickRoll you no matter what

def virus():
    for x in range(4):
        print("loading...\n")
        y = random.randint(1, 3)
    if y == 3:
        print("Failed to load...\n")
        print("Trying again...\n")
        print("Successfully loaded: \n")

chatbot_name = "Helper"
creation_year = 2022
creator = "Maksym_G"
chatbot_version = "Latest_Release_1.18"

virus()

print("Hey there, It seems you need help")
print("My name is: " + chatbot_name)

maths1 = int(input("Give me a random number, GO!"))
maths2 = int(input("Give me a second random number, GO!"))

answer1 = maths1 + maths2
answer2 = maths1 - maths2
answer3 = maths1 * maths2
answer4 = maths1 / maths2
answer5 = maths1 ** maths2

print(maths1, "+", maths2, "=", answer1)
time.sleep(random.randint(1,2))
print(maths1, "-", maths2, "=", answer2)
time.sleep(random.randint(1,2))
print(maths1, "*", maths2, "=", answer3)
time.sleep(random.randint(1,2))
print(maths1, "/", maths2, "=", answer4)
time.sleep(random.randint(1,2))
print(maths1, "**", maths2, "=", answer5)

time.sleep(random.randint(1,5))
print("loading...\n")
time.sleep(random.randint(1,5))
print("loading...\n")
time.sleep(random.randint(1,5))
print("Failed to load...\n")
webbrowser.get(chrome).open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
