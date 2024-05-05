k, n = tuple(map(int, input().split()))

answer = []

def choose(curr_num):
    if curr_num == n:
        print(*answer, sep=" ")
        return
    for i in range(1, k+1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(0)