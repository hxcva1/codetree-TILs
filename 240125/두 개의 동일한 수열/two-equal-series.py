n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()

flag = 1
for i in range(n):
    if arr1[i] != arr2[i]:
        flag = 0
        break
if flag:
    print("Yes")
else:
    print("No")