n = int(input())

def func(n):
    if n == 1:
        return 1
    return func(n-1) + n

print(func(n))