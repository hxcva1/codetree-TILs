n = int(input())

for i in range(1, n + 1):
    flag = 1
    tmp = i
    while tmp:
        if tmp % 10 == 3 or tmp % 10 == 6 or tmp % 10 == 9 or tmp % 3 == 0:
            flag = 0
            break
        tmp //= 10
    if flag:
        print(i, end=" ")
    else:
        print(0, end=" ")