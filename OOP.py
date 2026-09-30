# class car:
#     def __init__(self): #constructor is a special method which is automatically called when we create an object of the class
#         self.color="black"
#         self.brand="BMW"
#         self.type="M6 coupe"
#         self.engine="2000cc"
        
    
# c1=car()
# print(c1.color)
# print(c1.brand)
# print(c1.type)
# print(c1.engine)


class student:
    college="uet peshawar"
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
        print("adding new student in database")
s1=student("zaid ali",20,101)
print("name:",s1.name)
print("age:",s1.age)
print("rollno:",s1.rollno)
s2=student("shayan shah",22,102)
print("name:",s2.name)
print("age:",s2.age)
print("rollno:",s2.rollno)
print(student.college)