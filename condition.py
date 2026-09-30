# light= "blue"
# if(light == "red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("Get Ready")
# elif(light == "green"):
#     print("Go")
# else:
#     print("Invalid Color")

# student_marks = input("Enter your marks: ")
# if(student_marks >= 90):
#     print("Grade A")
# elif(student_marks >= 80 and student_marks < 90):
#     print("Grade B")
# elif(student_marks >= 70 and student_marks < 80):
#     print("Grade C")
# elif(student_marks >= 60 and student_marks < 70):
#     print("Grade D")
# else:
#     print("fail")
# number = int(input("Enter a number: "))
# if(number % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")
# a=10
# b=20
# c=30
# if(a > b and a > c):
#     print("A is the largest")
# elif(b > a and b > c):
#     print("B is the largest")
# else:
#     print("C is the largest")
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
d=int(input("enter fourth number: "))
if(a > b and a > c and a > d):
    print("A is the largest")
elif(b > a and b > c and b > d):
    print("B is the largest")
elif(c > a and c > b and c > d):
    print("C is the largest")
else:
    print("D is the largest")