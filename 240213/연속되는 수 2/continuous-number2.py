n = int(input())

prev = -1
cnt = 0
ret = 0
for i in range(n):
    num = int(input())
    if num == 0 or num != prev:
        cnt = 1
        prev = num
        continue
    cnt += 1
    prev = num
    ret = max(cnt, ret)
print(ret)