def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    #Alphabetical Sorting function



filename = "C:/Users/maxsu/OneDrive/Desktop/PythonTestingFileReaders/ArchiTextFileTest1.txt"  #File with unsorted data

with open(filename) as file:
    lines = file.readlines()  #reads 1st line of file

list2 = []    # creates empty list

name = ""
href = ""

index = 0
for line in lines:   #loop that splits odd and even rows then combines the 2 into 1 tuple
    if index % 2 == 0:
        name = line
    else:
        href = line
        list2 += [(name, href)]

    index += 1

list2 = list(set(list2))    #adds new data to list

bubbleSort(list2)  #alphabeticaly sorts tuples individualy

MyFile = open('C:/Users/maxsu/OneDrive/Desktop/PythonTestingFileReaders/ArchiTextFileEdit5.txt', 'w')  #New file that will be sorted
for element in list2:   #writes tuples into file line by line
    MyFile.write(element[0])
    MyFile.write(element[1])

MyFile.close() # closes file