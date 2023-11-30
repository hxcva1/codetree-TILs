a = input().split()
a = list(map(int, a))

if a[0] > a[1] :
    print(a[0]*a[1])
else :
    print(a[1]//a[0])