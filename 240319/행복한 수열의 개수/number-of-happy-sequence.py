n , m = tuple(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ret = 0
for i in range(n):
    cnt = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            cnt += 1
            if cnt == m:
                ret += 1
                break
        else:
            cnt = 1

for i in range(n):
    cnt = 1
    for j in range(n-1):
        if arr[j][i] == arr[j+1][i]:
            cnt += 1
            if cnt == m:
                ret += 1
                break
        else:
            cnt = 1

print(ret)