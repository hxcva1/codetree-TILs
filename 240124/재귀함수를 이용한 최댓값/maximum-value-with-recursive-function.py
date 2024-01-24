n = int(input())

arr = list(map(int, input().split()))

ret = -1

def f(num):
    global ret
    if num == n:
        return
    if arr[num] > ret:
        ret = arr[num]
    f(num+1)

f(0)
print(ret)