n = int(input())
arr = list(map(int, input().split()))

mx = max(arr)
cnt = 0
mx2 = arr[0]
for i in range(n):
    if (arr[i] == mx):
        cnt += 1
        if (cnt == 2):
            mx2 = mx
            break;
        continue
    if arr[i] > mx2 and mx2 < mx:
        mx2 = arr[i]
print(mx, mx2)