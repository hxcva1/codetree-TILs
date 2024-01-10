n = input()
arr = input().split()

ans = "".join(arr)
for i in range(len(ans)):
    if i % 5 == 0 and i != 0:
        print()
    print(ans[i], end="")