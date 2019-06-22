num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))
ans= num/check
if num % 4 == 0:
    print(num, "Is a multiple of 4, and is an even number")
elif num % 2 == 0:
    print(num, "Is an even number")
else:
    print(num, "Is an odd number")

if num % check == 0:
    print(num, "Divides evenly by", check)
    print(str(num) + " divided by " + str(check) + " is " + str(ans))
else:
    print(num, "Does not divide evenly by", check)