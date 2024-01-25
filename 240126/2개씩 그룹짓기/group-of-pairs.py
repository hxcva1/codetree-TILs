n = int(input())

arr = list(map(int, input().split()))
arr.sort()
arr1 = arr
arr2 = arr[::-1]
mx = arr1[0] + arr2[0]
for i in range(2*n):
    mx = max(mx, arr1[i]+arr2[i])
print(mx)