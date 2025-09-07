def calculate(r, unit, arr, n):
    if arr is None or n==0:
        return -1
    totalFoodRequired = r * unit
    foodTillNow = 0
    for house in range(n):
        foodTillNow += arr[house] 
        if foodTillNow >= totalFoodRequired:
            return house + 1
    return 0

r = int(input("Enter number of rats: "))
unit=int(input("Enter the value of units: "))
n=int(input("Number of elements in a array: "))
arr = list(map(int, input("List elements with sapce separated: ").split()))

print(calculate(r,unit,arr,n))


