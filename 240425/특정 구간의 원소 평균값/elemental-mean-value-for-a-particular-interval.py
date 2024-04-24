n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i,n):
        section = arr[i:j+1]
        aver = sum(section) / len(section)
        for elem in section:
            if elem == aver:
                cnt += 1
                break
print(cnt)