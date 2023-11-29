a = input().split()
t = int(a[0])
w = int(a[1])

bmi = (w * 10000) // (t * t)
print(bmi)
if bmi >= 25 :
    print("Obesity")