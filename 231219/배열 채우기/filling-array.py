inp = list(map(int, input().split()))
arr = []
for elem in inp:
    if elem == 0:
        break
    arr.append(elem)
for elem in arr[::-1]:
    print(elem, end=" ")