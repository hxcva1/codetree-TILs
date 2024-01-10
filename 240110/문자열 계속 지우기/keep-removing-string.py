s = input()
t = input()

idx = s.find(t)
while idx != -1:
    s = s[0:idx] + s[idx+len(t):]
    idx = s.find(t)
print(s)