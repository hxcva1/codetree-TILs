n = int(input())
offset = 100
arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for t in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            if t % 2 == 0:
                arr[i+offset][j+offset] = 0
            else:
                arr[i+offset][j+offset] = 1

ret = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            ret += 1
print(ret)