a = list(input())




def f(n):
    num = 0
    for i in range(len(n)):
        num = num * 2 + int(n[i])
    return num 

ret = 0
for i in range(len(a)):
    if a[i] == "1":
        a[i] = "0"
        ret = max(ret, f(a))
        a[i] = "1"
    else:
        a[i] = "1"
        ret = max(ret, f(a))
        a[i] = "0"
print(ret)