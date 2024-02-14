n, k, p, T = tuple(map(int, input().split()))

inp = []
for _ in range(T):
    t, x, y = tuple(map(int, input().split()))
    inp.append((t,x,y))

inp.sort(key=lambda x : x[0])

arr = [0] * (n+1)
arr[p] = 1
cnt = 0
for elem in inp:
    if cnt < k and (arr[elem[1]] == 1 or arr[elem[2]] == 1) :
        cnt += 1
        arr[elem[1]] = 1
        arr[elem[2]] = 1
for i in range(1, n+1):
    print(arr[i], end='')