arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

winner = 0
retx, rety = 0, 0
find = 0
end = 0
#가로방향 탐색
for i in range(19):
    cnt = 0
    for j in range(19):
        #백돌
        if arr[i][j] == 1:
            if prev == 1:
                cnt += 1
            else:
                cnt = 1
        #검은돌
        elif arr[i][j] == 2:
            if prev == 2:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
        prev = arr[i][j]
        if cnt == 5:
            winner = arr[i][j]
            retx, rety = i+1, j-1
            find = 1
            break
    if find:
        break
#세로
for i in range(19):
    cnt = 0
    for j in range(19):
        #백돌
        if arr[j][i] == 1:
            if prev == 1:
                cnt += 1
            else:
                cnt = 1
        #검은돌
        elif arr[j][i] == 2:
            if prev == 2:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
        prev = arr[j][i]
        if cnt == 5:
            winner = arr[j][i]
            retx, rety = j-1, i+1
            find = 1
            break
    if find:
        break
        print(cnt, end = ' ')

# 대각선 탐색
def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

start_x, start_y = 0, 0
while start_y != 19:
    x, y = start_x, start_y
    cnt = 0
    while in_range(x, y):
        #백돌
        if arr[x][y] == 1:
            if prev == 1:
                cnt += 1
            else:
                cnt = 1
        #검은돌
        elif arr[x][y] == 2:
            if prev == 2:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
        prev = arr[x][y]
        if cnt == 5:
            winner = arr[x][y]
            retx, rety = x - 1, y - 1
            find = 1
            break
        if find:
            break
        x += 1
        y += 1
    start_y += 1

start_x, start_y = 0, 0
while start_x != 19:
    x, y = start_x, start_y
    cnt = 0
    while in_range(x, y):
        #백돌
        if arr[x][y] == 1:
            if prev == 1:
                cnt += 1
            else:
                cnt = 1
        #검은돌
        elif arr[x][y] == 2:
            if prev == 2:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
        prev = arr[x][y]
        if cnt == 5:
            winner = arr[x][y]
            retx, rety = x - 1, y - 1
            find = 1
            break
        if find:
            break
        x += 1
        y += 1
    start_x += 1



start_x, start_y = 0, 18
while start_y != 0:
    x, y = start_x, start_y
    cnt = 0
    while in_range(x, y):
        #백돌
        if arr[x][y] == 1:
            if prev == 1:
                cnt += 1
            else:
                cnt = 1
        #검은돌
        elif arr[x][y] == 2:
            if prev == 2:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
        prev = arr[x][y]
        if cnt == 5:
            winner = arr[x][y]
            retx, rety = x - 1, y + 3
            find = 1
            break
        if find:
            break
        x += 1
        y -= 1
    start_y -= 1

start_x, start_y = 0, 18
while start_x != 19:
    x, y = start_x, start_y
    cnt = 0
    while in_range(x, y):
        #백돌
        if arr[x][y] == 1:
            if prev == 1:
                cnt += 1
            else:
                cnt = 1
        #검은돌
        elif arr[x][y] == 2:
            if prev == 2:
                cnt += 1
            else:
                cnt = 1
        else:
            cnt = 0
        prev = arr[x][y]
        if cnt == 5:
            winner = arr[x][y]
            retx, rety = x - 1, y + 3
            find = 1
            break
        if find:
            break
        x += 1
        y -= 1
    start_x += 1


if find and end == 0:
    print(winner)
    print(retx, rety)
    end = 1