n = int(input())


arr = [0] * 2001

now = 1000
for _ in range(n):
    x, direction = tuple(input().split())
    if direction == "R":
        for i in range(int(x)):
            arr[now] += 1
            now += 1
        now += 1
    else:
        for i in range(int(x)):
            arr[now] += 1
            now -= 1
        now -= 1
ret = 0
for i in range(2000):
    if arr[i] >= 2:
        ret += 1
print(ret)