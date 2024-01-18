n = int(input())

def is_mul(n):
    sum_val = 0
    tmpn = n
    while tmpn > 0:
        sum_val += tmpn % 10
        tmpn //= 10
    return n % 2 == 0 and sum_val % 5 == 0
if is_mul(n):
    print("Yes")
else:
    print("No")