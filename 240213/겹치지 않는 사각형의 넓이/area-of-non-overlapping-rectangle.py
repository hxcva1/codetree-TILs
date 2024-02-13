offset = 1000
arr = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

for _ in range(2):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i+offset][j+offset] = 1
x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i+offset][j+offset] = 0
ret = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            ret += 1
print(ret)