n, m = map(int, input().split())

def squre(n, m):
    for _ in range(n):
        for _ in range(m):
            print("1", end="")
        print()
squre(n,m)