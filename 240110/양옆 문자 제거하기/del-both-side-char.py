s = input()

s = list(s)
s.pop(len(s)-2)
s.pop(2)
s = ''.join(s)
print(s)