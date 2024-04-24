import sys

MAX_NUM = 100

n = int(input())
if n == 1:
    print(0)
    sys.exit()
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    l, a = input().split()
    l = int(l)
    if a == "G":
        arr[l] = 1
    else:
        arr[l] = -1

ans = 0
for i in range(MAX_NUM + 1):
    if arr[i] != 0:
        cnt_g = 0
        cnt_h = 0
        if arr[i] == 1:
            cnt_g += 1
        else:
            cnt_h += 1
        for j in range(i+1,MAX_NUM + 1):
            if arr[j] != 0:
                if arr[j] == 1:
                    cnt_g += 1
                if arr[j] == -1:
                    cnt_h += 1
                if cnt_g == cnt_h or cnt_g == 0 or cnt_h == 0:
                    ans = max(ans, j-i)
print(ans)