n = int(input())

arr = list(map(int, input().split()))

even = [elem for elem in arr if elem % 2 == 0]

for elem in even:
    print(elem, end=" ")