# def redup(arr, n):
#     if n == 0:
#         return 0
    
#     res = 1
#     for i in range(1, n):
#         if arr[res - 1] != arr[i]:
#             arr[res] = arr[i]
#             res += 1
            
#     return res

# arr = [1, 1, 2, 2, 3, 4, 4, 5]
# n = len(arr)
# new_length = redup(arr, n)
# unique_elements = arr[:new_length]
# print(unique_elements) 

# def redup(n):
#     empty = []
#     for i in n:
#         if i not in empty:
#             empty.append(i)
        
#     return empty

# n = [10,20,20,30,40,50,50,50,60]
# print(redup(n))


def redup(arr,n):
    if n == 0:
        return False

    res = 1
    for i in range(1,n):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res += 1
    return res

user_input = input("Enter the Values: ")
arr = list(map(int,user_input.split()))
n = len(arr)


new_length = redup(arr,n)
unique_elements = arr[:new_length]
print(unique_elements)


# def redup(arr, n):
#     if n == 0:
#         return False  # Handle empty array case
#     res = 1  # Pointer for the next unique element
#     for i in range(1, n):
#         if arr[res - 1] != arr[i]:
#             arr[res] = arr[i]  # Place the new unique element at the res position
#             res += 1  # Move the res pointer forward
#     return res  # Return the number of unique elements

# # Get user input for the array
# user_input = input("Enter the values: ")
# arr = list(map(int, user_input.split()))
# n = len(arr)

# # Remove duplicates and get the new length
# new_length = redup(arr, n)

# # Extract and print the unique elements
# unique_elements = arr[:new_length]
# print("Unique elements:", unique_elements)





