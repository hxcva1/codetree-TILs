n = int(input())

arr = list(map(int, input().split()))
arr.sort()
arr1 = arr[:n//2] + arr[-(n//2):]
arr2 = arr[n//2:-n//2]
print(max(sum(arr1), sum(arr2))