n = int(input())

arr = []
inp = list(map(int, input().split()))
for i in range(n):
    arr.append((inp[i], i))
tmp = arr[:]
arr.sort(key=lambda x : x[0])
ret = []
for i in range(n):
    for j in range(n):
        if tmp[i] == arr[j]:
            ret.append(j+1)
    
for elem in ret:
    print(elem, end=' ')