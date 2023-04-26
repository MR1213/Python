import csv


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


lines = []
with open("C:/Users/maxsu/OneDrive/Desktop/PythonTestingFileReaders/ArchiTextFileTest1.txt", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    length = len(csvfile.readlines())
    print(length)
    # for line in csvfile:
    # inner_list = [elt.strip() for elt in line.split(',')]
    # list_of_lists.append(inner_list)
    for row in spamreader:
        print(', '.join(row))
        # for b in range(length):
        # if b % 2 == 1:

        # elif b % 2 == 0:

        # data[b] = data[b].strip()
        # lines = [data[b]]
        # print(lines)
        # print(data)

# bubbleSort(data)
# print(data)
# MyFile = open('C:/Users/maxsu/OneDrive/Desktop/PythonTestingFileReaders/ArchiTextFileEdit4.txt', 'w')  # Add all this
# for element in data:
# MyFile.write(element + "\n")
# MyFile.close()
