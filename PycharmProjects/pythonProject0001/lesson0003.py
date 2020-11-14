while 1:

    i = float(input("What do you want to check: "))
    if i * 10 > 25:
        print("Greater")
    elif i * 10 == 25:
        print("equal to")
        break
    else:
        print("less than")