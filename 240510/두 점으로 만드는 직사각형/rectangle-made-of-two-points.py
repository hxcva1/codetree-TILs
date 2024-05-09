x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

print(abs(min(x1,a1)- max(x2, a2)) * abs(min(y1,b1) - max(y2, b2)))