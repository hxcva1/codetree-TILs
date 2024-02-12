n = list(input())

ret = 0
for elem in n:
    ret = ret * 2 + int(elem)
ret *= 17

def f(n):
    if n < 2:
        print(n%2, end='')
        return
    f(n//2)
    print(n%2,end='')
f(ret)