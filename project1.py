import csv
import os
import logging

'''
1) The instructor enters the program and defines the information in the doors including the name of the course, 
the name of the teacher, the number of units and the capacity.
2) The student enters the program and sees the list of courses that can be selected for his / her field.
3) The student chooses a number of subjects. The number of selected units must be more than 10 and less than 20.
4) With each student choice, the capacity of the relevant course decreases.
5) The student can see the list of selected courses and the total number of credits.
6) The person in charge of education can see the list of students and by selecting each student,
 he / she can see the selected courses and approve or reject them.'''


class File_users():
    def __init__(self,path1):
        self.path1=path1


    '''The admin enters the program, registers first, and in the next step, 
    logs out if he does not enter the username and password correctly.
    And all the information received from the admin is stored in the file'''

    def register_admin(self):

        with open(self.path1, mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")

            username = input("please enter username admin: ")
            password = input("please enter your password admin: ")

            for i in range(3):
                if password == 'admin':
                    writer.writerow([username, password])
                    print("Registration is succesful!")
                    return True

                else:
                    print("please try again.")
                    break


    def login_admin(self):

        username = input("please enter username: ")
        password = input("please enter your password: ")

        with open(self.path1, mode='r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row == [username, password]:
                    print("you are logged in!")
                    return True
                else:
                    break


    '''The student enters the program, registers first, and in the next step,
     logs out if he does not enter the username and password correctly.
     And all the information received from the student is stored in the file
     '''

    def register_student(self):

        with open(self.path1, mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")

            username = input("please enter username: ")
            password = input("please enter your password: ")
            password2 = input("please Re-type password: ")
            if password == password2:
                writer.writerow([username, password])
                print("Registration is succesful!")
                return True


            else:
                print("please try again.")


    def login_student(self):

        username = input("please enter username: ")
        password = input("please enter your password: ")

        with open(self.path1, mode='r') as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row == [username, password]:
                    print("you are logged in!")
                    return True
                else:
                    break




'''The admin enters the list of courses in a csv file and the student sees
    them based on his / her major after entering.Three courses are defined here'''

class File_process(File_users):

    def __init__(self, path):
        self.path = path

    def read(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as myfile:
                reader = csv.DictReader(myfile)
                return list(reader)
        else:
            return "path is incorrect"

    def write(self, content):
        try:
            with open(self.path, 'w', newline='') as csvfile:
                fieldnames = ['major', 'Name_course', 'professor_name', 'Number_units', 'Capacity']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if len(open(self.path).readlines()) == 0:
                    writer.writeheader()
                for i in content:
                    writer.writerow(i)
        except Exception as ex:
            print(ex)
        return


    '''After entering the program, he chooses his field.'''

    @classmethod
    def check_major(cls,major):
        pass

    '''The student chooses a number of subjects. The number of selected units must be more than 10 and less than 20.'''
    @classmethod
    def select_lessons(cls):
        pass

    '''The courses selected by the student are removed from the list.'''
    @classmethod
    def remove_select_lessons(cls):
        pass

    '''With each student choice, the capacity of the relevant course decreases.And the information is updated.'''
    @classmethod
    def update_capacity_lessons(cls):
        pass





f2=File_users("usres1.csv")
print(f2.register_admin())
print(f2.login_admin())


f1 = File_process("task2.csv")
print(f1.write([{'major':'a','Name_course':'adabiat','professor_name':'mohammadi','Number_units':2,'Capacity':50},
                {'major':'b','Name_course':'zaban','professor_name':'asghari','Number_units':3,'Capacity':45},
                {'major':'c','Name_course':'riyazi','professor_name':'mirzaee','Number_units':4,'Capacity':30}]))
print(f1.read())

f2=File_users("users2.csv")
print(f2.register_student())
print(f2.login_student())




