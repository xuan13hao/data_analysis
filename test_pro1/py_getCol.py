'''Test GetCsvColumn'''
import pandas as pd
from GetCsvColumn import CsvFile,EXCLUDE
import csv
csvfilename = '../../Fam300_csv.csv'
#csvfile = CsvFile(csvfilename)
#f=open(csvfilename,'rb')
#reader=csv.DictReader(f)
#csvfiletest = file('csvtest1.csv', 'wb')
#writer = csv.writer(csvfiletest)
# example 1: get a column by its header
#col= csvfile.get_column('POS')
#ior i in df:
    #print(df[df["POS"].str.contains('Z')])
#for row in col:
#    print row
"""
with open(csvfilename,'rb') as csvfile:
    reader = csv.reader(csvfile)
    for i,rows in enumerate(reader):
        if i == 2:
            row = rows
print row
"""
csvfile = file(csvfilename,'rb')
reader = csv.DictReader(csvfile)
for row in reader:
        if row['POS']=='14464':
            print row


# example 2: get a column filtered by another column
#print 'example 2:', csvfile.get_column('Name', Gender='M')

# example 3: get a column filtered by other columns
#print 'example 3:', csvfile.get_column('Name', Gender='M', Age=9)

#example 4: exclusive filters
#print 'example 4:', csvfile.get_column('POS', POS=EXCLUDE('POS'))

# example 5: get a column filtered by other column with multi-criteria
#print 'example 5:', csvfile.get_column('Name', Age=[8, 9, 13])

# example 6: get a column exclusively filtered by other column with multi-criteria
#print 'example 6:', csvfile.get_column('Name', Age=EXCLUDE([8, 9, 13]))

# example 7: get multiple columns for unpacking
#no, start = csvfile.get_column('POS', 'start')
#print 'example 7:', no, start
