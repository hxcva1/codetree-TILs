inp = input().split()
inp = list(map(int, inp))

while inp[0] <= inp[1]:
    print(inp[0], end=" ")
    if inp[0] % 2 == 1:
        inp[0] *= 2
    else:
        inp[0] += 3