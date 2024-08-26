import openpyxl

wb = openpyxl.load_workbook("octobre.xlsx")
print(wb.sheetnames)

# sheet = wb['Feuil1'] # sheet = wb[wb.sheetnames[0]]
sheet = wb.active

# cell = sheet['A1']

# row = 2
# for row in range(2, 7):
#     cell = sheet.cell(row, column=2)
#     print(cell.value)

print(sheet.max_row)
print(sheet.max_column)
