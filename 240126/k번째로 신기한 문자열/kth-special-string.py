n, k, T = input().split()
n = int(n)
k = int(k)

a = [
    input()
    for _ in range(n)
]

arr = [
    elem for elem in a if elem.find(T) != -1
]

arr.sort()
print(arr[k-1])