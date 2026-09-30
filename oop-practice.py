# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod #static method is a method that belongs to the class rather than an instance of the class.
#     #It can be called on the class itself, rather than on an instance of the class. 
#     # Static methods do not have access to the instance (self) or class (cls) variables.
#     def hello():
#         print("hello")
#     def get_average(self):
#         sum=0
#         for mark in self.marks:
#             sum+=mark
#         return sum/len(self.marks)

# s1=student("zaid ali",[45,50,60])
# s1.hello()
# print("Average marks of zaid in 3 subjects:",s1.get_average())

class account:
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number
    def debit(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount

    def credit(self,amount):
        self.balance+=amount
        print("RS.",amount,"credited")
        print("Current balance:",self.get_balance())
    
    def get_balance(self):
        return self.balance

account1=account(300,"03429832401")
print("Account number:",account1.account_number)
print("Balance:",account1.balance)
account1.debit(150)
print("Balance after debit:",account1.get_balance())
account1.credit(30000)
account1.debit(5000)
print("Balance after debit:",account1.get_balance())