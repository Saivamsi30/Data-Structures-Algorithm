def leftrotate(l):
    n = len(l)
    x = l[0]
    for i in range(1,n):
        l[i-1] = l[i]

    l[n-1] = x

# l = [10,20,30,40,50]
# leftrotate(l)
# print(l)

user_input = input("Enter the Values: ")
l = list(map(int,user_input.split()))
leftrotate(l)
print(l)


