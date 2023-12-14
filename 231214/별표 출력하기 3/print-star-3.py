n = int(input())

for i in range (n):
    for _ in range(i):
        print("  ", end="")
    for _ in range(2*n -i*2 - 1):
        print("*", end=" ")
    print()