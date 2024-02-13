n = int(input())

arr = [0] * 201
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a+100, b+100):
        arr[i] += 1
ret = 0
for i in range(201):
    ret = max(ret, arr[i])
print(ret)