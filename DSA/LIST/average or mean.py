# def average(n):
#     sum = 0
#     for i in n:
#         sum = sum+i
#         l = len(n)
#     return sum/l

# n = [10,20,30,40]
# print(average(n))


# def average(n):
#     sum = 0
#     for i in n:
#         sum = sum+i
#     l = len(n)
#     return sum/l

# user_input = input("Enter the values: ")

# n = list(map(int,user_input.split()))

# print(average(n))


def average(n):
    sum = 0
    for i in n:
        sum = sum + i
    l = len(n)
    return sum/l

user_input = input()
n = list(map(float, user_input.split()))

print(average(n))
                       









