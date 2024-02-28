n = int(input())

arr = list(map(int, input().split()))

cnt = 0
for i in range(1,n+1):
    for j in range(n-i+1):
        tmp = []
        for k in range(j, j+i):
            tmp.append(float(arr[k]))
        if (sum(tmp) / i) in tmp:
            cnt += 1
print(cnt)