n, m = tuple(map(int, input().split()))

n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))

idx = 0
flag = 0
for i in range(len(n1)):
    if n1[i] == n2[idx]:
        idx += 1
    else:
        idx = 0
    if idx == m:
        flag = 1
if flag:
    print("Yes")
else:
    print("No")