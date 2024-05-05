k, n = map(int, input().split())

answer = []
def f(curr_num):
    if curr_num == n:
        print(*answer)
        return
    for i in range(1,k+1):
        if curr_num >= 2 and answer[-1] == answer[-2] and answer[-1] == i:
            continue
        answer.append(i)
        f(curr_num + 1)
        answer.pop()

f(0)