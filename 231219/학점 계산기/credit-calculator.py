n = int(input())

arr = list(map(float, input().split()))

ever = sum(arr) / len(arr)

print(f"{ever:.1f}")
if ever >= 4:
    print("Perfect")
elif ever >= 3:
    print("Good")
else:
    print("Poor")