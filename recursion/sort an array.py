def recursive_sort(arr):
    if len(arr) <= 1:
        return arr
    
    last = arr[-1]
    arr = arr[:-1]
    arr = recursive_sort(arr)
    return insert_in_sorted(arr,last)

def insert_in_sorted(arr,value):
    if len(arr) == 0 or arr[-1] <= value:
        arr.append(value)
        return arr
    
    last = arr[-1]
    arr = arr[:-1]
    arr = insert_in_sorted(arr,value)

    arr.append(last)
    return arr

arr = [2,5,3,7,6]
print(arr)
sorted_arr = recursive_sort(arr)
print(sorted_arr)
