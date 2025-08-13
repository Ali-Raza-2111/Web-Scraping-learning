from openpyxl import load_workbook
from openpyxl.styles import Font
wb = load_workbook('Report.xlsx')
sheet = wb['Report']
sheet['A1'] = 'Sales Report'
sheet['A2'] = 'July'

sheet['A1'].font = Font('Arial',bold=True, size=20)
sheet['A2'].font = Font('Arial',bold=True, size=10)

wb.save('Report_July.xlsx')