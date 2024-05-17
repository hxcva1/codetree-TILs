n = int(input())

s = set()
for _ in range(n):
    arr = list(input().split())
    if arr[0] == "add":
        s.add(int(arr[1]))
    if arr[0] == "find":
        if int(arr[1]) in s:
            print("true")
        else:
            print("false")
    if arr[0] == "remove":
        if int(arr[1]) in s:
            s.remove(int(arr[1]))