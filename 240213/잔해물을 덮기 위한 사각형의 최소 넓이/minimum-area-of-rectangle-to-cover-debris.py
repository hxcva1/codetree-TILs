offset = 1000
arr = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i+offset][j+offset] = 1
x1, y1, x2, y2 = tuple(map(int, input().split()))
for i in range(x1, x2):
    for j in range(y1, y2):
        arr[i+offset][j+offset] = 0
mnx = mny = 2001
mxx = mxy = 0
flag = 1
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            if i < mnx:
                mnx = i
            if i > mxx:
                mxx = i
            if j < mny:
                mny = j
            if j > mxy:
                mxy = j
            flag = 0
if flag:
    print(0)
else:
    print((mxx-mnx+1) * (mxy - mny+1))