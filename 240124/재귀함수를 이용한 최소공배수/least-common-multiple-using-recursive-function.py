n = int(input())

arr = list(map(int, input().split()))

# 최대공약수를 구하는 함수
def gcd(a, b):
    if b == 0:
        return a;
    return gcd(b, a % b)

#a가 현재 최소공배수여야 한다
def lcm(a, b, idx):
    if idx == n-1:
        return a*b//gcd(a,b)
    now = a * b // gcd(a,b)
    return lcm(now, arr[idx + 1], idx + 1)

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] * arr[1] // gcd(arr[0],arr[1]))
else:
    print(lcm(arr[0], arr[1], 1))