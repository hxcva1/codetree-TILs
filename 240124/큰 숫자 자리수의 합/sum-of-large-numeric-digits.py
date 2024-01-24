arr = list(map(int, input().split()))

def f(n):
    if n < 10:
        return n
    return f(n // 10) + (n % 10)
tmp = 1
for i in range(3):
    tmp *= arr[i]
print(f(tmp))