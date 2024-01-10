string, c = tuple(input().split())

flag = string.find(c)

if flag == -1:
    print("No")
else:
    print(flag)