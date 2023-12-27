arr = [0 for _ in range(5)]

for _ in range(3):
    inp = input().split()
    temp = int(inp[1])
    if (inp[0] == "Y"):
        if (temp >= 37):
            arr[0] += 1
        else:
            arr[2] += 1
    else:
        if (temp >= 37):
            arr[1] += 1
        else:
            arr[3] += 1
for i in range(4):
    print(arr[i], end=" ")
if arr[0] >= 2:
    print("E")