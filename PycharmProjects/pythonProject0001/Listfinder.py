def checkIfMatch(elem):
    if len(elem) == 5:
        return True;
    else:
        return False;
x = str(input("What do you want to search"))
def main():
    listOfStrings = ['Hi', 'hello', 'at', 'this', 'there', 'from']
    print(listOfStrings)
    if x in listOfStrings:

        print("Yes" + x + "found in List")
    result = any(len(elem) == 5 for elem in listOfStrings)

    if result:
        print("Yes, string element with size 5 found")
    result = any(checkIfMatch for elem in listOfStrings)
if __name__ == '__main__':
    main()