# Comma Separated Values (CSV)
"""
SN,NAME,ADDRESS
1,John,BHK
"""

# Example-1
# Write Content
"""
import csv
import sys
filename = "D:/Python/PythonDjango-4/MyFiles/data3.csv"
heading_row = ['SN','NAME','ADDRESS']
data_row1 = [1, 'John', 'BHK']
data_row2 = [2, 'Jeena', 'LAT']
try:
    csv_file = open(filename, mode="w")
    writer = csv.writer(csv_file)
    writer.writerow(heading_row)
    writer.writerow(data_row1)
    writer.writerow(data_row2)
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del filename
    del heading_row
    del data_row1
    del data_row2
"""

# Example-2
# Reading rows from CSV
"""
import csv
import sys
filename = "D:/Python/PythonDjango-4/MyFiles/data3.csv"
try:
    csv_file = open(filename, mode="r")
    reader = csv.reader(csv_file)
    for row in reader:
        if(len(row)>0):
            print(', '.join(row))
except:
    print("Error : ", sys.exc_info()[1])
finally:
    del filename
"""