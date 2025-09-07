def lcm(a,b):
    res = max(a,b)

    while True:
        if res % a == 0 and res % b == 0:
            return res
        
        res += 1
    return res

a = 4
b = 6
print(lcm(a,b))

# import math
# def lcm(a,b):
#     return abs(a*b)//math.gcd(a,b)

# a = 4
# b = 6
# print(lcm(a,b))

# import math
# def lcm(a,b):
#     return abs(a*b)//math.gcd(a,b)








