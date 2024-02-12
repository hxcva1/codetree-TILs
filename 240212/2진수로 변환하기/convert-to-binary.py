n = int(input())

def f(a):
    if a < 2:
        print(a%2,end='')
        return ;
    f(a // 2)
    print(a%2,end='')

f(n)