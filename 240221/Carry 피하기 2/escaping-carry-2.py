n = int(input())
arr = [
    input()
    for _ in range(n)
]

def f(a, b):
    for i in range(min(len(a), len(b))):
        if (int(a[len(a) -1 - i]) + int(b[len(b) -1 -i]) >= 10):
            return False
    return True

ret = 0 
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if f(arr[i], arr[j]):
                num = int(arr[i]) + int(arr[j])
            else:
                continue
            if f(str(num), arr[k]):
                num = num + int(arr[k])
                ret = max(ret, num)
print(ret)