import openpyxl

# ---------- Step One ----------

# wb = openpyxl.load_workbook("octobre.xlsx")

# print(wb.sheetnames)

# # sheet = wb['Feuil1'] # sheet = wb[wb.sheetnames[0]]
# sheet = wb.active
#
# # cell = sheet['A1']
#
# # row = 2
# # for row in range(2, 7):
# #     cell = sheet.cell(row, column=2)
# #     print(cell.value)
#
# print(sheet.max_row)
# print(sheet.max_column)

# ---------- Step Two ----------
wb1 = openpyxl.load_workbook("octobre.xlsx", data_only=True)
wb2 = openpyxl.load_workbook("novembre.xlsx", data_only=True)
wb3 = openpyxl.load_workbook("decembre.xlsx", data_only=True)

# {"Pommes": (760, 660, 900) }

def add_data_from_wb(workbook, dictionnary):
    sheet = workbook.active
    for row in range(2,sheet.max_row):
        article_name = sheet.cell(row,1).value
        if not article_name:
            break
        total_sales = sheet.cell(row,4).value
        if dictionnary.get(article_name):
            dictionnary[article_name].append(total_sales)
        else:
            dictionnary[article_name] = [total_sales]

data = {}
add_data_from_wb(wb1, data)
add_data_from_wb(wb2, data)
add_data_from_wb(wb3, data)

print(data)