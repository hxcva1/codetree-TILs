n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
cnt = 1
row = 0
for col in range(m):
    if (col == m - 1):
        while(row < n):
            tempc = col
            tempr = row
            while (tempc >= 0 and tempr < n):
                arr[tempr][tempc] = cnt
                cnt += 1
                tempc -= 1
                tempr += 1
            row += 1
        break
    tempc = col
    tempr = row
    while (tempc >= 0 and tempr < n):
        arr[tempr][tempc] = cnt
        cnt += 1
        tempc -= 1
        tempr += 1
    col += 1

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()