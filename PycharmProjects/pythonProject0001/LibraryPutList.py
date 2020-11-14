def bubbleSort(arr):   #Bubble sort function
    n = len(arr)    #Bubble sort function
    for i in range(n - 1):  #Bubble sort function
        for j in range(0, n - i - 1):    #Bubble sort function
            if arr[j] > arr[j + 1]:    #Bubble sort function
                arr[j], arr[j + 1] = arr[j + 1], arr[j]    #Bubble sort function


add = input(str("Please enter a name:"))    #Adds names to file
fileObject = open("C:\\Users\\maxsu\\OneDrive\\Documents\\NAMES.txt", "r")  #opens file and reads it
data = fileObject.readlines()#reads lines in file 
data += [add]   #Adds input
n = len(data)   #Finds numeber of lines in file
for i in range(n - 1):   #Finds numeber of lines in file
    data[i] = data[i].strip()    #Finds numeber of lines in file
print(data) #Prints old unsorted file
bubbleSort(data)    #Sorts old unsorted file
print(data) #Prints new sorted file
MyFile = open('C:\\Users\\maxsu\\OneDrive\\Documents\\NAMESsorted.txt', 'w')    #Writes in new sorted file
for element in data:    #Formats the Names with "Enter" after each one
    MyFile.write(element + "\n")    #Formats the Names with "Enter" after each one
MyFile.close()  #Closes Sorted File
