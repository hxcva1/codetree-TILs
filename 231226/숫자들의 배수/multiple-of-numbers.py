n = int(input())

cnt = 0
arr = [i * n for i in range(1, 11)]

for elem in arr:
    print(elem, end=" ")
    if (elem % 5 == 0):
        cnt += 1
    if cnt == 2:
        break