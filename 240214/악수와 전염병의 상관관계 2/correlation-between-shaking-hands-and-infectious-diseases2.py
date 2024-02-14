n, k, p, T = tuple(map(int, input().split()))

inp = []
for _ in range(T):
    t, x, y = tuple(map(int, input().split()))
    inp.append((t,x,y))

inp.sort(key=lambda x : x[0])
arr = [0] * (n+1)
hand = [0] * (n+1)
arr[p] = 1
for elem in inp:
    if arr[elem[1]] == 1 and arr[elem[2]] == 1:
        hand[elem[1]] += 1
        hand[elem[2]] += 1
    if arr[elem[1]] == 1:
        if hand[elem[1]] < k:
            hand[elem[1]] += 1
            arr[elem[2]] = 1
    elif arr[elem[2]] == 1:
        if hand[elem[2]] < k:
            hand[elem[2]] += 1
            arr[elem[1]] = 1
for i in range(1, n+1):
    print(arr[i], end='')