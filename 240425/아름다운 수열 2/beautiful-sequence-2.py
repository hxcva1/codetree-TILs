n, m = tuple(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

visit = [0] * 101
for elem in b:
    visit[elem] += 1

cnt = 0
for i in range(n-len(b)+1):
    tmp = visit[:]
    c = True
    for j in range(i, i+m):
        if tmp[a[j]] == 0:
            c = False
            break;
        else:
            tmp[a[j]] -= 1
    if c:
        cnt += 1
print(cnt)