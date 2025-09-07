def getsmall(l):
    x = 10
    for i in l:
        if i < x:
           print(i)
           i +=1


l = [10,2,3,9,34,54]
print(getsmall(l))
