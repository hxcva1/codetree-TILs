a, b = map(int, input().split())

def sub369(n):
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n //= 10
    return False 

def is_case(n):
    return n % 3 == 0 or sub369(n)

def cnt_369(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_case(i):
            cnt += 1
    return cnt

print(cnt_369(a, b))