n, m = map(int, input().split())

answer = []

def f(curr_num, num):
    if curr_num == m:
        print(*answer)
        return
    for i in range(num, n+1):
        answer.append(i)
        f(curr_num + 1, i + 1)
        answer.pop()
f(0, 1)