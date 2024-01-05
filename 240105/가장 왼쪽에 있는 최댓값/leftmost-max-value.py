import sys

n = int(input())

arr = list(map(int, input().split()))

idx = n-1
while idx:
    mx = -sys.maxsize
    mxidx = 0
    for i in range(idx):
        if arr[i] > mx:
            mxidx = i
            mx = arr[i]
    print(mxidx+1, end=" ")
    idx = mxidx