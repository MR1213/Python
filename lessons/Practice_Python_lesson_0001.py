# def age (word):
#     100-age(word)=x
#     print(x)
#     age("50")
#name = input("Give me your name: ")
#print("Your name is " + name)
#age = input("Enter your age: ")
#print("Your age is " + age)
#age = int(age)
#str(2018-age + 100)

#print(str)

import datetime

now = datetime.datetime.now()

year = now.year

name = input('Please, enter your name: ')
age = int(input('How old are you {}? '.format(name)))
solution = (year - age) + 100
print('{0}, you will be 100 years old in year {1}'.format(name, solution))

print("Today: " + str(now))