n, k, p, T = tuple(map(int, input().split()))

inp = []
for _ in range(T):
    t, x, y = tuple(map(int, input().split()))
    inp.append((t,x,y))

inp.sort(key=lambda x : x[0])

arr = [0] * (n+2)
arr[p] = 1
cnt = 0
for elem in inp:
    if cnt < k and (arr[elem[1]] == 1 or arr[elem[2]] == 1) :
        cnt += 1
        arr[elem[1]] = 1
        arr[elem[2]] = 1

for i in range(1, n+1):
    print(arr[i], end='')
s = "01100100101001000111101010000000000001000000000100000101001110101100011010110"
t = "00100100101001000011001010000000000000000000000000000001001100101000010000100"