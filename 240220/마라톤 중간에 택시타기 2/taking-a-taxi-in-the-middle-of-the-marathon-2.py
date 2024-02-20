import sys

n = int(input())

arr = []
for _ in range(n):
    x, y = tuple(map(int, input().split()))
    arr.append((x,y))
ret = sys.maxsize
for i in range(1,n-1):
    dist = 0
    cx, cy = arr[0][0], arr[0][1]
    for j in range(1,n):
        if j == i:
            continue
        dist += abs(cx-arr[j][0]) + abs(cy-arr[j][1])
        cx, cy = arr[j][0], arr[j][1]
    ret = min(ret,dist)
print(ret)