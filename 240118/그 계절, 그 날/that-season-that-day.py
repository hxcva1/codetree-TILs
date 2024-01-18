y, m, d = map(int, input().split())

flag = 0
def is_yoon(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return True
    return False

def season(m):
    if m >= 3 and m <= 5:
        return "Spring"
    elif m >= 6 and m <= 8:
        return "Summer"
    elif m >= 9 and m <= 11:
        return "Fall"
    elif: m == 12 or m >= 1 and m <= 2
        return "Winter"

if m == 2:
    if is_yoon:
        if d > 29:
            flag = 1
    else:
        if d > 28:
            flag = 1
elif m == 4 or m == 6 or m == 9 or m == 11:
    if d > 30:
        flag = 1

if flag == 1:
    print(-1)
else:
    print(season(m))