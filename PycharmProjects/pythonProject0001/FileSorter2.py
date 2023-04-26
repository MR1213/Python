def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


name_url = []
fileObject = open("C:/Users/maxsu/OneDrive/Desktop/PythonTestingFileReaders/ArchiTextFileTest1.txt", "r")   #add file with name and location
data = fileObject.readlines()
n = len(data)
for i in range(n):
    data[i] = data[i].strip()
print(data)
bubbleSort(data)
print(data)
MyFile = open('C:/Users/maxsu/OneDrive/Desktop/PythonTestingFileReaders/ArchiTextFileEdit1.txt', 'w')    #add new file with name and correct location
for element in data:
    MyFile.write(element + "\n")
MyFile.close()
