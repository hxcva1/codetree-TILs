n, m = map(int, input().split())

adj_list = [
    []
    for _ in range(n+1)
]
visit = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

cnt = 0
def dfs(cur_node):
    visit[cur_node] = 1
    for next_node in adj_list[cur_node]:
        if visit[next_node]:
            continue
        global cnt
        cnt += 1
        dfs(next_node)

dfs(1)
print(cnt)