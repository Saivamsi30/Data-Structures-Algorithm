# def reverse(num):
#     rev = 0
#     temp = num
#     while temp != 0:
#         id = temp % 10
#         rev = rev * 10 + id
#         temp = temp//10
#     return rev

# num = 123456
# print(reverse(num))
        

# def character(str):
#     return len(str.replace(" ",""))

# str = "Sai Vamsi kodavati"
# print(character(str))



# def range(n):
#     len1 = len(n)
#     sum = n*(n+1)/2



def fibonacci(n):
    fib_series = [0,1]
    for i in range(2,n):
        next_num = fib_series[i-1]+fib_series[i-2]
        fib_series.append(next_num)
    return fib_series


n = 4
print(fibonacci(n))




def bitwise(input1,input2):
    return input1|input2

input1 = 5
input2 = 9
print(bitwise(input1,input2))