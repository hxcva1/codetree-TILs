n, b = map(int, input().split())

def f(n, b):
    if n < b:
        print(n % b, end='')
        return
    f(n // b, b)
    print(n % b, end='')
f(n, b)