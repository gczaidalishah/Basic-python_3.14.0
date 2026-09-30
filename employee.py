class Employee:
    def __init__(self, role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def details(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
class engineer(Employee):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("AI engineer","software development","80,000")
engg=engineer("bill gates", 65)
engg.details()

