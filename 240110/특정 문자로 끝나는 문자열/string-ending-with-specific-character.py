arr = [
    input()
    for _ in range(10)
]

c = input()

flag = 0

for elem in arr:
    if elem[len(elem) - 1] == c:
        flag = 1
        print(elem)
if flag == 0:
    print("None")