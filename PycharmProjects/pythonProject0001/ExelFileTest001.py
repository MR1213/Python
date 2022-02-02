import csv
import sys
args = sys.argv
input_csv_file = args[1]
x = 0
length = len(args)

target_column_name = 'Spent'

if length >= 3:
    target_column_name = args[2]

with open(input_csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = x + float(row[target_column_name])
#numbers = 'Spent'
min_number = min(numbers)
print(min_number)
print("Total: $" + str(x))