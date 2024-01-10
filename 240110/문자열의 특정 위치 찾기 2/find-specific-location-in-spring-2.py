arr = ["apple", "banana", "grape", "blueberry", "orange"]

c = input()

cnt = 0
for elem in arr:
    if elem[2] == c or elem[3] == c:
        print(elem)
        cnt += 1
print(cnt)