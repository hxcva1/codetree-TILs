n = int(input())

memo = [-1] * (n+1)

def f(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
        return memo[n]
    memo[n] = f(n-1) + f(n-2)
    return memo[n]


print(f(n))