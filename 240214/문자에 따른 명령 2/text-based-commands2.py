dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = input()

x, y = 0, 0
c_dir = 3
for elem in n:
    if elem == "L":
        c_dir = (c_dir + 4 - 1) % 4
    elif elem == "R":
        c_dir = (c_dir + 1) % 4
    else:
        x = x+ dx[c_dir]
        y = y+ dy[c_dir]
print(x, y)