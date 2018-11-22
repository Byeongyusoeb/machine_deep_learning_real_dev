'''
CSV is acronym of Comma-Seperated Values

CSV rules
1. One data in one line, seperate values by comma
2. First line could be used as a header
'''

import csv, codecs

filename = "./data/csv_test_data.csv"

file = codecs.open(filename, 'r', 'euc_kr')

reader = csv.reader(file, delimiter=",")

for cells in reader:
    for cell in cells:
        print(cell)