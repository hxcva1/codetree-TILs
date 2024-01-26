n = int(input())

arr = list(map(int, input().split()))

a = []
for i in range(n):
    a.append(arr[i])
    if i % 2 == 0:
        a.sort()
        print(a[i//2], end=" ")