n = int(input())

arr = [
    int(input())
    for _ in range(n)
]
aver = sum(arr) // len(arr)

ans = 0
for elem in arr:
    ans += abs(aver - elem)
print(ans // 2)