a = input()
n = len(a)
cnt = 0
for i in range(n-3):
    if a[i] == "(" and a[i+1] == "(":
        for j in range(i+2,n-1):
            if a[j] == ")" and a[j+1] == ")":
                cnt += 1
           
print(cnt)