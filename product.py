def get_create_product():
    Name_Course = input("Enter Name_Course :")
    professor_name = input("Enter professor_name :")
    Number_units = int(input("Enter Number_units :"))
    Capacity = int(input("Enter Capacity:"))
    product = Product(Name_Course, professor_name, Number_units, Capacity)
    # return product
    print(product)


class Product:
    def __init__(self,Name_Course,professor_name,Number_units,Capacity):
        self.Name_Course=Name_Course
        self.professor_name=professor_name
        self.Number_units=Number_units
        self.Capacity=Capacity

    def __str__(self):
        return f"{self.__dict__}"
