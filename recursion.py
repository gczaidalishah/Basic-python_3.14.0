# def show(n):
#     if (n == 6):
#         return
#     print(n)
#     show(n+1)
# show(1)

# def natural_sum(n):
#     if (n == 1):
#         return 1
#     return n + natural_sum(n-1)
# sum=natural_sum(5)
# print(sum)

# def list_sum(my_list, n):
#     if (n == 0):
#         return 0
#     return my_list[n-1] + list_sum(my_list, n-1)
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
def list_sum(list, idx=0):
    if (idx == len(list)):
        print(list[idx])
        list_sum(list,idx+1)

num=[1,2,3,4,5]
list_sum(num)