# marks = [95, 98, 97]
# print(type(marks))
# print(marks[0])
# print(marks)
# student = ["John", 25, 3.5, "california"]
# print(student)
# student[1]=26
# student[3]="texas"
# print(student)
# print(student[:3])    #index slicing
# print(student[-4:-1]) #negative indexing

# list=[11,2,45,67,23]
# print(list.append(99))
# print(list.sort(reverse=True))
# print(list)

# user=input("Enter first movie name: ")
# user1=input("Enter second movie name: ")
# user2=input("Enter third movie name: ")
# movies=[]
# movies.append(user)
# movies.append(user1)
# movies.append(user2)
# print(movies)
list=[1,2,1,2,1,3]
copy_list=list.copy()
copy_list.reverse()
if(list==copy_list):
    print("Palindrome")
else:
    print("Not a Palindrome")