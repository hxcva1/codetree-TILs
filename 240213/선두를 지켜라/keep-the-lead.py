n, m = map(int, input().split())

a = [0] * 1000001
b = [0] * 1000001
time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a[time_a] = a[time_a - 1] + v
        time_a += 1

time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b[time_b] = b[time_b - 1] + v 
        time_b += 1
now = 0
ret = 0
for i in range(1, time_a):
    if now == 1:
        if a[i] < b[i]:
            now = 2
            ret += 1
    elif now == 2:
        if a[i] > b[i]:
            now = 1
            ret += 1
    else:
        if a[i] < b[i]:
            now = 2
        if a[i] > b[i]:
            now = 1
print(ret)