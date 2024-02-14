n, m = map(int, input().split())

a = [0] * 1000001
b = [0] * 1000001
time_a = 1
for _ in range(n):
    t, d = input().split()
    for _ in range(int(t)):
        if d == "L":
            a[time_a] = a[time_a - 1] - 1
        else:
            a[time_a] = a[time_a - 1] + 1
        time_a += 1

time_b = 1
for _ in range(m):
    t, d = input().split()
    for _ in range(int(t)):
        if d == "L":
            b[time_b] = b[time_b - 1] - 1
        else:
            b[time_b] = b[time_b - 1] + 1
        time_b += 1
if time_a < time_b:
    while time_a != time_b:
        a[time_a] = a[time_a - 1]
        time_a += 1
else:
    while time_a != time_b:
        b[time_b] = b[time_b - 1]
        time_b += 1
ret = 0
for i in range(1, max(time_a,time_b)):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        ret += 1
print(ret)