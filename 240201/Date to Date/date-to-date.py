a, b, c, d = map(int, input().split())

m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(c-1, a, -1):
    days += m[i]
days += d
days += m[a]-b+1
print(days)