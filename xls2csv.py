#!/usr/bin/env python3

# Import xlrd
import xlrd
import sys
import csv

# Open a workbook and select a sheet
book = xlrd.open_workbook(sys.argv[1])
sheet = book.sheet_by_index(0)
csvWriter = csv.writer(open('.'.join([sys.argv[1],'csv']), 'w'), delimiter=',')
for i in range(sheet.nrows):
    csvWriter.writerow(sheet.row_values(i))
