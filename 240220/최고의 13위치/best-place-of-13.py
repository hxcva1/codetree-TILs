n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
ret = 0
for i in range(n):
    for j in range(n-2):
        cnt = 0
        cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ret = max(ret, cnt)     
print(ret)