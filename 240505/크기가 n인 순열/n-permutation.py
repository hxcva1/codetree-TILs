n = int(input())

visit = [0] * (n + 1)
answer = []
def f(cur_num):
    if cur_num == n:
        print(*answer)
        return
    for i in range(1, n+1):
        if visit[i]:
            continue
        visit[i] = 1
        answer.append(i)
        f(cur_num + 1)
        visit[i] = 0
        answer.pop()
f(0)