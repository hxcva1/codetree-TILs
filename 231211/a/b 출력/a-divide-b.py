a = input().split()
b = int(a[1])
a = int(a[0])

print(f"{a//b}.", end="")
num = a%b
size = 0

while 1:
    num *= 10
    print(num // b, end="");
    num = num % b
    size += 1
    if (size == 20):
        break