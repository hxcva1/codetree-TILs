string = input()

prev = string[0]
cnt = 0
ans = ""
for i in range(len(string)):
    if prev == string[i]:
        cnt += 1
    else:
        ans += prev
        ans += str(cnt)
        prev = string[i]
        cnt = 1
ans += prev
ans += str(cnt)
print(len(ans))
print(ans)