arr = list(map(int, input().split()))

cnt = 0
val_sum = 0
for elem in arr:
    if elem == 0:
        break
    if elem % 2 == 0:
        cnt += 1
        val_sum += elem
print(cnt, val_sum)