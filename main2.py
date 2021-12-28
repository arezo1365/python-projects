'''
1) The instructor enters the program and defines the information in the doors including the name of the course,
the name of the teacher, the number of units and the capacity.
2) The student enters the program and sees the list of courses that can be selected for his / her field.
3) The student chooses a number of subjects. The number of selected units must be more than 10 and less than 20.
4) With each student choice, the capacity of the relevant course decreases.
5) The student can see the list of selected courses and the total number of credits.
6) The person in charge of education can see the list of students and by selecting each student,
 he / she can see the selected courses and approve or reject them.'''



import user
import product
import file_handeler
while True:
    check = input("1)admin 2) student")
    if check == "1":
        username = input("Enter your username :")
        password = input("Enter your password :")
        code = input("Enter your code admin:")
        if user.login(username, password, code):
            menuAdmin = input("1)create_product 2)show_list_students,3)show_choice_student")
            if menuAdmin == "1":
                pro = product.get_create_product()
            elif menuAdmin == "2":
            elif menuAdmin == "3":
                pass
            else:
                print("Worng!")
    elif check == "2":
        username = input("Enter your username :")
        password = input("Enter your password :")
        code = input("Enter your code_student:")
        if user.login(username,password,code):
            menuStudent = input("1)read_courses 2)choice_courses")
            if menuStudent == "1":
                pro = product.get_create_product()
            elif menuStudent == "2":
                pass

            else:
                print("Wrong!")

