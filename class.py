# class Student:
#     def __init__(self, physics, chemistry, math):
#         self.physics = physics
#         self.chemistry = chemistry
#         self.math = math
   
   
#     @property
#     def percentage(self):
#         return str((self.physics + self.chemistry + self.math) / 3) + "%"
# student1 = Student(80, 90, 85)
# print(student1.percentage)

# student1.physics = 95
# print("percentage after correction:", student1.percentage)

# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def show(self):
#         print(self.real, "+", self.imag, "j")
#     def __add__(self, other):
#         real_part = self.real - other.real
#         imag_part = self.imag - other.imag
#         return complex(real_part, imag_part)

# c1 = complex(2, 3)
# c1.show()

# c2 = complex(4, 5)
# c2.show()
# c3 = c1 + c2
# c3.show()

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius **2 
    def perameter(self):
        return 2 * (22/7) * self.radius
c1 = circle(7)
print("Area of circle:", c1.area())
print("Perameter of circle:", c1.perameter())