"""

author: @endormi

Automated income tracker
Automatically adds to excel

"""

import xlsxwriter

wb = xlsxwriter.Workbook('filename.xlsx', {'strings_to_numbers': True})
wsb = wb.add_worksheet(name='Income')
bold = wb.add_format({'bold': True})

wsb.write('A1', 'Income', bold)
wsb.write('A2', 'Date:', bold)
wsb.write('B2', 'Type of income:', bold)
wsb.write('C2', 'Amount of income:', bold)
wsb.write('E2', 'Total:', bold)

currency_format = wb.add_format({'num_format': '€#,##0.00'})

wsb.write('A3', '01.01.2020')
wsb.write('B3', 'type1')
wsb.write('C3', '1000')
wsb.write('A4', '01.01.2020')
wsb.write('B4', 'type2')
wsb.write('C4', '1000')
wsb.write('A5', '01.01.2020')
wsb.write('B5', 'type2')
wsb.write('C5', '1000')
wsb.write('A6', '01.01.2020')
wsb.write('B6', 'type2')
wsb.write('C6', '1000')
wsb.write('A7', '01.01.2020')
wsb.write('B7', 'type2')
wsb.write('C7', '1000')
wsb.write_formula("E3", "=SUM(C3:C7)", currency_format)

wb.close()