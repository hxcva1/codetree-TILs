n = int(input())

d = {}
for _ in range(n):
    arr = list(input().split())
    if arr[0] == "add":
        d[int(arr[1])] = int(arr[2])
    if arr[0] == "find":
        if int(arr[1]) in d:
            print(d[int(arr[1])])
        else:
            print("None")
    if arr[0] == "remove":
        d.pop(int(arr[1]))