n = int(input())

def sum_ten(n):
    ret = 0
    for i in range(1, n+1):
        ret += i
    return ret // 10

print(sum_ten(n))