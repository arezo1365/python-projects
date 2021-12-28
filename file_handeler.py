'''The admin enters the list of courses in a csv file and the student sees
    them based on his / her major after entering.Three courses are defined here'''


import csv
import os
import pandas as pd
import product



class File_handeler():

    def __init__(self, path):
        self.path = path

    def read(self):
        if os.path.exists(self.path):
            with open(self.path, 'a') as myfile:
                # reader = csv.DictReader(myfile)
                # # return list(reader)
                reader = pd.read_csv(myfile)
                print(reader.loc[:, ['name_students']])

        else:
            return "path is incorrect"

    def write(self, content):
        try:
            with open(self.path, 'w', newline='') as csvfile:
                fieldnames = ['name_students', 'Name_course', 'professor_name', 'Number_units', 'Capacity']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if len(open(self.path).readlines()) == 0:
                    writer.writeheader()
                for i in content:
                    writer.writerow(i)

        except Exception as ex:
            print(ex)
        return

f1 = File_handeler("task2.csv")
# print(f1.write([{'name_students':'arezo','Name_course':'adabiat','professor_name':'mohammadi','Number_units':2,'Capacity':50},
#                 {'name_students':'azadeh','Name_course':'zaban','professor_name':'asghari','Number_units':3,'Capacity':45},
#                 {'name_students':'nastaran','Name_course':'riyazi','professor_name':'mirzaee','Number_units':4,'Capacity':30}]))
print(f1.read())
print(f1.write(content='row'))
