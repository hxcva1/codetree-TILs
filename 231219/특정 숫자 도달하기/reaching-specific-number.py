inp = list(map(int, input().split()))
arr = []

for elem in inp:
    if elem < 250:
        arr.append(elem)
    else:
        break
sum_val = 0
ever = 0

for elem in arr:
    sum_val += elem
if len(arr) == 0:
    ever = 0
else:
    ever = sum_val / len(arr)
print(f"{sum_val} {ever:.1f}")