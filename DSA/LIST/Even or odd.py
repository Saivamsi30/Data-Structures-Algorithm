# a = [10,20,31,32,11]
# for i in a:
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# def eve(n):
#     for i in range(n):
#         if n%2 == 0:
#             return True
#         else:
#             return False
        
# n = 10       
# print(eve(n))


def even_odd(n):
      if n%2 == 0:
          print(f"{n} is even number")
      else:
          print(f"{n} is odd number")

n = int(input("Enter the values:"))

even_odd(n)

