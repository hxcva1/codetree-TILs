import sys

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
ret = sys.maxsize
for i in range(n):
    dist = 0
    for j in range(n):
        dist += arr[(i+j)%n] * j
    ret = min(ret,dist)
print(ret)