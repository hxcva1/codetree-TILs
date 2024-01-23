string = input()

def palin(s):
    tmp = ""
    for i in range(len(s) - 1, -1, -1):
        tmp += s[i]
    if tmp == s:
        return True
    return False

if palin(string):
    print("Yes")
else:
    print("No")