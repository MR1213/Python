import random
import webbrowser
import time

chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"


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

print("I hope you are sitting down right now: ")
print("loading...\n")
time.sleep(5)
print("loading...\n")
time.sleep(5)
print("Failed to load...\n")
time.sleep(5)
webbrowser.get(chrome).open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")