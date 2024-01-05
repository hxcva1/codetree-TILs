arr_2d = [
    input().split()
    for _ in range(5)
]
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[0])):
        print(arr_2d[i][j].upper(), end=" ")
    print()