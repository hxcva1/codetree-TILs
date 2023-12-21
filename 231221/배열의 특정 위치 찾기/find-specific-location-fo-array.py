arr = list(map(int, input().split()))

arr2 = arr[1::2]
arr3 = arr[2::3]
print(f"{sum(arr2)} {sum(arr3)/len(arr3):.1f}")