a, b, c = map(int, input().split())

start = 60*24*11 + 11*60 + 11
end = 60*24*a + 11*b + c
if end - start < 0:
    print(-1)
else:
    print(end - start)