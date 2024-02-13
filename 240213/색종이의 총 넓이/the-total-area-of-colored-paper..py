n = int(input())

arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]

for _ in range(n):
    x1, y1 = tuple(map(int, input().split()))
    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            arr[i+100][j+100] = 1
ret = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            ret += 1
print(ret)