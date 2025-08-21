def kthgrammar(n,k):
    if n == 1 or k == 1:
        return 0
    
    mid = 2**(n-1) // 2

    if k<= mid:
        return kthgrammar(n-1,k)
    else:
        return 1-kthgrammar(n-1,k-mid)
    
n = 5
k = 10
print(kthgrammar(n,k))