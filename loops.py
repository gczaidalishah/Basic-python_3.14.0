# count=1
# while count <= 5:
#     print("zaid ali shah")
#     count += 1

# print(count)

# num=1
# while num <= 100:
#     print(num)
#     num += 1
# num=100
# while num >= 1:
#     print(num)
#     num -= 1

# n=int(input("Enter a number: "))
# i=1
# n*i
# while i <= 10:
#     print(n*i)
#     i += 1

nums=(1,2,3,4,5,6,7,8,9,10)
x=49
i=0

while i < len(nums):
    if (nums[i] == x):
        print("Found at index", i)
        break
    else:
        print("finding...")
    i += 1
# num=(1,2,3,4,5,6,7,8,9,10)
# for val in num:
#     print(val)
# nums= [1,2,3,4,5,6,7,8,9,10]
# x=5
# for i in range(len(nums)):
#     if nums[i] == x:
#         print("Found at index", i)
#         break
#     else:
#         print("finding...")
# for val in range(2,20,2): #range(start,stop,step)
#     print(val)
# for val in range(1,101):
#     print(val)
    
# for val in range(100,0,-1):
#     print(val)
# n=int(input("Enter a number: "))
# for i in range(1,11):
#     print(n*i)
# n=7
# sum=0
# while n > 0:
#     sum += n
#     n -= 1
# print("The sum is:", sum)
n=4
fact=1
for i in range(1,n+1):
    fact *= i
print("The factorial is:", fact)
