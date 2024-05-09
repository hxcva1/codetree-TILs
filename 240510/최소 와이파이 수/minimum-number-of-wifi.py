N, M = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
i = 0
while i < N:
    if arr[i] == 0:
        i += 1
    else:
        cnt += 1
        i += 2*M + 1
print(cnt)