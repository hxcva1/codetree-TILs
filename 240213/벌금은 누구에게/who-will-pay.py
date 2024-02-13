n, m, k = tuple(map(int, input().split()))

arr = [0] * (n+1)
flag = False
for _ in range(m):
    num = int(input())
    arr[num] += 1
    if arr[num] == k:
        print(num)
        flag = True
if flag == False:
    print(-1)