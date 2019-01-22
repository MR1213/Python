# finds all factors of a given number
num = int(input("Please choose a number to divide: "))
divisorList = []
for number in range(1,num+1):
    if num % number == 0:
        divisorList.append(number)
print(divisorList)