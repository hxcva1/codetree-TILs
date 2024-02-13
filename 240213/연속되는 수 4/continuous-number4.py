n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

cnt = 0
ret = 0
for i in range(n):
    if i == 0 or arr[i] <= arr[i-1] :
        cnt = 1
    else:
        cnt += 1
    ret = max(cnt, ret)
print(ret)