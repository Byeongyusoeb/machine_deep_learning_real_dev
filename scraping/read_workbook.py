'''
Delvelopment environment
 - Ubuntu with below packages
    * Openpyxl
'''

import openpyxl

book = openpyxl.load_workbook('./data/104102_population.xlsx')

name_list = book.sheetnames

sheet = book[name_list[0]]

for row in sheet.rows:
    for data in row:
        print(data.value, end = " ")
    print("", end = "\n")