n = int(input())


arr = [0] * 200001
white = [0] * 200001
black = [0] * 200001

now = 100000
for _ in range(n):
    x, direction = tuple(input().split())
    if direction == "R":
        for i in range(int(x)):
            arr[now] = 1
            black[now] += 1
            now += 1
        now -= 1
    else:
        for i in range(int(x)):
            arr[now] = -1
            white[now] += 1
            now -= 1
        now += 1

w = b = g = 0
for i in range(200001):
    if white[i] >= 2 and black[i] >= 2:
        g += 1
        continue;
    if arr[i] > 0:
        b += 1
    if arr[i] < 0:
        w += 1
print(w, b, g)