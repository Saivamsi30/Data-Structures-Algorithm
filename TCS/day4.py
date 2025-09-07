def large(arr,n):
    max = arr[0]
    for i in range(0,n):
        if (max < arr[i]):
            max = arr[i]
    return max
    
arr = [0,9,4,6,2.4]
n = 6
print(large(arr,n))