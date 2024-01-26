n, k, T = input().split()
n = int(n)
k = int(k)

a = [
    input()
    for _ in range(n)
]

arr = [
    elem for elem in a if elem[:len(T)] == T
]

arr.sort()
print(arr[k-1])