# def cal_sum(a, b):
#     sum_result = a + b
#     print("Sum:", sum_result)
#     return sum_result
# cal_sum(3, 5)

# def cal_sum(a, b,c):
#     average = (a + b + c)/3
#     print("averageof three numbers:", average)
#     return average
# cal_sum(3, 5,7) 

# def length_of_list(list1):
#     length = len(list1)
#     print("Length of the list:", length)
#     return length
# length_of_list([10, 20, 30, 40])

# def cal_factorial(n):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     print("Factorial of", n, "is:", factorial)
#     return factorial
# cal_factorial(5)
# cal_factorial(10) #calling function again with different argument

# def converter(PKR):
#     USD = PKR / 280
#     print("Amount in USD:", USD)
# converter(1400000)

def number_check(num):
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
        number_check(input("Enter a number: "))  
number_check()
