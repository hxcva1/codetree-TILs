a = input()

cnt = 0
for i in range(n):
    if a[i] == "(":
        for j in range(i+1,n):
            if a[j] == "(":
                for k in range(j+1,n):
                    if a[k] == ")":
                        for l in range(k+1, n):
                            if a[l] == ")":
                                cnt += 1
print(cnt)