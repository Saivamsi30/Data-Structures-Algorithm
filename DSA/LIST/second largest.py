def greater(l):
    x = l[0]
    for i in l:
        if i > x:
            x = i

    return x
    

l = [2,3,4,5,6,7,8,990]
print(greater(l))