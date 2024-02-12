a, b = map(int, input().split())
n = input()

ret = 0
n = list(str(n))
for elem in n:
    ret = ret * a + int(elem)

def f(n, a):
    if n < a:
        print(n % a, end='')
        return
    f(n // a, a)
    print(n % a, end='')
f(ret, b)