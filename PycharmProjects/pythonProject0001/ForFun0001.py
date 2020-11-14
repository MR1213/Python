import random
count = 0
n=int(input("what are the odds?"))

for x in range(n):
    y = random.randint(1, 5)
    #print(y)
    if y == 5:
        count=count+1
prcnt = (count/n)*100
print("5 had a chance of:")
print(str(prcnt)+"%")