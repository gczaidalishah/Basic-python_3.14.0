# class A:
#     var1 = "Hello"

# class B:
#     var2 = "World"

# class C(A, B):
#     var3 = "!"
# c1 = C()
# print(c1.var1)
# print(c1.var2)
# print(c1.var3)

class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start_engine():
        print("Engine started")
    @staticmethod
    def stop_engine():
        print("Engine stopped")

class toyota(car):   #inheritane where toyata inherit the properties and methods of car class
    def __init__(self, name,type):
        self.name = name
        super().__init__(type)  #super() is used to call the __init__ method of the parent class (car).
    

car1=toyota("corolla","electric")
print(car1.type) 
print(car1.name) 
