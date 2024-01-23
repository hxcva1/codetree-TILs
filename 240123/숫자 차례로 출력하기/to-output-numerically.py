n = int(input())

def func(num):
    if num == n + 1:
        print()
        return
    print(num, end=' ')
    func(num + 1)
    print(num, end=' ')

func(1)