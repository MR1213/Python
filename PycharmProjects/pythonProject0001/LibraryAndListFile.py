def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


fileObject = open("C:\\Users\\maxsu\\OneDrive\\Documents\\NAMES.txt", "r")
data = fileObject.readlines()
n = len(data)
for i in range(n - 1):
    data[i] = data[i].strip()

print(data)
bubbleSort(data)
print(data)

MyFile = open('C:\\Users\\maxsu\\OneDrive\\Documents\\NAMESsorted.txt', 'w')
for element in data:
    MyFile.write(element + "\n")
MyFile.close()
