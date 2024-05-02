n = int(input())

arr = [int(input()) for _ in range(n)]

s1, e1 = tuple(map(int, input().split()))
arr = arr[:s1-1] + arr[e1:]
s2, e2 = tuple(map(int, input().split()))
arr = arr[:s2-1] + arr[e2:]
print(len(arr))
for elem in arr:
    print(elem)