# Missing Number

def missingnum(nums):
    n = len(nums)
    Tsum = (n*(n+1)//2)
    actual_sum = sum(nums)
    return Tsum - actual_sum

nums = [3,0,1 ]
print(missingnum(nums))