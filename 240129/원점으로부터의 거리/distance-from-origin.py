n = int(input())

points = []
for i in range(n):
    x, y = tuple(map(int, input().split()))
    points.append((x,y, i+1))

points.sort(key=lambda x : (abs(x[0])+abs(x[1]), x[2]))

for p in points:
    print(p[2])