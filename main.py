# Skip the header of a file with CSV Reader in Python

import csv

with open('employees.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader)

    for row in csv_reader:
        print(row)
