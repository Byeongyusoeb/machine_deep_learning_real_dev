'''
Delvelopment environment
 - Ubuntu with below packages
    * Openpyxl
'''

import openpyxl

workbook = openpyxl.Workbook()

sheet = workbook.active # Call active sheet (Usually the first sheet)

sheet['A1'] = 'Test file'
sheet['A2'] = 'wattup'
sheet.merge_cells("A1:C1")
sheet['A1'].font = openpyxl.styles.Font(size = 20, color='FF0000')

workbook.save("./data/newFile.xlsx")


'''
There are lots of options about openpyxl, so if you need to get it more then google it by python3 openpyxl
'''