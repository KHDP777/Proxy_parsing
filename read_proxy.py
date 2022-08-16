import csv

with open('main.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)

