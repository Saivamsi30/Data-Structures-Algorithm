# ROTATE ARRAY BY 1

# def rotate(arr):
#     temp = arr[-1]
#     for i in range(len(arr) - 2,-1,-1):
#         arr[i+1]  =arr[i]
#     arr[0] = temp

# arr = [1,2,3,4,5]
# rotate(arr)
# print(arr)   

# ROTATE ARRAY BY K

def rotate(arr,k):
    n = len(arr)
    k = k%n
    arr[:] = arr[n-k:] + arr[:n-k]

arr = [1,2,3,4,5,6,7]
k = 3
rotate(arr,k)
print(arr)


    