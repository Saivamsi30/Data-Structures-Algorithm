def merge(arr1,arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    arr = []

    while (i<len1) and (j<len2):
        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i += 1

        else:
            arr.append(arr2[j])
            j += 1

    while (i<len1):
        arr.append(arr1[i])
        i += 1

    while (j<len2):
        arr.append(arr2[j])
        j += 1

    return arr

# arr1 = [1,2,3,4]
# arr2 = [5,6,7,8]
# print(merge(arr1,arr2))

user_input_1 = input("Enter the Values: ")
user_input_2 = input("Enter the Values: ")

arr1 = list(map(int,user_input_1.split()))
arr2 = list(map(int,user_input_2.split()))

print(merge(arr1,arr2))


