inp = input().split()
inp = list(map(int, inp))

if inp[0] > inp[1]:
    for i in range(inp[0], inp[1]-1, -1):
        print(i, end=" ")
else:
    for i in range(inp[1], inp[0]-1, -1):
        print(i, end=" ")