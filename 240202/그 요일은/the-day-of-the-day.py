m1, d1, m2, d2 = map(int, input().split())
a = input()

m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
w = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
wdiff = 0
for i in range(7):
    if a == w[i]:
        wdiff = i

day1 = 0
day2 = 0

for i in range(1, m1):
    day1 += m[i]
day1 += d1
for i in range(1, m2):
    day2 += m[i]
day2 += d2
diff = day2 - day1
diff -= wdiff - 1
ret = diff // 7
if ret < 0:
    print(0)
else:
    print(ret+1)