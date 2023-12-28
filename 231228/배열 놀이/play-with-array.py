n, q = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

for _ in range(q):
    qus = list(map(int, input().split()))
    if qus[0] == 1:
        print(arr[qus[1] - 1])
    elif qus[0] == 2:
        if qus[1] not in arr:
            print(0)
        else:
            print(arr.index(qus[1]) + 1)
    else:
        for i in range (qus[1] - 1, qus[2]):
            print(arr[i], end=" ")
        print()