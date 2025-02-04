def unique(kon):
    k=[]
    for i in kon:
        if kon.count(i)==1:
            k.append(i)
    return k
bankai=input().split()
print(*unique(bankai))