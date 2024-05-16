n, m = map(int, input().split())
arr = list(map(int, input().split()))
d = {}

for elem in arr:
    if elem in d:
        d[elem] += 1
    else:
        d[elem] = 1
ques = list(map(int, input().split()))
for e in ques:
    if e in d:
        print(d[e], end=' ')
    else:
        print(0, end=' ')