a, b = input().split()

s = ""
for elem in a:
    if elem >= '0' and elem <= '9':
        s += elem
    else:
        break
val = 0
val += int(s)

s = ""
for elem in b:
    if elem >= '0' and elem <= '9':
        s += elem
    else:
        break

val += int(s)
print(val)