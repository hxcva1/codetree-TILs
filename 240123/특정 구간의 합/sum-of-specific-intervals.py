n, m = map(int, input().split())

arr = list(map(int, input().split()))
for _ in range(m):
    a1, a2 = map(int, input().split())
    ret = 0
    for i in range(a1-1, a2):
        ret += arr[i]
    print(ret)