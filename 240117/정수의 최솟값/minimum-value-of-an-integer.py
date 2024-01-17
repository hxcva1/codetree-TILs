a, b, c = map(int, input().split())

def sum_val(a, b, c):
    return min(min(a,b),c)

print(sum_val(a, b, c))