import csv
import os

file_name = 'fa.csv'
fake_data = [[1, 2, 3, 4, 5, 4444, 6, 67], [1, 2, 3, 4, 5, 4444, 6, 67],
             [1, 2, 3, 4, 5, 4444, 6, 67], [1, 2, 3, 4, 5, 4444, 6, 67]]
headers = ['DataA', 'DataB', 'DataC', 'DataD']

if os.path.isfile(file_name):
  with open(file_name, 'a', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    for datum in fake_data:
      writer.writerow(datum)
else:
  with open(file_name, 'w', encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    for datum in fake_data:
      writer.writerow(datum)