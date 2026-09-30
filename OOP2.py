# class Student:
#     def __init__(self, name):
#         self.name = name

# student1 = Student("zaid ali shah")
# print(student1.name)
# del student1  # delete the object. del is a keyword
# print(student1.name)


# class account:
#     def __init__(self, account_number, account_password):
#         self.account_number = account_number
#         self.__account_password = account_password # private variable, it cannot be accessed outside the class. 
#     def reset_password(self):
#         print(self.__account_password)
        

# account1 = account("123456789", "password123")
# print(account1.account_number)
# print(account1.__account_password)  # This will raise an AttributeError because __account_password is a private variable.
# print(account1.reset_password())  #access the private variable because it is being accessed within the class method.

class car:
    @staticmethod
    def start_engine():
        print("Engine started")
    @staticmethod
    def stop_engine():
        print("Engine stopped")

class toyota(car):   #inheritane where toyata inherit the properties and methods of car class
    def __init__(self, brand):
        self.brand = brand
    

class honda(car):   #inheritane where honda inherit the properties and methods of car class
    def __init__(self, type):
        self.type = type
car1 = honda("diesel")
car1.start_engine()  #access the static method of the parent class
